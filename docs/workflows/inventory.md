# 更新库存

1. 用户没有明确目标账号时，先问“本次更新 bixianjue 还是 zhaoguohua 的库存？”。在答复之前不读取任何账号库存或写文件。用户在同一连续任务已明确账号时不重复询问。
2. 声明“本次更新用户：xxx”。只读取该用户 `profile.json`、`inventory.json` 和本次图片。不得加载演武文档、外部模板、其他用户或历史综合交接文档。
3. 按名称和版本匹配武将，按名称匹配战法。必要时通过公共库定向查询；截图不清晰的字段询问用户，不猜填。
4. 将本次图片和部分更新 JSON 放入该用户 `evidence/incoming/`，通过 `--images` 传入本次整批图片。只提供本次明确的字段；省略字段沿用原值，明确的 `null` 才表示未知。未出现在图片中的已有条目保留。
5. 执行增量更新并校验、生成报告。成功后 `evidence/current/` 只保留最新一批截图和清单，替换旧批次并删除本次 incoming 临时输入；不再生成历史库存快照。失败时保留原库存和原截图。只在用户明确要求完整替换时加 `--replace`；完整替换必须同时提供两类列表。

```powershell
python scripts/account_inventory.py --user bixianjue update --input user/bixianjue/evidence/incoming/update.json --images user/bixianjue/evidence/incoming/01.png user/bixianjue/evidence/incoming/02.png
python scripts/account_inventory.py --user bixianjue validate
python scripts/account_inventory.py --user bixianjue report
```

命令中的账号必须替换为本任务用户明确指定的账号，示例不构成默认值。

```json
{"user_id":"bixianjue","verified_at":"2026-09-10","source":"本次用户截图","generals":[{"name":"小乔","variant":"普通","advancement":2}]}
```

只统计金将和金紫战法，范围外条目不进入当前库存。公共定义尚未收录的名字可以连同明确品质作为待补录条目保留，不能伪造实体 ID。`validate` 显式报告未解析项；待补录完成前不用于自动配将。

文字更新不带 `--images`，保留现有最新截图。截图使用内容哈希命名，避免旧来源路径错误指向新图片；结构化数据继续保留来源描述和核定日期。脚本只清理指定用户的库存截图和 incoming 输入，不删除外部传入文件、其他用户、演武战报或公共证据。不得将仍承担公共数值证据的图片放入会轮换的库存截图目录。

禁止直接运行历史日期脚本；不要用演武仓库、个人报告或旧数据库回填当前库存。
