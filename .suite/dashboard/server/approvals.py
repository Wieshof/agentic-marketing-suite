"""Read-only, explicitly configured approval sources; never record decisions or execute actions."""
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'tools'))
from approval_audit import CheckError, summarize

MAX_LOG_BYTES = 10 * 1024 * 1024
DISPLAY_FIELDS = ('request_id', 'title', 'module', 'path', 'artifact_version', 'status',
                  'event_type', 'actor', 'actor_role', 'occurred_at', 'recorded_at', 'reason',
                  'budget_limit', 'currency')


def configure_approvals(config, directory):
    section = config.setdefault('approvals', {})
    if not isinstance(section, dict):
        raise ValueError('approvals muss ein JSON-Objekt sein.')
    logs = section.setdefault('logs', [])
    if not isinstance(logs, list):
        raise ValueError('approvals.logs muss eine Liste sein.')
    ids, paths = set(), set()
    for source in logs:
        if (not isinstance(source, dict) or set(source) != {'id', 'label', 'path'}
                or not all(isinstance(source[key], str) and source[key].strip() for key in ('id', 'label', 'path'))):
            raise ValueError('Jedes Freigabeprotokoll benötigt id, label und path.')
        if not re.fullmatch(r'[a-zA-Z0-9_-]+', source['id']) or source['id'] in ids:
            raise ValueError('Freigabeprotokoll-IDs müssen eindeutig sein und dürfen keine Pfade enthalten.')
        path = (Path(directory) / source['path']).absolute()
        if path.suffix.lower() != '.jsonl' or '://' in source['path']:
            raise ValueError('Freigabeprotokolle müssen lokale JSONL-Dateien sein.')
        identity = path.resolve()
        if identity in paths:
            raise ValueError('Ein Freigabeprotokoll darf nur einmal konfiguriert sein.')
        ids.add(source['id'])
        paths.add(identity)
        source['path'] = str(path)


class ApprovalView:
    def __init__(self, sources):
        self.sources = sources

    def snapshot(self):
        sources, items = [], []
        for source in self.sources:
            # Neither private absolute paths nor executable approval candidates reach the browser.
            public = {'id': source['id'], 'label': source['label']}
            path = Path(source['path'])
            try:
                if path.is_symlink():
                    raise CheckError('Symlinked log')
                if not path.is_file():
                    public.update(status='unavailable', notice='Das Freigabeprotokoll ist nicht verfügbar.')
                elif path.with_name(path.name + '.lock').exists():
                    public.update(status='updating', notice='Das Freigabeprotokoll wird gerade aktualisiert.')
                else:
                    rows = summarize(path, max_bytes=MAX_LOG_BYTES)
                    if path.with_name(path.name + '.lock').exists():
                        public.update(status='updating', notice='Das Freigabeprotokoll wird gerade aktualisiert.')
                    else:
                        public['status'] = 'ok'
                        items.extend({'source_id': source['id'],
                                      **{key: row[key] for key in DISPLAY_FIELDS if key in row}} for row in rows)
            except (CheckError, OSError, ValueError):
                public.update(status='invalid', notice='Das Freigabeprotokoll kann derzeit nicht verlässlich angezeigt werden.')
            sources.append(public)
        return {'configured': bool(self.sources), 'sources': sources, 'items': items}
