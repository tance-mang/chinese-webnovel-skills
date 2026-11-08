import contextlib
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

try:
    import httpx
    import openai
except ImportError:
    httpx = openai = None

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'cli'))
import webnovel


@unittest.skipIf(openai is None or httpx is None, 'Requires the CLI OpenAI SDK')
class GrokCliTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.requests = []
        self.sdk = openai.OpenAI
        self.completed = True
        self.stdout, self.stderr = io.StringIO(), io.StringIO()

    def transport(self, request):
        self.requests.append(request)
        if request.method == 'GET':
            return httpx.Response(200, json={'object': 'list', 'data': [{'id': 'test-grok', 'created': 0,
                                                                       'object': 'model', 'owned_by': 'xai'}]})
        events = [{'type': 'response.output_text.delta', 'delta': '第2章 归来\n\n灯亮了。'}]
        if self.completed:
            events.append({'type': 'response.completed', 'response': {
                'usage': {'input_tokens': 100, 'output_tokens': 20, 'total_tokens': 120}}})
        sse = ''.join('data: ' + json.dumps(event) + '\n\n' for event in events)
        return httpx.Response(200, headers={'content-type': 'text/event-stream'}, text=sse)

    def client(self, **options):
        return self.sdk(**options, http_client=httpx.Client(transport=httpx.MockTransport(self.transport)))

    def run_cli(self, *args, key='unit-test-secret'):
        with patch.dict(os.environ, {'XAI_API_KEY': key, 'XAI_MODEL': ''}), \
                patch.object(webnovel, 'CONFIG_PATH', str(self.root / 'absent.json')), \
                patch.object(openai, 'OpenAI', side_effect=self.client), \
                contextlib.redirect_stdout(self.stdout), contextlib.redirect_stderr(self.stderr):
            return webnovel.main(['--grok', *map(str, args)])

    def test_discovers_model_without_config_or_preselected_model(self):
        self.assertEqual(self.run_cli('--models'), 0)
        self.assertEqual(self.stdout.getvalue(), 'test-grok\n')
        self.assertEqual([(r.method, r.url.host, r.url.path) for r in self.requests],
                         [('GET', 'api.x.ai', '/v1/models')])

    def test_writing_files_flow_through_responses_and_save_utf8(self):
        brief, source, output = [self.root / name for name in ('brief.txt', 'original.txt', 'draft.txt')]
        brief.write_text('只写第二章', encoding='utf-8-sig')
        source.write_text('第一章在熄灯时结束。', encoding='utf-8')
        self.assertEqual(self.run_cli('--model', 'test-grok', '--workflow', 'continue',
                                      '--prompt-file', brief, '--source-file', source,
                                      '--max-output-tokens', 500, '--output', output), 0)
        request, = self.requests
        payload = json.loads(request.content)
        self.assertEqual((request.method, request.url.path), ('POST', '/v1/responses'))
        self.assertEqual(payload['model'], 'test-grok')
        self.assertEqual(payload['max_output_tokens'], 500)
        self.assertFalse(payload['store'])
        self.assertIn('当前任务模式 continue', payload['input'][0]['content'])
        self.assertIn('只写第二章', payload['input'][1]['content'])
        self.assertIn('第一章在熄灯时结束。', payload['input'][1]['content'])
        self.assertEqual(output.read_bytes().decode('utf-8'), '第2章 归来\n\n灯亮了。\n')
        self.assertEqual(source.read_text(encoding='utf-8'), '第一章在熄灯时结束。')
        self.assertNotIn('unit-test-secret', self.stdout.getvalue() + self.stderr.getvalue())

    def test_missing_key_never_sends_a_request(self):
        self.assertEqual(self.run_cli('--model', 'test-grok', '写一段', key=''), 1)
        self.assertIn('XAI_API_KEY', self.stderr.getvalue())
        self.assertFalse(self.requests)

    def test_existing_output_rejected_before_request(self):
        output = self.root / 'draft.txt'
        output.write_bytes(b'keep')
        with self.assertRaises(SystemExit) as err:
            self.run_cli('--model', 'test-grok', '--output', output, '写一段')
        self.assertEqual(err.exception.code, 2)
        self.assertFalse(self.requests)
        self.assertEqual(output.read_bytes(), b'keep')

    def test_interrupted_response_does_not_save_draft(self):
        self.completed = False
        output = self.root / 'draft.txt'
        self.assertEqual(self.run_cli('--model', 'test-grok', '--output', output, '写一段'), 1)
        self.assertFalse(output.exists())
        self.assertEqual(len(self.requests), 1)
