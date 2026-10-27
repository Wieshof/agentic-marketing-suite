#!/usr/bin/env python3
"""Offline static help package checks. NOT a full JSON Schema / harness validator."""
import argparse,json,re,sys
from pathlib import Path

def validate(root):
    root=Path(root).resolve()
    h=root/'help'; base=h/'.help'
    issues=[];stats={}
    essentials=[h/'AGENT.md',base/'METHODEN.md',base/'WISSENSQUELLEN.md',base/'BERATUNG.md',base/'RULES.md',base/'TESTFAELLE.md']
    for p in essentials:
        if not p.is_file(): issues.append(f'Pflichtdatei fehlt: {p}')
    methods=list((base/'methoden').rglob('*.md'))
    stats['method_files']=len(methods)
    for m in methods:
        s=m.read_text(encoding='utf-8')
        for section in ['## Zweck','## Wann einsetzen','## Vorgehen','## Ergebnis','## Qualitätskontrolle','## Zusammenarbeit']:
            if section not in s: issues.append(f'{m.relative_to(root)}: fehlend {section}')
    for index in [base/'METHODEN.md',base/'ANLEITUNGEN.md']:
        if not index.exists(): continue
        s=index.read_text(encoding='utf-8')
        for link in re.findall(r'\[[^]]+\]\(([^)]+)\)',s):
            if link.startswith(('http:','https:','#')): continue
            if not (index.parent/link).is_file(): issues.append(f'{index.relative_to(root)}: Linkziel fehlt {link}')
    for p in (base/'schemas').glob('*.json'):
        try:
            schema=json.loads(p.read_text(encoding='utf-8'))
            assert schema.get('type')=='object'
        except Exception as ex: issues.append(f'JSON-Schema beschädigt: {p.name}: {ex}')
    for p in (base/'examples').glob('*.json'):
        try: assert json.loads(p.read_text(encoding='utf-8')).get('schema_version')=='0.1'
        except Exception as ex: issues.append(f'Beispiel-JSON ungültig: {p.name}: {ex}')
    stats['guide_files']=len(list((base/'guides').rglob('*.md')))
    stats['issues']=issues
    stats['ok']=not issues
    return stats

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',default='.')
    args=p.parse_args();result=validate(args.root)
    print(json.dumps(result,ensure_ascii=False,indent=2))
    sys.exit(0 if result['ok'] else 1)
