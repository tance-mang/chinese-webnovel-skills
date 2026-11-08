import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from types import SimpleNamespace as Obj
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'cli'))
from providers import ProviderError, ProviderRouter, error_message
import webnovel


class Stream:
    def __init__(self, *events):
        self.events = events

    def __enter__(self):
        return iter(self.events)

    def __exit__(self, *args):
        return False


def config():
    return {'base_url': 'https://example.test/v1', 'api_key': 'legacy-key', 'model': 'old',
            'providers': {'grok': {'kind': 'xai', 'model': 'mock-grok',
                                    'usd_input_per_million': 2, 'usd_output_per_million': 5},
                          'local': {'kind': 'ollama', 'model': 'mock-local'}},
            'routes': {'edit': 'local'}}


class ProviderTests(unittest.TestCase):
    def setUp(self):
        self.calls = []
        self.events = []
        self.messages = [{'role': 'user', 'content': 'test prompt'}]

    def factory(self, **opts):
        self.calls.append(('client', opts))
        def response(**data):
            self.calls.append(('responses', data))
            return Stream(*self.events)

        def chat(**data):
            self.calls.append(('chat', data))
            return Stream(Obj(choices=[Obj(delta=Obj(content='legacy reply'))]))

        return Obj(responses=Obj(create=response), chat=Obj(completions=Obj(create=chat)),
                   models=Obj(list=lambda: [Obj(id='mock-local')]))

    def test_legacy_configuration_uses_chat(self):
        router = ProviderRouter(config(), self.factory)
        self.assertEqual(list(router.stream(None, self.messages)), ['legacy reply'])
        self.assertEqual(self.calls[0][1]['api_key'], 'legacy-key')
        self.assertEqual(self.calls[1][1]['model'], 'old')

    def test_xai_responses_usage_and_cost(self):
        self.events = [Obj(type='response.output_text.delta', delta='Hello'),
                       Obj(type='response.completed', response=Obj(usage=Obj(input_tokens=4, output_tokens=2)))]
        with patch.dict(os.environ, {'XAI_API_KEY': 'mock-secret'}):
            router = ProviderRouter(config(), self.factory)
            self.assertEqual(list(router.stream(None, self.messages, 'grok')), ['Hello'])
        self.assertEqual(self.calls[0][1]['base_url'], 'https://api.x.ai/v1')
        self.assertEqual(self.calls[0][1]['max_retries'], 0)
        self.assertEqual(self.calls[1][1]['input'], self.messages)
        self.assertFalse(self.calls[1][1]['store'])
        self.assertEqual(router.usage, (4, 2))
        self.assertAlmostEqual(router.estimated_cost, .000018)

    def test_xai_explicit_chat_compatibility(self):
        cfg = config()
        cfg['providers']['grok']['api_mode'] = 'chat'
        with patch.dict(os.environ, {'XAI_API_KEY': 'mock-secret'}):
            self.assertEqual(list(ProviderRouter(cfg, self.factory).stream(None, self.messages, 'grok')),
                             ['legacy reply'])
        self.assertEqual(self.calls[-1][0], 'chat')

    def test_incomplete_or_refused_response_never_falls_back(self):
        for event in ('response.incomplete', 'response.refusal.delta', 'response.failed', 'response.created'):
            with self.subTest(event=event), patch.dict(os.environ, {'XAI_API_KEY': 'mock-secret'}):
                self.calls.clear()
                self.events = [Obj(type=event)]
                router = ProviderRouter(config(), self.factory)
                with self.assertRaises(ProviderError):
                    list(router.stream(None, self.messages, 'grok'))
                self.assertEqual([name for name, _ in self.calls], ['client', 'responses'])

    def test_local_health_does_not_generate(self):
        router = ProviderRouter(config(), self.factory)
        self.assertTrue(router.health('local'))
        self.assertEqual(self.calls[0][1]['api_key'], 'ollama')
        self.assertEqual(len(self.calls), 1)

    def test_cancel_switch_and_restore_legacy(self):
        cfg = config()
        router = ProviderRouter(cfg, self.factory)
        with patch('builtins.input', return_value='no'):
            webnovel.provider_command('/provider', 'local', cfg, router, self.messages)
        self.assertEqual(router.active, 'legacy')
        self.assertFalse(self.calls)
        with patch('builtins.input', return_value='yes'):
            webnovel.provider_command('/provider', 'local', cfg, router, self.messages)
            self.assertEqual(cfg['model'], 'mock-local')
            webnovel.provider_command('/provider', 'legacy', cfg, router, self.messages)
        self.assertEqual(cfg['model'], 'old')

    def test_compare_uses_same_input_without_private_history(self):
        cfg = config()
        router = ProviderRouter(cfg, self.factory)
        messages = [{'role': 'system', 'content': 'rules'}, {'role': 'user', 'content': 'unpublished chapter'}]
        with patch('builtins.input', return_value='yes'), contextlib.redirect_stdout(io.StringIO()):
            webnovel.provider_command('/compare', 'legacy,local same input', cfg, router, messages)
        sent = [args['messages'] for kind, args in self.calls if kind == 'chat']
        self.assertEqual(sent, [[messages[0], {'role': 'user', 'content': 'same input'}]] * 2)
        self.assertEqual(len(messages), 2)

    def test_error_message_excludes_credentials(self):
        class APIError(Exception):
            status_code = 429
        self.assertIn('限流', error_message(APIError('Authorization: mock-secret')))
        self.assertNotIn('mock-secret', error_message(APIError('Authorization: mock-secret')))
        self.assertIn('超时', error_message(TimeoutError('mock-secret')))

    def test_legacy_env_overrides_still_apply(self):
        with tempfile.TemporaryDirectory() as directory:
            cfg_path = Path(directory) / 'config.json'
            cfg_path.write_text(json.dumps(config()), encoding='utf-8')
            with patch.object(webnovel, 'CONFIG_PATH', str(cfg_path)), patch.dict(os.environ, {'WN_MODEL': 'override'}):
                self.assertEqual(webnovel.load_config()['model'], 'override')


