# 数据规范与维护

字段级核定、红度观察查询、证据标识和演武当前状态详见 [公共材料模型与命令](materials.md)。已迁移期次以 current_state.json 为当前编辑源，历史建议不能反向覆盖；等级观察为数值查询源，主表正文不再直接当任意红度满级值。

公共 SQLite 为公共定义的查询库，`game/sources/public-baseline.sql` 是其完整离线重建源；两者必须一起更新。个人库存唯一编辑来源为每个用户 `inventory.json`，报告为派生文件。

`config.json` 是全局品质范围，用户不能覆盖。武将用 `(name, variant)` 区分普通与英雄，公共引用使用稳定 `entity_id`；战法用 `name` 与稳定 ID。保留已有来源、核定时间、红度、等级、当前编队及未知值。

账号查询只在内存中建立 `v_owned_generals` 和 `v_owned_tactics`。公共文件中不含账号表，不复制公共数据库作为新的个人运行库。迁移验收后的旧库存和 SQLite 副本已清理，不再生成多个库存版本。

演武 `event.json` 明确所有者、赛季和首次记录日期；`start_date=null` 表示开赛日期未知。索引只导航，不作为用户确认当前期次的替代。

来源中的截图路径可以指向个人证据，不复制图片。`evidence-index.json` 记录迁移后的路径与校验值；历史来源中的旧路径由迁移清单映射。

维护校验：

```powershell
python scripts/verify_project.py
python -m unittest discover -s tests -v
```

仅在验收此次迁移时使用 `python scripts/verify_project.py --migration` 比较原始基线；后续用户正常更新库存后不再要求与迁移前库存相同。

迁移清单保留原文件的路径与 SHA-256，并标记验收后按用户要求清理的材料；库存基线以哈希校验，不依赖完整旧库存副本。库存截图只保留最新成功批次，详见 [资料保留规则](retention.md)。

对话规则只能约束按指引执行的代理，不能提供文件权限隔离；脚本的必填账号和用户路径校验是实际写入边界。
