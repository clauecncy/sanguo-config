# zhaoguohua

- 用户于 2026-09-30 确认当前已进入 S2；库存仍是 S1 来源记录，后续按需增量更新，不因转季清空或假定新增。
- [最近记录的演武：S1 2026-09-16](演武/s1-2026-09-16/event.json) 保留原赛季，不改名为 S2，不默认视为当前新一期。
- 当前账号资料：profile.json；唯一库存来源：inventory.json。
- [库存操作](../../docs/workflows/inventory.md)；写入必须明确此用户。
- [库存报告](reports/库存.md)、[演武期次](演武/index.json)。
- formations/ 为个性化常规配队，evidence/current/ 只保留最新成功更新的库存截图；不再保存多个库存版本。

更新库存时不需要读取演武、历史快照或另一个账号。
