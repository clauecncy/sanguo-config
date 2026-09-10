"""Compatibility CLI: validation requires an explicit user."""
import argparse
import json
from project_data import summary

if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--user',required=True)
    a=p.parse_args()
    try:
        d=summary(a.user)
        print(json.dumps({'user_id':a.user,'counts':d['counts'],'unresolved':d['unresolved']},ensure_ascii=False))
    except (ValueError,OSError) as e: p.exit(1,str(e)+'\n')
