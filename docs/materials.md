# 公共材料与当前状态

## 数据边界

- `game/game.sqlite3` 与 `game/sources/public-baseline.sql` 同步发布；等级观察 JSON 是数据库的确定性导出。
- 主表正文是历史来源展示，不是任意红度的通用满级效果。查询以 `tactic_level_observations` 中对应等级、红度、平台、赛季、场景和有效核定为准。红度未知不当零，无匹配返回需要确认并列出现有观察。
- `review_state` 区分 `unreviewed/reviewed/superseded/retracted`。`superseded_by` 指向同技能的新观察，禁止自环和循环；已撤回/被替代观察不参加可信查询。自动分类不覆盖已核决定。
- `verified_fields` 表示本条证据认证的字段，`observation_scope` 区分 `event_native/support/owned/unspecified`。没有来源依据的场景保留 unspecified，不从日期猜填。`screenshot_verified_fields` 仍保留主表历史核定边界。
- `game/facts.json` 是单独机制事实的公共入口。每条有字段、对象、来源、核定日期、平台、赛季、状态。用户确认MD可认证对应机制，但不是整项技能完整10级认证，也不是账号拥有证明。
- `evidence_id=sha256:<内容哈希>` 标识证据内容；路径可不同。索引保存观察及实体字段关联、`event_refs=账号/期次`。已有原图哈希不符直接报错；历史已清理材料标 historical_missing。用户指定不入版本库的图片标 `local_only`：本机仍核哈希，远端缺少文件可接受，后续索引刷新保留此状态；不伪造图片，也不自动推翻保留的核定转写。

本地图片证据要随文字数据发布时，在同目录或对应事件目录保存转译Markdown，并在索引/清单写 `transcription_ref`、`transcription_status=verified_text`、`transcription_marker`、`trust_status`、`trust_reason` 和非空 `verified_fields`。文内锚点使用 `image-<SHA256>`，并写标记 `<!-- IMAGE_TEXT_TRANSCRIPTION_V1:sha256:<SHA256> -->`；校验器核对引用、锚点及标记。标记用于可核查地绑定文字记录与原图内容身份，不是数字签名或准确性证明；可信度仍由逐字段复核和 `trust_status/trust_reason` 决定。原始 PNG/JPG/WebP 在本机保留并忽略 Git，不将二进制截图加入提交。

## 当前与历史

已迁移期次的 `current_state.json` 是仓库、支援、最新装备、当前建议及锁定状态的唯一编辑来源。`当前仓库.json` 和 `当前状态.md` 自动生成，只读。`event.json` 保存期次元数据、公共证据索引及规则；`decision_history.json` 追加历史状态和被撤回的建议。旧截图对应的阵容快照不改成当前配置。

未知锁定用 null；“截图证实清风装备”不等于“截图展示清风援标”，支援来源推定文字必须保留。此前郭嘉重随、支援水淹等未执行或已变更建议只保留历史。

续战按轮次、对手、队伍合并为一组结果，不再按每张详情图计场。`final_result` 保存实见结果，`assessment` 保存胜负倾向；预计胜负不得回写实见结果。8回合后续战保留兵力存活、重置增减buff。异常状态次数不等于独立受控回合。

## 命令

公共材料维护使用 Python 3.11+（SQLite serialize 支持）；导入图片额外需要 Pillow。普通库存/离线重建仍可用 Python 3.10+ 标准库。所有材料入口必须显式用户和期次，不能写个人 inventory.json。

```powershell
python scripts/materials.py query --user bixianjue --event s2-2026-09-23 --name 断敌粮道 --advancement 1
python scripts/materials.py validate --user bixianjue --event s2-2026-09-23
python scripts/materials.py import --user bixianjue --event s2-2026-09-23 --input incoming-review.json
```

写入命令默认只预演；核对 `changed_files` 后同命令加 `--apply`。材料入库必须先人工对图逐字段确认，CLI不执行OCR或自动判真。现阶段导入已有公共战法的完整等级观察；新增实体、武将四维需先单独审核定义，不能塞进战法观察，也不能把战斗buff属性当基础四维。

导入格式（示意，不可将示意正文当事实导入）：

```json
{
  "user_id": "明确账号",
  "event_id": "明确期次",
  "observations": [{
    "name": "已存在的战法名称",
    "image": "项目内相对路径或本机绝对路径.png",
    "observed_at": "2026-09-24",
    "platform": "Steam",
    "season": "s2",
    "level": 10,
    "advancement": null,
    "scope": "unspecified",
    "effect_raw": "人工核定的完整正文",
    "activation_rate": "100%",
    "verified_fields": ["effect_raw", "level", "activation_rate"],
    "reviewed": true,
    "trust_reason": "具体核定依据与边界",
    "supersedes": []
  }]
}
```

明确红度时填0至5并在 verified_fields 增加 advancement_confirmed；未核发动率填 null，不在 verified_fields 声称核定。`supersedes` 填明确被替代的旧观察ID。同证据同上下文重复导入不新增观察；冲突转写拒绝覆盖，需要独立证据和明确替代关系。主表不会因这次导入自动把整个武将/战法升可信。

当前状态更新用 `materials.py state`，输入 `{expected_revision, reason, state}`；state为完整当前状态，必须保留证据和不确定性。旧修订自动追加历史，版本不符拒绝覆盖。更新后先 dry-run，再 --apply。图像文件本身只复制，不修改原始输入。

## 事务与恢复

发布前保存旧文件和新内容到 `notes/backups/<时间>-materials-<ID>/`，`transaction.json` 记录前后哈希。SQLite、SQL、观察、公共索引、事件索引和状态以一组日志发布，写后交叉验收失败自动回滚。多文件替换不是操作系统级原子事务；其他读取进程应在发布结束后读取。进程崩溃时系统文件锁自动释放，残留 publishing 日志会阻止下一次发布。

恢复先检查所有当前文件均匹配旧值或本次新值，发现后续用户编辑则拒绝覆盖。新建文件回滚时移入备份里的 rolled-back-new，保留资料，不销毁。

```powershell
python scripts/materials.py recover --user bixianjue --event s2-2026-09-23 --journal notes/backups/具体事务目录
```

检查预演后加 `--apply`。不要删除 `.materials.lock` 来绕过运行中的事务；它是持久锁文件，存在不代表仍被占用。

首次结构修复配方在 `materials-migration.json`。`migrate --input docs/materials-migration.json` 默认预演；已应用配方记录哈希，重复执行不重新覆盖当前状态。18个日期脚本改为明确报错的停用入口，完整原代码保留 `scripts/archive/*.py.txt`，不可重放旧脚本覆盖新核定。

## 验收

```powershell
python -m unittest discover -s tests -v
python scripts/verify_project.py
```

验收覆盖SQL一致性、观察导出、替代关系、证据哈希、事件索引、状态投影及续战去重。链接检查排除备份、原任务记录和历史归档，只检查活跃文档；备份原文里的旧相对路径不当作活跃断链。
