#!/usr/bin/env python3
"""Preflight for the four *bounded* suite JSON contracts; no network/side effects.
This is NOT a full JSON Schema, security, compliance or legal validator.
"""
import argparse, json, re, sys
from datetime import datetime, timezone
from pathlib import Path

HERE=Path(__file__).resolve().parents[1]
SCHEMA_NAMES=('work-order','artifact','review','action-approval')
class CheckError(Exception):pass

def check(name, record):
    if name not in SCHEMA_NAMES:raise CheckError('unknown contract')
    schema=json.loads((HERE/'contracts'/f'{name}.schema.json').read_text(encoding='utf8'))
    if not isinstance(record,dict):raise CheckError('object expected')
    errors=[]
    fields=schema['properties']
    for r in schema.get('required',[]):
        if r not in record:errors.append('required missing: '+r)
    for key,value in record.items():
        spec=fields.get(key)
        if spec is None:
            errors.append('unexpected field: '+key);continue
        typ=spec.get('type')
        if typ=='string' and not isinstance(value,str):errors.append(key+': string expected');continue
        if typ=='integer' and (not isinstance(value,int) or isinstance(value,bool)):errors.append(key+': integer expected');continue
        if typ=='boolean' and not isinstance(value,bool):errors.append(key+': boolean expected');continue
        if typ=='number' and (not isinstance(value,(int,float)) or isinstance(value,bool)):errors.append(key+': number expected');continue
        if typ=='array' and not isinstance(value,list):errors.append(key+': array expected');continue
        if isinstance(value,str):
            if len(value)<spec.get('minLength',0):errors.append(key+': too short')
            if 'enum' in spec and value not in spec['enum']:errors.append(key+': invalid enum')
            if 'pattern' in spec and re.fullmatch(spec['pattern'],value) is None:errors.append(key+': invalid pattern')
            if spec.get('format')=='date-time':
                try:
                    x=datetime.fromisoformat(value.replace('Z','+00:00'))
                    if x.tzinfo is None:errors.append(key+': timezone required')
                except ValueError:errors.append(key+': invalid datetime')
        elif isinstance(value,(int,float)) and not isinstance(value,bool):
            if value<spec.get('minimum',float('-inf')):errors.append(key+': below minimum')
        if isinstance(value,list):
            if spec.get('uniqueItems') and len({json.dumps(v,sort_keys=True) for v in value})<len(value):errors.append(key+': duplicate')
            if key=='findings':
                for i,f in enumerate(value):
                    if not isinstance(f,dict) or not isinstance(f.get('message'),str) or f.get('severity') not in ('info','minor','major','critical'):
                        errors.append(f'findings[{i}]: invalid object')
            elif spec.get('items',{}).get('enum'):
                if any(v not in spec['items']['enum'] for v in value):errors.append(key+': invalid array item')
            elif spec.get('items',{}).get('type')=='string':
                if any(not isinstance(v,str) for v in value):errors.append(key+': non-string item')
    if name=='artifact' and isinstance(record.get('path'),str):
        p=record['path']
        if p.startswith('/') or '\\' in p or '..' in p.split('/') or '://' in p or not p.strip():errors.append('path: unsafe/non-relative')
    if name=='action-approval':
        # Spending always demands an explicit cap; no automatic publish on a JSON parse.
        if record.get('action')=='spend' and 'budget_limit_eur' not in record:errors.append('spend needs budget_limit_eur')
        if record.get('execution_status')=='confirmed' and not record.get('execution_external_id'):errors.append('confirmed needs external id')
    if name=='review' and record.get('status')=='pass':
        if not record.get('evidence_refs') and not any(f.get('evidence_ref') for f in record.get('findings',[]) if isinstance(f,dict)):
            errors.append('pass needs evidence reference')
    if errors:raise CheckError('; '.join(errors))
    return True

def main():
    parser=argparse.ArgumentParser();parser.add_argument('contract',choices=SCHEMA_NAMES);parser.add_argument('json_file',type=Path);args=parser.parse_args()
    try:
        check(args.contract,json.loads(args.json_file.read_text(encoding='utf8')))
        print('STRUCTURAL_PREFLIGHT_OK (no compliance certification)')
    except (CheckError,OSError,ValueError,json.JSONDecodeError) as e:
        print('PREFLIGHT_BLOCKED:',str(e),file=sys.stderr);return 2
    return 0
if __name__=='__main__':sys.exit(main())
