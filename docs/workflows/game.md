# 公共游戏数据

公共库在 `game/game.sqlite3`，只存定义、规则和来源。个人库存不得写进公共库；配将建议放在参考层。

日常任务不需要联网同步。现有网页原始快照和战法观察保存在 `game/sources/`；离线完整重建使用不含账号数据的 `public-baseline.sql`：

```powershell
python scripts/sync_game_data.py --output game/rebuilt.sqlite3
```

默认输出为公共库，若基线与当前库不同则拒绝覆盖，先在独立输出中比较。重建会检查用户仍引用的实体，不能静默移除它们。停用的历史联网采集脚本已清理，当前入口只负责离线重建。

新增或修正公共数据时同时更新公共库、SQL 基线和来源索引，在独立库校验后替换；实体 `entity_id` 保持稳定。通过 `migration-conflicts.json` 可查看两份旧库冲突，主库值被保留，次库证据没有被当作已确认的新值。

`first_season` 表示首发；`applicable_seasons`、`platform` 表示有证据支持的适用范围。缺少依据时为 null；来源的赛季不等于实体只可用于该赛季。
