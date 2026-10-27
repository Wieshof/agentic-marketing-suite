#!/usr/bin/env python3
"""Offline formal validator for Business-DNA JSONL. NOT a proof of factual truth."""
import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

STATUSES = {'verified','declared','planned','hypothesis','disputed','superseded','rejected','unknown'}
VISIBILITIES = {'public','shared','restricted'}
STRONG_EVIDENCE = {'official_register','primary_document','technical_test','audited_record'}
SOURCE_KINDS = STRONG_EVIDENCE | {'human_statement','internal_record','external_publication','derived_analysis'}

def load_jsonl(path):
    records=[]
    for number,line in enumerate(Path(path).read_text(encoding='utf-8').splitlines(),1):
        if not line.strip(): continue
        try:
            item=json.loads(line)
        except json.JSONDecodeError as ex:
            raise ValueError(f'{path}:{number}: invalid JSON: {ex}') from ex
        if not isinstance(item,dict): raise ValueError(f'{path}:{number}: must be an object')
        records.append(item)
    return records

def valid_datetime(value):
    try:
        if not isinstance(value,str): return False
        datetime.fromisoformat(value.replace('Z','+00:00'))
        return True
    except (TypeError,ValueError): return False

def validate_claims(claims,sources):
    errors=[]; ids=set(); src={}
    for source in sources:
        key=source.get('source_id')
        if not key or not isinstance(key,str): errors.append('source missing source_id'); continue
        if key in src: errors.append(f'duplicate source_id {key}')
        src[key]=source
        if source.get('kind') not in SOURCE_KINDS: errors.append(f'{key}: unknown source kind')
        if source.get('visibility') not in VISIBILITIES: errors.append(f'{key}: invalid source visibility')
        if not isinstance(source.get('locator'),str) or not source['locator'].strip(): errors.append(f'{key}: missing locator')
        if not valid_datetime(source.get('captured_at')): errors.append(f'{key}: invalid captured_at')
    for item in claims:
        key=item.get('claim_id')
        if not isinstance(key,str) or not key.strip(): errors.append('claim missing claim_id'); continue
        if key in ids: errors.append(f'duplicate claim_id {key}')
        ids.add(key)
        for req in ('subject','predicate'):
            if not isinstance(item.get(req),str) or not item[req].strip(): errors.append(f'{key}: missing {req}')
        if 'value' not in item: errors.append(f'{key}: missing value')
        if item.get('status') not in STATUSES: errors.append(f'{key}: invalid status')
        if item.get('visibility') not in VISIBILITIES: errors.append(f'{key}: invalid visibility')
        if type(item.get('version')) is not int or item['version']<1: errors.append(f'{key}: invalid version')
        if not valid_datetime(item.get('updated_at')): errors.append(f'{key}: invalid updated_at')
        refs=item.get('source_refs')
        if not isinstance(refs,list) or any(not isinstance(s,str) for s in refs):
            errors.append(f'{key}: source_refs must be list of IDs'); refs=[]
        for ref in refs:
            if ref not in src: errors.append(f'{key}: missing source {ref}')
        if item.get('status')=='verified' and not any(src.get(ref,{}).get('kind') in STRONG_EVIDENCE for ref in refs):
            errors.append(f'{key}: verified without an eligible evidence source')
        if item.get('status') in {'superseded','rejected'} and not refs:
            errors.append(f'{key}: historical/rejected claim needs referenced provenance')
        if item.get('status')=='planned' and item.get('predicate')=='is_production_ready' and item.get('value') is True:
            errors.append(f'{key}: planned cannot assert current production readiness as fact')
    return errors

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('claims',type=Path)
    ap.add_argument('--sources',type=Path,required=True)
    args=ap.parse_args()
    try: errors=validate_claims(load_jsonl(args.claims),load_jsonl(args.sources))
    except (OSError,ValueError) as ex:
        print(f'FAIL: {ex}',file=sys.stderr); return 2
    if errors:
        for error in errors: print('ERROR:',error,file=sys.stderr)
        print(f'FAIL {len(errors)} issue(s)',file=sys.stderr);return 1
    print('PASS: formal consistency checks; content accuracy NOT verified')
    return 0
if __name__=='__main__': sys.exit(main())
