"""Read-only acceptance checks for layout, catalogs, identities and migration."""
import hashlib
import argparse
import json
from pathlib import Path
import re
from urllib.parse import unquote
from project_data import ROOT, read_json, public_connection, load_inventory, query
from sync_game_data import validate_public

def verify(root=ROOT, migration=False):
    manifest=read_json(root/'docs/migration-manifest.json')
    with public_connection(root) as c:
        validate_public(c)
    result={}
    for user in ['bixianjue','zhaoguohua']:
        current=load_inventory(user,root)
        if migration:
            baseline=manifest.get('inventory_baseline',{}).get(user)
            if baseline:
                if hashlib.sha256((root/f'user/{user}/inventory.json').read_bytes()).hexdigest()!=baseline['sha256']:
                    raise AssertionError(f'Inventory differs from verified migration baseline: {user}')
            else:
                original=read_json(root/f'user/{user}/snapshots/pre-migration-inventory.json')
                for group in ['generals','tactics']:
                    omitted=[r['record'] for r in manifest['excluded'][user] if r['group']==group]
                    expected=[r for r in original[group] if r not in omitted]
                    if len(expected)!=len(current[group]): raise AssertionError(f'{user}/{group} count changed')
                    for before,after in zip(expected,current[group]):
                        if any(after.get(k)!=v for k,v in before.items()): raise AssertionError(f'Field loss: {user}/{before["name"]}')
        with query(user,root) as c:
            for group in ['generals','tactics']:
                assert c.execute(f'SELECT count(*) FROM v_owned_{group}').fetchone()[0]==len(current[group])
            if migration and user=='bixianjue':
                assert c.execute("SELECT force FROM v_owned_generals WHERE variant='英雄'").fetchone()[0] is None
        result[user]={g:len(current[g]) for g in ['generals','tactics']}
    for row in (manifest['files'] if migration else []):
        if row.get('removed_after_verification'): continue
        p=root/row['new']
        if not p.is_file(): raise AssertionError('Lost migration file: '+row['new'])
        if hashlib.sha256(p.read_bytes()).hexdigest()!=row.get('post_cleanup_sha256',row['migrated_sha256']):
            raise AssertionError('Migration hash mismatch: '+row['new'])
    broken=[]
    # Original task prose is immutable, and resolves via migration-manifest.json.
    for p in root.rglob('*.md'):
        if any(part in ['.git','__pycache__','.ocr-python'] or part.startswith('tmp') for part in p.parts): continue
        if any(p.is_relative_to(root/x) for x in ('notes/tasks','notes/backups','notes/history')): continue
        for raw in re.findall(r'\]\(([^)\n]+)\)',p.read_text(encoding='utf-8-sig')):
            if raw.startswith(('http:','https:','mailto:','#','app:')): continue
            target=unquote(raw.split('#')[0].strip('<>'))
            if target and not (p.parent/target).exists(): broken.append([str(p.relative_to(root)),raw])
    if broken: raise AssertionError('Broken links: '+json.dumps(broken,ensure_ascii=False))
    result['migration_files']=len(manifest['files'])
    result['missing_original_assets']=len(manifest.get('missing_original_assets',[]))
    result['cleaned_materials']=manifest.get('retention_cleanup',{}).get('removed_count',0)
    result['public_integrity']='ok'
    from validate_materials import verify_materials
    result['materials'] = verify_materials(root)
    if migration: result['migration_fields']='unchanged except documented quality exclusions and added IDs'
    return result

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--migration',action='store_true',help='Verify original migration baseline, not subsequent inventory updates')
    args=parser.parse_args()
    print(json.dumps(verify(migration=args.migration),ensure_ascii=False,indent=2))
