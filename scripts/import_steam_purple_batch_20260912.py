import hashlib,json,os,shutil,sqlite3
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; DB=ROOT/'game/game.sqlite3'; STAGED=ROOT/'game/game.staged.sqlite3'
E=ROOT/'game/sources/screenshots/2026-09-12'; I=ROOT/'game/sources/evidence-index.json'; O=ROOT/'game/sources/tactic_level_observations.json'
TMP=Path(r'C:\Users\BIXIAN~1\AppData\Local\Temp'); NOW='2026-09-12T00:00:00+08:00'
ROWS='''咏歌尝酒|主动|治疗|65%|恢复我军随机两人兵力（治疗率145.6%，受智力影响），并提升其17.92点统率，持续2回合|36784e47-f2c4-4739-af1e-7de7188a6cb5
决水破敌|主动|谋略|60%|对敌军随机两人造成109%谋略伤害，若目标处于洪水状态，则额外造成65.4%谋略伤害；否则施加洪水，持续2回合|bea575c1-9fb2-4b13-829a-45ea1f462ed1
束手无策|主动|谋略|45%|对敌军随机单体造成218%谋略伤害，并施加技穷，持续1回合|81d78cc6-33c4-4ec3-81a4-c565596c2994
铸甲销戈|指挥|防御|100%|战斗开始前3回合，我军全体在回合开始时有70.85%概率获得1层抵御|7c81ed4a-66c7-4202-bf7f-21d28062b7d3
骁勇之姿|被动|辅助|100%|自身连击率提升65.4%，造成伤害提升10.9%|25f3adbd-5f41-437f-af68-c8cd39413416
任人唯贤|主动|辅助|60%|提升我军随机两人16.35%造成伤害、27.25点统率，持续2回合|fd3c44ca-9037-40c8-b3ad-005000b7f743
避其锐气|指挥|防御|100%|战斗开始前4回合，自身及随机友军单体受到伤害减少27.56%|013fbbec-bc86-4f40-b286-61cc3c55d9db
如有神助|被动|辅助|100%|主动战法发动率提升8.48%，主动战法伤害提升15.9%|dcd1ad77-2c86-4e35-8d66-6aec5ea18542
坚壁清野|主动|防御|50%|嘲讽敌军全体，并提升自身40.32点统率，持续2回合|82497a96-808d-4a41-aa35-0ffba7e2792e
火羽|主动|兵刃|40%|对敌军全体造成168%兵刃伤害，并施加火攻，持续2回合|22e46733-0bcb-4b0d-8974-5a3c69f02578
上兵伐谋|指挥|谋略|100%|回合开始时，对敌军随机单体造成134.4%谋略伤害；上兵伐谋伤害会随回合数增加，每回合提升伤害10%|be629d52-1ed0-4a67-b06d-c6b9d6709641
一计决胜|主动|谋略|35%|准备1回合，对敌军随机两人造成239.8%谋略伤害，并施加虚弱状态，持续2回合；若目标已持有虚弱状态，则额外造成54.5%谋略伤害|303b49c6-4429-4db5-ab8a-5f99013fce87
奇计迭出|追击|谋略|40%|普通攻击后，对敌军随机单体造成287.5%谋略伤害，优先选择敌军后排|e946894f-da74-4dd1-8048-816fdd84c277
以战养战|被动|治疗|100%|武力提升23点；普通攻击后，恢复自身兵力（治疗率126.5%，受智力和武力影响）|05075b1f-96d4-463b-8567-40911ded9bb5
强袭|被动|兵刃|100%|普通攻击后，对敌军随机单体造成该次普通攻击92%的传递伤害|3bf01ec9-482f-4052-a731-2f580fb9da37
计逐穷寇|被动|谋略|100%|造成谋略伤害后，有67.2%概率对敌军随机单体造成1次普通攻击，每回合最多触发1次|6ad03219-c07e-4fe7-9e1c-48f7dd278279
乱敌方阵|追击|兵刃|35%|普通攻击后，对攻击目标造成246.4%兵刃伤害，并施加混乱，持续1回合|4da1c44e-e887-4290-9d6e-09c33d993913
克敌如风|主动|兵刃|50%|对敌军随机单体造成261.6%兵刃伤害（优先选择后排），并施加风暴，持续2回合；若目标已处于风暴状态，则额外降低其27.25点先攻，持续2回合|12b30cde-e34b-41d7-a7ee-d46ecc65e344
谈笑诛心|被动|谋略|100%|敌军被施加负面状态时，有60%概率对敌军随机单体造成119.9%谋略伤害，每回合最多触发2次|015f6e59-d17a-4dc1-a65a-4bf2b8fc01e2
夜袭|追击|兵刃|45%|普通攻击后，对敌军随机两人造成130.8%兵刃伤害；若自身先攻大于目标，则额外造成54.5%兵刃伤害|1ee61d98-6214-4137-b878-bdfdaf38b185
筹划良策|主动|谋略|50%|提升自身21.8点智力，持续2回合；对敌军随机两人造成174.4%谋略伤害|ea22290e-2688-4ffc-a614-eae2f8736f9d
屈人之兵|主动|防御|40%|对敌军随机两人施加缴械，持续1回合；若目标已持有缴械，则使其造成伤害降低16.35%，持续2回合|4b0af31a-632c-4906-a40e-eb41db7d003e
穷追不舍|被动|兵刃|100%|每个回合行动时有60%概率对持有异常状态的敌军造成130.8%兵刃伤害，每个目标独立判定|15b1f1a8-5970-40bd-834c-27664a50ef05
临阵突袭|追击|兵刃|40%|普通攻击后，降低目标31.8点统率，持续2回合，然后对其造成265%兵刃伤害|f24e7e78-14f2-4a9e-84ed-2095d4750e30
疾行侧击|主动|兵刃|60%|对敌军随机单体造成159%兵刃伤害，并施加畏惧，持续2回合，触发2次|d0ccb90e-e9e6-4f47-bc98-a711b65a61cb
来好息师|被动|治疗|100%|每回合结束时，恢复我军前排全体兵力（治疗率95.4%，受智力影响）|b80aa2c7-2743-4cf5-bb51-f49065bf8e71
迎敌|主动|兵刃|50%|准备1回合，提升自身21.2%破甲，持续2回合，然后对敌军单体造成466.4%兵刃伤害，优先选择前排目标|0e55ef48-3bc7-4d27-a06c-9cd8cf0e28f2
揭竿而起|主动|兵刃|45%|对敌军随机两人造成159%兵刃伤害，并对目标施加断粮，持续1回合|8204ebfb-950c-4284-acb8-9d8db51a5a2c
文治武功|指挥|文武|100%|每个回合行动时有60%概率对敌军随机两人造成106%兵刃和谋略伤害|189e0103-7d39-405c-add7-8cb8d19aa572
如沐春风|被动|治疗|100%|每个回合行动时恢复自身兵力（治疗率148.4%，受智力和统率影响）|a297dfa3-c07e-477a-8d7e-df93dfef5724
临危勇烈|被动|兵刃|100%|自身反击率提升42.4%，受到普通攻击伤害降低21.2%|35c91f20-ab11-4c16-8370-5d6f5abfb541'''
HERO='''独断专权|被动|治疗|100%|自身统率提升40%（受统率影响），战斗中两名队友受到负面状态时，自身有30%概率（受统率影响）为其驱散1种随机负面状态，并恢复其兵力（治疗率100%，受智力和统率影响）|f1e03323-76c8-4b4d-9bba-03d3e39258c8
恃勇论锋|主动|兵刃|65%|对敌军随机单体（有75%概率选择统率最低目标）造成250%兵刃伤害，自身每有一个基础属性高于目标，兵刃系数提升80%，并恢复我军兵力最低单体兵力（治疗率180%，受武力影响）|c4740b01-f26e-47e5-a91f-13af06aef86d
江东虎威|追击|兵刃|55%|普通攻击后，降低敌军随机单体70点统率（受统率影响），持续2回合，并施加震慑，持续1回合|d154b089-c514-4683-af27-390f45332762'''
rows=[x.split('|',5) for x in (ROWS+'\n'+HERO).splitlines()]
def main():
 E.mkdir(parents=True,exist_ok=True)
 for n,*_,token in rows:
  src=TMP/f'codex-clipboard-{token}.png'; dst=E/f'{n}-10级.png'
  if not src.exists(): raise FileNotFoundError(src)
  shutil.copy2(src,dst)
 if STAGED.exists(): STAGED.unlink()
 shutil.copy2(DB,STAGED); c=sqlite3.connect(STAGED)
 try:
  c.execute('begin immediate'); existing={x[0] for x in c.execute('select name from tactics')}
  for n,typ,dmg,rate,desc,token in rows:
   if n not in existing:
    eid='tactic:'+hashlib.sha256(n.encode()).hexdigest()[:20]
    c.execute('insert into tactics(name,quality,is_self_tactic,first_season,verification_status,updated_at,description_level,platform,entity_id) values (?,?,?,?,?,?,?,?,?)',(n,'金' if n in {x.split('|',1)[0] for x in HERO.splitlines()} else '紫',int(n in {x.split('|',1)[0] for x in HERO.splitlines()}),'S2','待核',NOW,10,'Steam',eid))
   rel=f'game/sources/screenshots/2026-09-12/{n}-10级.png'; sn=f'Steam截图-{n}-10级-20260912'
   c.execute('delete from sources where name=?',(sn,)); sid=c.execute('insert into sources(name,url,source_type,platform,season,trust_rank,fetched_at,notes) values (?,?,?,?,?,?,?,?)',(sn,rel,'游戏内截图','Steam','S2',100,NOW,'用户提供；满级/满级预览截图')) .lastrowid
   c.execute('update tactics set tactic_type=?,damage_type=?,activation_rate=?,description_raw=?,description_level=10,verification_status=?,source_id=?,updated_at=?,platform=? where name=?',(typ,dmg,rate,desc,'Steam截图已核',sid,NOW,'Steam',n))
  c.commit()
 finally: c.close()
 index=json.loads(I.read_text(encoding='utf-8')); paths={x.get('path') for x in index}
 for n,*_ in rows:
  path=E/f'{n}-10级.png'; rel=path.relative_to(ROOT).as_posix()
  if rel not in paths: index.append({'path':rel,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'source_type':'游戏内截图','platform':'Steam','season':'S2','notes':f'{n} 10级满级效果，用户提供'})
 I.write_text(json.dumps(index,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 raw_obs=json.loads(O.read_text(encoding='utf-8')); container=raw_obs.get('observations',raw_obs) if isinstance(raw_obs,dict) else raw_obs
 names={x[0] for x in rows}; obs=[x for x in container if x.get('tactic_name',x.get('name')) not in names]
 for n,typ,dmg,rate,desc,_ in rows: obs.append({'name':n,'level':10,'quality':'金' if n in {x.split('|',1)[0] for x in HERO.splitlines()} else '紫','tactic_type':typ,'damage_type':dmg,'activation_rate':rate,'effect_raw':desc,'verification_status':'Steam截图已核','observed_at':'2026-09-12T00:00:00+08:00','source':{'name':f'Steam截图-{n}-10级-20260912','url':f'game/sources/screenshots/2026-09-12/{n}-10级.png'}})
 if isinstance(raw_obs,dict): raw_obs['observations']=obs
 else: raw_obs=obs
 O.write_text(json.dumps(raw_obs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 c=sqlite3.connect(STAGED)
 try: dump='\n'.join(c.iterdump())+'\n'
 finally: c.close()
 (ROOT/'game/sources/public-baseline.sql').write_text(dump,encoding='utf-8'); os.replace(STAGED,DB)
 print(json.dumps({'updated':len(rows)},ensure_ascii=False))
if __name__=='__main__': main()
