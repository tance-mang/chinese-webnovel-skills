"""Offline task exchange. Imported material is evidence to review, never instructions."""
import argparse
import hashlib
import json
from pathlib import Path
from urllib.parse import urlsplit


def make_task(kind, brief, excerpt=''):
    task = {'schema': 1, 'kind': kind, 'brief': brief.strip(), 'excerpt': excerpt}
    if not task['brief']:
        raise ValueError('任务说明不能为空。')
    payload = json.dumps(task, ensure_ascii=False, sort_keys=True).encode('utf-8')
    return {**task, 'task_id': hashlib.sha256(payload).hexdigest()}


def review(task, result):
    if (not isinstance(result, dict) or result.get('schema') != 1 or
            result.get('task_id') != task['task_id'] or not isinstance(result.get('findings'), list) or
            not result['findings']):
        raise ValueError('结果格式不符，或 task_id 与交接任务不一致。')
    findings = []
    for item in result['findings']:
        if not isinstance(item, dict) or not all(isinstance(item.get(k), str) and item[k].strip()
                                                for k in ('observation', 'suggestion')):
            raise ValueError('每条发现须有 observation 和 suggestion。')
        sources = item.get('sources', [])
        if not isinstance(sources, list):
            raise ValueError('sources 须为 URL 列表。')
        for source in sources:
            if not isinstance(source, str):
                raise ValueError('来源须为 HTTP(S) URL。')
            url = urlsplit(source)
            if url.scheme not in ('https', 'http') or not url.hostname or url.username or url.password:
                raise ValueError('来源须为无凭据的 HTTP(S) URL。')
        findings.append({'observation': item['observation'], 'suggestion': item['suggestion'],
                         'sources': sources, 'source_status': '待复核' if sources else '未提供来源',
                         'decision': '待作者确认'})
    return {'schema': 1, 'task_id': task['task_id'], 'findings': findings}


def write_new(path, content):
    with path.open('x', encoding='utf-8', newline='\n') as file:
        file.write(content)


def json_text(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + '\n'


def main():
    parser = argparse.ArgumentParser(description='手动交接研究、写作或评审任务，所有操作在本机完成。')
    sub = parser.add_subparsers(dest='command', required=True)
    export = sub.add_parser('export')
    export.add_argument('kind', choices=('research', 'review', 'writing'))
    export.add_argument('brief', type=Path, help='UTF-8 任务说明')
    export.add_argument('output', type=Path, help='新建 .md 或 .json')
    export.add_argument('--excerpt', type=Path, help='仅纳入作者明确选择的 UTF-8 片段')
    ingest = sub.add_parser('import')
    ingest.add_argument('task', type=Path, help='原始 .md 或 .json 任务包')
    ingest.add_argument('result', type=Path, help='外部评审返回的 JSON')
    ingest.add_argument('output', type=Path, help='新的待审 JSON 文件')
    args = parser.parse_args()

    try:
        if args.command == 'export':
            brief = args.brief.read_text(encoding='utf-8-sig')
            excerpt = args.excerpt.read_text(encoding='utf-8-sig') if args.excerpt else ''
            data = make_task(args.kind, brief, excerpt)
            payload = json_text(data)
            if args.output.suffix.lower() == '.md':
                payload = ('# 手动交接任务\n\n按 README 所列结果 JSON 格式回传，引用可复查的公开来源。\n\n'
                           '<!-- TASK JSON -->\n' + payload)
            elif args.output.suffix.lower() != '.json':
                raise ValueError('任务输出须为 .md 或 .json。')
        else:
            if args.output.suffix.lower() != '.json':
                raise ValueError('待审输出须为 .json。')
            task_text = args.task.read_text(encoding='utf-8-sig')
            if args.task.suffix.lower() == '.md':
                task_text = task_text.split('<!-- TASK JSON -->\n', 1)[1]
            task = json.loads(task_text)
            if task != make_task(task['kind'], task['brief'], task['excerpt']):
                raise ValueError('原始任务内容或 ID 已变更。')
            payload = json_text(review(task, json.loads(args.result.read_text(encoding='utf-8-sig'))))
        write_new(args.output, payload)
    except (OSError, ValueError, KeyError, IndexError, TypeError) as exc:
        parser.exit(1, '操作失败，未覆盖已有文件。' + (f' {exc}' if isinstance(exc, ValueError) else '') + '\n')
    print(args.output)


if __name__ == '__main__':
    main()
