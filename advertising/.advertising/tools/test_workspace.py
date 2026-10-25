#!/usr/bin/env python3
"""Offline tests for consistency and safety. No ad network is accessed."""
import json,re,sys,subprocess,os
from pathlib import Path
sysdir=Path(__file__).resolve().parents[1]
base=sysdir.parent
sys.path.insert(0,str(sysdir/'tools'))
from validate_manifest import check

def links_ok(p):
  broken=[]
  for href in re.findall(r'\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
    if href.startswith(('https://','http://','#','mailto:')):continue
    q=(p.parent/href.split('#')[0])
    if not q.exists():broken.append((p.name,href))
  return broken

errors=[]
for p in sysdir.rglob('*.md'):errors+=links_ok(p)
agent=(base/'AGENT.md').read_text()
if 'Wobei kann ich Ihnen bei Werbung und Kampagnen helfen?' not in agent:errors.append('Gesprächseröffnung fehlt')
for name in ('STATE.md','LOG.md','HISTORY.md','MEDIA_BUYING.md','RULES.md','ARCHITECTURE.md','METHODEN.md','KANAELE.md','FORMATE.md'):
 if not (sysdir/name).exists():errors.append(name+' fehlt')
allmethods=list((sysdir/'methoden').rglob('*.md'))
channels=list((sysdir/'kanaele').rglob('*.md'))
formats=list((sysdir/'formate').rglob('*.md'))
if len(allmethods)<70 or len(channels)<20 or len(formats)<14:errors.append('Bibliothek unvollständig')
for n,files,index in [('Methoden',allmethods,'METHODEN.md'),('Kanal',channels,'KANAELE.md'),('Formate',formats,'FORMATE.md')]:
 txt=(sysdir/index).read_text()
 for p in files:
  if p.name not in txt:errors.append(n+' ohne Index: '+str(p))
draft=json.loads((sysdir/'beispiele'/'DRAFT_MANIFEST_DEMO.json').read_text())
if check(draft):errors.append('sicherer Entwurf wird abgewiesen: '+str(check(draft)))
for action in ['activate','stage_paused','update','pause']:
 case=json.loads(json.dumps(draft));case['action']=action
 if not check(case):errors.append('unsicherer '+action+' Request wurde akzeptiert')
case=json.loads(json.dumps(draft));case['budget']['daily_max']='1000';case['budget']['lifetime_max']='1'
if not check(case):errors.append('Budgetrelation wurde nicht kontrolliert')
print('Methods',len(allmethods),'Channels',len(channels),'Formats',len(formats))
if errors:
 for e in errors:print('FAIL:',e)
 sys.exit(2)
print('PASS — links, library indexes, start behavior, manifest draft and blocked actions')
