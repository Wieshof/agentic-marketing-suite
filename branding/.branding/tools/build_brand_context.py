#!/usr/bin/env python3
"""Selective, OFFLINE brand context builder. No messaging, auth or network calls."""
import argparse,json,sys
from datetime import datetime,timezone
from pathlib import Path
from lint_records import lint
RANK={'public':0,'shared':1,'restricted':2}
FIELDS={'positioning','promise','core','values','voice','visual_principles','target_groups'}
def build(request,profiles, *, now=None):
 errors=lint(request,'brand-context-request')
 if errors:raise ValueError('invalid request: '+ '; '.join(errors))
 topics=set(request['topics']); unknown=topics-FIELDS
 if unknown:raise ValueError('unknown topics: '+','.join(sorted(unknown)))
 selected=[]; excluded=0
 for p in profiles:
  errors=lint(p,'brand-profile')
  if errors:raise ValueError('invalid profile: '+'; '.join(errors))
  if request.get('brand_ids') and p['brand_id'] not in request['brand_ids']:continue
  if p['status']!='approved' or RANK[p['visibility']]>RANK[request['audience']]:
   excluded+=1;continue
  extracted={k:v for k,v in p['brand_platform'].items() if k in topics}
  if not extracted:continue
  selected.append({'brand_id':p['brand_id'],'name':p['name'],'version':p['version'],'status':p['status'], 'visibility':p['visibility'],'brand_platform':extracted,'source_refs':p.get('source_refs',[]),'decision_ref':p['decision_ref'],'limitations':p.get('limitations',[])})
 return {'request_id':request['request_id'],'requester':request['requester'],'purpose':request['purpose'],'audience':request['audience'],'generated_at':(now or datetime.now(timezone.utc)).isoformat(),'profiles':selected,'excluded_count':excluded,'limitations':['Nur freigegebene Brand Profiles; keine Unternehmensfakten-Verifikation, Rechte- oder Veröffentlichungsfreigabe.'],'version':'0.1'}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--request',type=Path,required=True);ap.add_argument('--profiles',type=Path,nargs='+',required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args()
 try:
  req=json.loads(a.request.read_text(encoding='utf-8'))
  ps=[json.loads(p.read_text(encoding='utf-8')) for p in a.profiles]
  result=build(req,ps)
  errors=lint(result,'brand-context-pack')
  if errors:raise ValueError('; '.join(errors))
  a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
 except (OSError,ValueError) as ex:print('ERROR',ex,file=sys.stderr);return 1
 print('CREATED',a.out,'profiles',len(result['profiles']),'excluded',result['excluded_count']);return 0
if __name__=='__main__':sys.exit(main())
