#!/usr/bin/env python3
"""Conservative local publication-job preflight; NO network, NO publishing."""
import sys, json, pathlib, re, datetime
ALLOWED_CHANNELS=set("linkedin instagram facebook threads tiktok youtube pinterest x bluesky mastodon reddit telegram whatsapp-channels discord".split())
ALLOWED_FORMATS=set("text-post image-post carousel story reel short tiktok-video long-video live infografik umfrage dokument-post thread podcast-clip behind-the-scenes community-antwort".split())
PUBLISH_STATES={'approved','scheduled','publishing','published'}
def main(path):
    data=json.loads(pathlib.Path(path).read_text(encoding='utf-8'))
    errors=[]; notes=[]
    keys=['schema_version','job_id','content_id','variant_id','channel','account_id','format','status','copy','assets','scheduled_at','approval']
    for key in keys:
        if key not in data: errors.append('missing key: '+key)
    if data.get('schema_version')!='0.1': errors.append('unknown schema version')
    if data.get('channel') not in ALLOWED_CHANNELS: errors.append('invalid channel')
    if data.get('format') not in ALLOWED_FORMATS: errors.append('invalid format')
    approval=data.get('approval') or {}
    state=data.get('status')
    if state in PUBLISH_STATES:
        if not approval.get('content_approved'): errors.append('publication state without content approval')
        if not approval.get('execution_authorized'): errors.append('publication state without execution authorization')
        if not approval.get('revision_sha256'): errors.append('publication state without revision fingerprint')
    if state=='published' and not data.get('external_post_id'):
        errors.append('published without remote platform post id')
    if not isinstance(data.get('assets',[]),list): errors.append('assets not a list')
    else:
        for i,a in enumerate(data.get('assets',[])):
            if not isinstance(a,dict): errors.append(f'asset {i} invalid'); continue
            if a.get('rights_status')!='cleared' and state in PUBLISH_STATES:
                errors.append(f'asset {i} rights not cleared')
            if not re.fullmatch(r'[a-fA-F0-9]{64}',str(a.get('sha256',''))):
                errors.append(f'asset {i} missing SHA256 (content must be validated before publishing)')
    if data.get('scheduled_at'):
        try:
            timestamp=datetime.datetime.fromisoformat(data['scheduled_at'].replace('Z','+00:00'))
            if timestamp.tzinfo is None: errors.append('scheduled_at lacks timezone')
        except (ValueError,TypeError): errors.append('invalid scheduled_at')
    notes.extend(['This is a local syntax/approval sanity check only.','Account ownership, API scopes, live platform limits, content quality and licenses are NOT verified.','Nothing was scheduled or published.'])
    print(json.dumps({'ok_local':not errors,'errors':errors,'notes':notes},ensure_ascii=False,indent=2))
    return 0 if not errors else 2
if __name__=='__main__':
    if len(sys.argv)!=2:
        print('usage: python3 validate_job.py job.json',file=sys.stderr); sys.exit(2)
    sys.exit(main(sys.argv[1]))