class HandoffTests(unittest.TestCase):
    def test_export_and_import_without_overwriting(self):
        tool = ROOT / 'integrations' / 'grokbot' / 'handoff.py'
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            brief, task, result, output = [base / name for name in ('brief.md', 'task.md', 'result.json', 'review.json')]
            brief.write_text('Research a platform', encoding='utf-8')
            def run(*args):
                return subprocess.run([sys.executable, '-X', 'utf8', str(tool), *map(str, args)], capture_output=True)
            self.assertEqual(run('export', 'research', brief, task).returncode, 0)
            payload = json.loads(task.read_text(encoding='utf-8').split('<!-- TASK JSON -->\n')[1])
            self.assertEqual(payload['excerpt'], '')
            item = {'observation': 'observed', 'suggestion': 'check again', 'sources': ['javascript:bad']}
            record = {'schema': 1, 'task_id': payload['task_id'], 'findings': [item]}
            result.write_text(json.dumps(record), encoding='utf-8')
            self.assertNotEqual(run('import', task, result, output).returncode, 0)
            self.assertFalse(output.exists())
            item['sources'] = ['https://example.org/rules']
            result.write_text(json.dumps(record), encoding='utf-8')
            self.assertEqual(run('import', task, result, output).returncode, 0)
            original = output.read_bytes()
            self.assertEqual(json.loads(original)['findings'][0]['decision'], '待作者确认')
            self.assertNotEqual(run('import', task, result, output).returncode, 0)
            self.assertEqual(output.read_bytes(), original)
            self.assertEqual(brief.read_text(encoding='utf-8'), 'Research a platform')


class ExportTests(unittest.TestCase):
    def test_committed_exports_match_source_and_keep_old_commands(self):
        spec = importlib.util.spec_from_file_location('build_exports', ROOT / 'tools' / 'build_exports.py')
        builder = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(builder)
        skills, count = builder.build_skills()
        refs, ref_count = builder.build_references()
        self.assertGreaterEqual(count, 38)
        self.assertGreaterEqual(ref_count, 35)
        for name, content in [('knowledge-skills.md', skills), ('knowledge-references.md', refs)]:
            self.assertEqual((ROOT / 'exports' / name).read_text(encoding='utf-8'), content)
        for name in ('start', 'expand', 'cowrite', 'english', 'genre-style', 'globalize', 'intimacy', 'native-edit', 'model-router'):
            self.assertIn(f'## 技能：{name}\n', skills)
        for path in (ROOT / 'skills').glob('*/SKILL.md'):
            skill, description, _ = builder.strip_frontmatter(path.read_text(encoding='utf-8'))
            self.assertEqual(path.parent.name, skill)
            self.assertTrue(description)

    def test_platform_history_stays_out_of_active_english_routes(self):
        guide = (ROOT / 'references' / 'overseas-platforms.md').read_text(encoding='utf-8')
        self.assertIn('| Radish | 历史平台', guide)
        self.assertIn('2025-12-31', guide)
        self.assertIn('查阅日期：', guide)
        self.assertNotIn('Radish', (ROOT / 'skills' / 'english' / 'SKILL.md').read_text(encoding='utf-8'))

    def test_english_export_local_links_survive_concatenation(self):
        skills = (ROOT / 'exports' / 'knowledge-skills.md').read_text(encoding='utf-8')
        self.assertIn('](../references/english-genre-profiles.md)', skills)
        self.assertNotIn('](../../references/english-genre-profiles.md)', skills)
