"""Explicit-user inventory query, partial update, validation and reports."""
import argparse
import json
from project_data import atomic_json, read_json, summary, candidates, update_inventory, user_dir

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--user',required=True,help='No default user; ask the user if unspecified.')
    p.add_argument('command',choices=['query','validate','report','update','candidates'])
    p.add_argument('--input',help='Partial JSON patch; omitted entities are retained.')
    p.add_argument('--replace',action='store_true',help='Full replacement ONLY when explicitly requested by user.')
    p.add_argument('--images',nargs='+',help='New screenshot batch; replace old inventory images only after successful validation.')
    args = p.parse_args()
    try:
        base = user_dir(args.user)
        if args.command == 'update':
            if not args.input: p.error('update requires --input')
            update_inventory(args.user,read_json(args.input),args.replace,images=args.images)
            from inventory_evidence import cleanup_incoming
            cleanup_incoming(base,[args.input,*(args.images or [])])
        elif args.input or args.replace or args.images:
            p.error('--input/--replace/--images only apply to update')
        data = summary(args.user)
        if args.command == 'report':
            lines = [f'# {args.user} 当前库存','', '唯一编辑来源：../inventory.json；报告为派生文件。', '',
                     f'金将记录 {data["counts"]["generals"]} 条（含英雄/限时记录）；金紫战法 {data["counts"]["tactics"]} 条。',
                     '', '## 武将', '', '| 名称 | 版本 | 状态 | 红度 | 等级 |', '| --- | --- | --- | --- | --- |']
            display = lambda value: '未知' if value is None else str(value)
            for r in data['generals']:
                lines.append('| '+' | '.join(display(r[k]) for k in ['name','variant','availability','advancement','level'])+' |')
            lines += ['', '## 战法', '', '| 名称 | 品质 | 红度 | 等级 | 满级详情 |', '| --- | --- | --- | --- | --- |']
            for r in data['tactics']:
                lines.append('| '+' | '.join(display(r[k]) for k in ['name','quality','advancement','level'])+' | '+('对应红度已核' if r['detail_status']=='可信' else '对应红度待核')+' |')
            base.joinpath('reports').mkdir(exist_ok=True)
            base.joinpath('reports/库存.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
            atomic_json(base/'reports/覆盖率.json',{'counts':data['counts'],'unresolved':data['unresolved'],
                         'known_max_level_details':sum(r['description_level']==10 for r in data['tactics'])})
        if args.command == 'candidates':
            data = candidates(args.user)
        print(json.dumps(data if args.command in ['query','candidates'] else
                         {'user_id':args.user,'counts':data['counts'],'unresolved':data['unresolved']},ensure_ascii=False,indent=2))
        return 0
    except (ValueError,KeyError,OSError) as exc:
        p.exit(1,str(exc)+'\n')

if __name__ == '__main__':
    raise SystemExit(main())
