#!/usr/bin/env python3
"""Offline formal checks for branding records. No network or writes."""
import argparse, json, sys
from pathlib import Path
from datetime import datetime
KINDS={'brand-profile','brand-decision','brand-context-request','brand-context-pack','brand-review','brand-event'}
REQUIRED={
'brand-profile':{'brand_id','name','version','status','updated_at','owner_scope','visibility','brand_platform','source_refs','limitations'},
'brand-decision':{'decision_id','brand_id','topic','statement','status','version','updated_at','source_refs','impact_areas'},
'brand-context-request':{'request_id','requester','purpose','audience','topics'},
'brand-context-pack':{'request_id','requester','purpose','audience','generated_at','profiles','excluded_count','limitations'},
'brand-review':{'review_id','brand_id','artifact_id','artifact_version','reviewed_at','status','findings'},
'brand-event':{'event_id','brand_id','occurred_at','kind','actor','artifact_ref','summary'}
}
VALID_STATUS={'draft','in_review','approved','rejected','superseded','retired'}
VIS={'public','shared','restricted'}
def stamp(s):
 try: return isinstance(s,str) and datetime.fromisoformat(s.replace('Z','+00:00')).tzinfo is not None
 except (ValueError,TypeError): return False

def lint(obj,kind):
 errors=[]
 if kind not in KINDS:return ['unknown kind']
 if not isinstance(obj,dict):return ['object expected']
 missing=REQUIRED[kind]-set(obj)
 if missing:errors.append('missing: '+', '.join(sorted(missing)))
 for k in (('version','artifact_version') if kind in ('brand-profile','brand-decision','brand-review') else ()):
  if k in obj and (not isinstance(obj[k],int) or isinstance(obj[k],bool) or obj[k]<1):errors.append(k+' must be positive integer')
 for k in ('updated_at','approved_at','occurred_at','reviewed_at','generated_at'):
  if k in obj and not stamp(obj[k]):errors.append(k+' must be offset-aware ISO timestamp')
 if kind in ('brand-profile','brand-decision'):
  if obj.get('status') not in VALID_STATUS:errors.append('invalid lifecycle status')
  if obj.get('status')=='approved':
   for k in (('approved_by','approved_at','decision_ref') if kind=='brand-profile' else ('approved_by','approved_at')):
    if not obj.get(k):errors.append('approved requires '+k)
 if kind=='brand-profile' and obj.get('visibility') not in VIS:errors.append('invalid visibility')
 if kind=='brand-context-request' and obj.get('audience') not in VIS:errors.append('invalid audience')
 if kind=='brand-context-pack' and obj.get('audience') not in VIS:errors.append('invalid audience')
 if kind=='brand-context-pack' and (not isinstance(obj.get('excluded_count'),int) or isinstance(obj.get('excluded_count'),bool) or obj['excluded_count']<0):errors.append('invalid excluded_count')
 if kind=='brand-context-request' and not obj.get('topics'):errors.append('topics cannot be empty')
 if kind=='brand-profile' and not isinstance(obj.get('brand_platform'),dict):errors.append('brand_platform object expected')
 for k in ['source_refs','limitations','topics','findings','profiles']:
  if k in obj and not isinstance(obj[k],list):errors.append(k+' must be array')
 return errors

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--kind',choices=sorted(KINDS),required=True);ap.add_argument('file',type=Path);args=ap.parse_args()
 try:data=json.loads(args.file.read_text(encoding='utf-8'))
 except (ValueError,OSError) as ex:print('INVALID_JSON',ex,file=sys.stderr);return 2
 errors=lint(data,args.kind)
 if errors:
  print('INVALID',*errors,sep='\n- ',file=sys.stderr);return 1
 print('VALID',args.kind,args.file);return 0
if __name__=='__main__':sys.exit(main())
