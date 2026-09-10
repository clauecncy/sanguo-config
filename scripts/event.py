"""Read one explicitly identified user's event; never guess the current event."""
import argparse
import json
from project_data import event_dir, read_json

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--user',required=True)
    p.add_argument('--event',required=True)
    args=p.parse_args()
    try:
        path=event_dir(args.user,args.event)
        print(json.dumps({'event':read_json(path/'event.json'),'files':[x.relative_to(path).as_posix() for x in path.rglob('*') if x.is_file()]},ensure_ascii=False,indent=2))
    except (ValueError,OSError) as e: p.exit(1,str(e)+'\n')

if __name__=='__main__': main()
