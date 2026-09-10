# 三国：谋定天下资料项目

| 任务 | 入口 |
| --- | --- |
| 更新个人库存 | [库存操作](docs/workflows/inventory.md)，先明确账号 |
| 常规配将 | [配将操作](docs/workflows/formations.md) |
| 某期演武 | [演武操作](docs/workflows/events.md)，明确账号和期次 |
| 公共游戏数据 | [公共数据操作](docs/workflows/game.md) |
| 项目维护与验收 | [数据规范](docs/data-model.md)、[迁移清单](docs/migration-manifest.json) |

- [公共游戏定义](game/README.md)：武将、战法、羁绊、阵营和规则。
- [参考配将](references/README.md)：按 S1/S2 分类，独立于账号库存。
- 账号：[bixianjue](user/bixianjue/README.md)、[zhaoguohua](user/zhaoguohua/README.md)。
- 库存只保留当前数据和最新一批截图；[资料保留规则](docs/retention.md)。

运行环境：Python 3.10+，日常库存与离线重建只需标准库。
