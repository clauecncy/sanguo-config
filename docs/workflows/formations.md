# 常规配将

明确用户后，只读该账号当前资料、库存与当前赛季相关参考；缺少用户或赛季时先澄清。

```powershell
python scripts/account_inventory.py --user bixianjue candidates
```

候选入口遵守全局品质范围，常规配将只取常驻普通武将。首发 S1 不表示 S2 不可用；未知适用范围标为待核，不擅自排除或宣称可用。不得使用公共库全量名单当作已有库存。

参考模板放在 `references/s1/`、`references/s2/`；个性化方案写入指定用户 `formations/`。方案不改变库存；需要演武配队时改走演武入口。
