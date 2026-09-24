"""Read one explicitly identified user's event; never guess the current event."""
import argparse
import json
from project_data import event_dir, read_json
from event_state import read_current

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--user',required=True)
    p.add_argument('--event',required=True)
    args=p.parse_args()
    try:
        path=event_dir(args.user,args.event)
        data=read_json(path/'event.json')
        current=read_current(path)
        print(json.dumps({'event':data,'current_state':current,'files':data.get('files',[]),
                          'history_policy':'历史记录按需读取，不作为当前建议'},ensure_ascii=False,indent=2))
    except (ValueError,OSError) as e: p.exit(1,str(e)+'\n')

if __name__=='__main__': main()
