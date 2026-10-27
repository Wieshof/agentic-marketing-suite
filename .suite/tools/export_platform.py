#!/usr/bin/env python3
"""Approved suite records -> import files for a manual upload (Google Ads Editor, social schedulers, email).

No network, no credentials, no platform action: a person imports the file and decides
in the platform. Writing an export requires the current human approval of exactly this
source file (see .suite/APPROVALS.md); --check only validates and writes nothing.
"""
import argparse
import csv
from decimal import Decimal
import hashlib
import html
import io
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'capabilities'))
from runtime import CapabilityError, relative_file, require_approval, summarize, write_new

ROOT = Path(__file__).resolve().parents[2]
# The human decision an import prepares; a paused Ads campaign still becomes spend once enabled.
ACTIONS = {'google-ads': 'spend', 'social-csv': 'publish', 'email-html': 'send'}
ADS_LIMITS = {'headline': 30, 'description': 90, 'path': 15}
ADS_MATCH = {'broad': 'Broad', 'phrase': 'Phrase', 'exact': 'Exact'}
ADS_COLUMNS = (['Campaign', 'Campaign Type', 'Campaign Status', 'Budget', 'Ad Group', 'Keyword',
                'Criterion Type', 'Ad type'] + ['Headline %d' % i for i in range(1, 16)]
               + ['Description %d' % i for i in range(1, 5)] + ['Path 1', 'Path 2', 'Final URL'])
# Buffer bulk upload columns; verify against the current scheduler documentation before release.
SOCIAL_COLUMNS = ['Text', 'Image URL', 'Tags', 'Posting Time']


def _text(value, name, errors, limit=None):
    if not isinstance(value, str) or not value.strip():
        errors.append(name + ' fehlt')
        return ''
    if limit and len(value) > limit:
        errors.append('%s länger als %d Zeichen' % (name, limit))
    return value


def check_google_ads(manifest):
    errors = []
    if manifest.get('platform') != 'google-ads':
        errors.append("platform muss 'google-ads' sein")
    ads = manifest.get('search_ads')
    if not isinstance(ads, dict) or not isinstance(ads.get('ad_groups'), list) or not ads['ad_groups']:
        return errors + ['search_ads.ad_groups fehlt']
    _text(ads.get('campaign_name'), 'search_ads.campaign_name', errors)
    for n, group in enumerate(ads['ad_groups'], 1):
        name = 'Anzeigengruppe %d' % n
        _text(group.get('name'), name + ': name', errors)
        if not str(group.get('final_url', '')).startswith('https://'):
            errors.append(name + ': final_url muss mit https:// beginnen')
        headlines, descriptions = group.get('headlines') or [], group.get('descriptions') or []
        if not 3 <= len(headlines) <= 15:
            errors.append(name + ': 3 bis 15 Headlines nötig')
        if not 2 <= len(descriptions) <= 4:
            errors.append(name + ': 2 bis 4 Descriptions nötig')
        for i, value in enumerate(headlines, 1):
            _text(value, '%s: Headline %d' % (name, i), errors, ADS_LIMITS['headline'])
        for i, value in enumerate(descriptions, 1):
            _text(value, '%s: Description %d' % (name, i), errors, ADS_LIMITS['description'])
        for key in ('path1', 'path2'):
            if len(group.get(key) or '') > ADS_LIMITS['path']:
                errors.append('%s: %s länger als %d Zeichen' % (name, key, ADS_LIMITS['path']))
        for keyword in group.get('keywords') or []:
            if not isinstance(keyword, dict) or keyword.get('match') not in ADS_MATCH:
                errors.append(name + ': Keyword braucht text und match (broad|phrase|exact)')
            else:
                _text(keyword.get('text'), name + ': Keyword', errors, 80)
    return errors


def rows_google_ads(manifest):
    ads = manifest['search_ads']
    campaign = ads['campaign_name']
    # The campaign is always created paused: enabling it in Ads Editor is the spend decision.
    rows = [{'Campaign': campaign, 'Campaign Type': 'Search', 'Campaign Status': 'Paused',
             'Budget': manifest['budget']['daily_max']}]
    for group in ads['ad_groups']:
        ad = {'Campaign': campaign, 'Ad Group': group['name'], 'Ad type': 'Responsive search ad',
              'Path 1': group.get('path1', ''), 'Path 2': group.get('path2', ''), 'Final URL': group['final_url']}
        ad.update({'Headline %d' % i: v for i, v in enumerate(group['headlines'], 1)})
        ad.update({'Description %d' % i: v for i, v in enumerate(group['descriptions'], 1)})
        rows.append(ad)
        rows.extend({'Campaign': campaign, 'Ad Group': group['name'], 'Keyword': k['text'],
                     'Criterion Type': ADS_MATCH[k['match']]} for k in group.get('keywords') or [])
    return ADS_COLUMNS, rows


