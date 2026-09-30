# 常规配将

明确用户后，只读该账号当前资料、库存与当前赛季相关参考；缺少用户或赛季时先澄清。

```powershell
python scripts/account_inventory.py --user bixianjue candidates
python scripts/task_context.py --task formations --user bixianjue --season s3
python scripts/account_inventory.py --user bixianjue candidates --season s3
```

候选入口遵守全局品质范围，常规配将只取常驻普通武将。首发 S1 不表示 S2 不可用；未知适用范围标为待核，不擅自排除或宣称可用。不得使用公共库全量名单当作已有库存。

账号当前赛季以 `profile.json.current_season` 为准；计划转季保存在 `planned_season_transition`，即使计划日期已到也不自动当成实际完成。明确为下赛季预配时用 `--season`，查询会标 `mode=planning`，不写账号或库存。实际进入后根据用户确认更新当前赛季，并移除已完成的计划。

`inventory.json.season` 是库存来源赛季，不能跟随账号赛季改写。返回的 `context` 标明账号赛季、查询赛季、库存来源赛季及批次核定日期；仍保留逐条证据日期，不把旧持有记录当新赛季已核库存。机制事实与数值观察只取对应平台、赛季的可信记录，缺少本季证据时按需核定，不自动继承旧季可信度。

参考模板放在 `references/<赛季>/`；当前已有 S1/S2，S3 尚未提供。任务入口遇到缺失参考会返回 `reference_status=missing`，不返回不存在的文件，也不自动以 S2 替代 S3。旧模板可作明确标注的历史参考，不能认证新季适用性。个性化方案写入指定用户 `formations/`。方案不改变库存；需要演武配队时改走演武入口。
