"""Offline public catalog rebuild. No network collection or personal writes."""
import argparse
import os
from pathlib import Path
import sqlite3
import tempfile
from project_data import ROOT, read_json, ClosingConnection

def validate_public(c):
    if c.execute('PRAGMA integrity_check').fetchone()[0] != 'ok': raise ValueError('Invalid database')
    if c.execute('PRAGMA foreign_key_check').fetchall(): raise ValueError('Foreign key errors')
    names = [r[0] for r in c.execute("SELECT name FROM sqlite_master WHERE type IN ('table','view')")]
    if any(n.startswith(('account_','v_owned_','owned_')) for n in names): raise ValueError('Public database contains personal tables/views')
    for group in ['generals','tactics']:
        if c.execute(f'SELECT count(*) FROM {group} WHERE entity_id IS NULL').fetchone()[0]: raise ValueError('Missing stable IDs')

def rebuild(output, root=ROOT):
    output = Path(output).resolve()
    if not output.is_relative_to((root/'game').resolve()): raise ValueError('Public output must stay inside game/')
    output.parent.mkdir(parents=True,exist_ok=True)
    fd,temp = tempfile.mkstemp(suffix='.tmp',dir=output.parent)
    os.close(fd)
    try:
        c=sqlite3.connect(temp)
        try:
            c.executescript((root/'game/sources/public-baseline.sql').read_text(encoding='utf-8'))
            validate_public(c)
            for path in (root/'user').glob('*/inventory.json'):
                for group in ['generals','tactics']:
                    for row in read_json(path)[group]:
                        eid=row.get('entity_id')
                        if eid and not c.execute(f'SELECT 1 FROM {group} WHERE entity_id=? AND name=?',(eid,row['name'])).fetchone():
                            raise ValueError(f'Rebuild would remove a referenced entity: {path.parent.name}/{row["name"]}')
            # A stale source must not overwrite a newer catalog silently.
            live=root/'game/game.sqlite3'
            if output == live.resolve() and live.exists():
                with sqlite3.connect(live.as_uri()+'?mode=ro',uri=True,factory=ClosingConnection) as old:
                    if list(old.iterdump()) != list(c.iterdump()):
                        raise ValueError('Baseline differs from current public catalog; rebuild to --output game/rebuilt.sqlite3 and reconcile sources first')
            c.commit()
        finally: c.close()
        os.replace(temp,output)
    finally:
        if os.path.exists(temp): os.unlink(temp)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path,default=ROOT/'game/game.sqlite3')
    args=p.parse_args()
    try:
        rebuild(args.output)
        print('Public catalog rebuilt; personal files unchanged.')
    except (ValueError,OSError,sqlite3.Error) as e: p.exit(1,str(e)+'\n')

if __name__=='__main__': main()