def check_social(jobs):
    errors = []
    for job in jobs if isinstance(jobs, list) else [jobs]:
        name = 'Job %s' % job.get('job_id', '?')
        _text(job.get('copy'), name + ': copy', errors)
        for asset in job.get('assets') or []:
            if not isinstance(asset, str) or not asset.startswith('https://'):
                errors.append(name + ': Assets für den Import müssen öffentliche https-URLs sein')
    return errors


def rows_social(jobs):
    rows = [{'Text': j['copy'], 'Image URL': (j.get('assets') or [''])[0],
             'Tags': j.get('channel', ''), 'Posting Time': j.get('scheduled_at') or ''}
            for j in (jobs if isinstance(jobs, list) else [jobs])]
    return SOCIAL_COLUMNS, rows


def check_email(draft):
    errors = []
    if draft.get('channel') != 'email':
        errors.append("channel muss 'email' sein")
    _text(draft.get('subject'), 'subject', errors, 150)
    _text(draft.get('body'), 'body', errors)
    return errors


def render_email(draft):
    paragraphs = [p.strip() for p in draft['body'].replace('\r\n', '\n').split('\n\n') if p.strip()]
    body = '\n'.join('<p>%s</p>' % html.escape(p).replace('\n', '<br>\n') for p in paragraphs)
    page = ('<!doctype html>\n<html><head><meta charset="utf-8"><title>%s</title></head>\n'
            '<body>\n%s\n</body></html>\n') % (html.escape(draft['subject']), body)
    return {'subject.txt': draft['subject'] + '\n', 'body.html': page, 'body.txt': draft['body'] + '\n'}


CHECKS = {'google-ads': check_google_ads, 'social-csv': check_social, 'email-html': check_email}


def to_csv(columns, rows):
    stream = io.StringIO()
    writer = csv.DictWriter(stream, fieldnames=columns, lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue()


def export(kind, source, out, root=ROOT, log=None, request_id=None, target=None, check_only=False):
    source = relative_file(root, Path(source).resolve(strict=True).relative_to(Path(root).resolve()).as_posix())
    data = source.read_bytes()
    record = json.loads(data.decode('utf-8'))
    errors = CHECKS[kind](record)
    if errors:
        raise CapabilityError('; '.join(errors))
    if check_only:
        return {'check': 'pass', 'written': []}
    if not (log and request_id and target):
        raise CapabilityError('Export braucht --log, --request-id und --target einer menschlichen Freigabe')
    # Parsed bytes must be the approved snapshot; require_approval re-hashes the file on disk.
    approval = require_approval(log, request_id, root, source, ACTIONS[kind], target,
                                hashlib.sha256(data).hexdigest())
    if kind == 'google-ads':
        # A spend approval is bound to a budget; the campaign may not exceed it.
        row = next(r for r in summarize(log) if r['request_id'] == request_id)
        if (row.get('currency') != record.get('currency')
                or Decimal(record['budget']['lifetime_max']) > Decimal(str(row.get('budget_limit', -1)))):
            raise CapabilityError('Kampagnenbudget oder Währung über der Freigabe')
    out = Path(out)
    if kind == 'email-html':
        out.mkdir(parents=True, exist_ok=False)
        files = {out / name: text for name, text in render_email(record).items()}
    else:
        files = {out: to_csv(*(rows_google_ads if kind == 'google-ads' else rows_social)(record))}
    for path, text in files.items():
        write_new(path, text.encode('utf-8'))
    return {'written': [str(p) for p in files], 'approval': approval,
            'note': 'Nur Importdatei erzeugt; keine Plattformaktion ausgeführt.'}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('kind', choices=sorted(CHECKS))
    parser.add_argument('source', type=Path, help='Freigegebene Quelldatei innerhalb von --root')
    parser.add_argument('--out', type=Path, help='Neue Zieldatei bzw. neuer Ordner (email-html)')
    parser.add_argument('--check', action='store_true', help='Nur prüfen, nichts schreiben')
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--log', type=Path, help='approvals.jsonl')
    parser.add_argument('--request-id')
    parser.add_argument('--target', help='Exakter Zielstring der Freigabe, z. B. google-ads:123-456-7890')
    args = parser.parse_args(argv)
    if not args.check and not args.out:
        parser.error('--out ist ohne --check erforderlich')
    try:
        result = export(args.kind, args.source, args.out, args.root, args.log, args.request_id,
                        args.target, args.check)
    except (CapabilityError, OSError, ValueError) as exc:
        print('EXPORT_BLOCKED:', exc, file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    sys.exit(main())
