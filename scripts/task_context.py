"""Return a small task reading list; missing identities require conversation."""
import argparse
import json
from project_data import ROOT, event_dir, read_json, user_dir

def route(task, user=None, event=None, root=ROOT):
    if not user:
        return {'status':'ask_user','question':'本次更新 bixianjue 还是 zhaoguohua 的库存？' if task=='inventory' else '本次操作哪个用户？','files':[]}
    base=user_dir(user,root)
    prefix=base.relative_to(root).as_posix()
    if task=='inventory':
        return {'status':'ready','user_id':user,'announcement':f'本次更新用户：{user}',
                'files':['docs/workflows/inventory.md',prefix+'/profile.json',prefix+'/inventory.json'],
                'additional':'仅本次图片；歧义时定向读取有关公共定义或个人证据'}
    if task=='events':
        if not event:
            return {'status':'ask_user','question':'请明确本次演武期次。','files':[prefix+'/演武/index.json']}
        path=event_dir(user,event,root)
        return {'status':'ready','files':['docs/workflows/events.md',path.relative_to(root).as_posix()+'/event.json'],
                'additional':'仅读取本期与问题有关的记录；支援核对才读常规库存'}
    season=read_json(base/'profile.json')['current_season']
    return {'status':'ready','files':['docs/workflows/formations.md',prefix+'/profile.json',prefix+'/inventory.json',f'references/{season}/README.md']}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--task',choices=['inventory','formations','events'],required=True)
    p.add_argument('--user')
    p.add_argument('--event')
    args=p.parse_args()
    try: print(json.dumps(route(args.task,args.user,args.event),ensure_ascii=False,indent=2))
    except (ValueError,OSError) as e: p.exit(1,str(e)+'\n')

if __name__=='__main__': main()
