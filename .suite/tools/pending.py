#!/usr/bin/env python3
"""Read-only list of approval requests that still need a person: pending, changes requested, expired.

Uses the same fail-closed replay as approval_audit.py. Writes nothing and decides nothing.
Logs come from --log or from approvals.logs in the dashboard configuration.
"""
import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from approval_audit import CheckError, summarize

CONFIG = Path(__file__).resolve().parents[1] / 'dashboard' / 'config.json'
OPEN = {'pending': 'Entscheidung offen', 'changes_requested': 'Überarbeitung nötig',
        'expired': 'Abgelaufen, neue Anfrage nötig'}


def configured_logs(config):
    data = json.loads(Path(config).read_text(encoding='utf-8'))
    return [(entry.get('label') or entry['id'], (Path(config).parent / entry['path']))
            for entry in data.get('approvals', {}).get('logs', [])]


def collect(logs, now=None):
    items, errors = [], []
    for label, path in logs:
        try:
            rows = summarize(path, now=now)
        except (CheckError, OSError, ValueError) as exc:
            # A broken log never yields an "all clear".
            errors.append({'log': label, 'error': str(exc)})
            continue
        items.extend(dict(row, log=label) for row in rows if row['status'] in OPEN)
    return items, errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--log', type=Path, action='append', default=[], help='approvals.jsonl, mehrfach möglich')
    parser.add_argument('--config', type=Path, default=CONFIG)
    parser.add_argument('--json', action='store_true')
    parser.add_argument('--strict', action='store_true', help='Exit 1, wenn etwas offen ist')
    args = parser.parse_args(argv)
    logs = [(str(p), p) for p in args.log] or configured_logs(args.config)
    if not logs:
        print('Keine Freigabeprotokolle angegeben oder in approvals.logs konfiguriert.', file=sys.stderr)
        return 2
    items, errors = collect(logs)
    if args.json:
        print(json.dumps({'open': items, 'errors': errors}, ensure_ascii=False, indent=2))
    else:
        for item in items:
            print('%-28s %-12s %-30s %s (%s)' % (OPEN[item['status']], item['module'], item['title'],
                                                item['path'], item['request_id']))
        for error in errors:
            print('PROTOKOLL NICHT LESBAR: %s – %s' % (error['log'], error['error']))
        if not items and not errors:
            print('Nichts offen.')
    if errors:
        return 2
    return 1 if args.strict and items else 0


if __name__ == '__main__':
    sys.exit(main())
