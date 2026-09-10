BEGIN TRANSACTION;
CREATE TABLE bond_members (
  bond_id INTEGER NOT NULL REFERENCES bonds(id) ON DELETE CASCADE,
  general_id INTEGER NOT NULL REFERENCES generals(id) ON DELETE CASCADE,
  PRIMARY KEY (bond_id, general_id)
);
INSERT INTO "bond_members" VALUES(1,106);
INSERT INTO "bond_members" VALUES(1,66);
INSERT INTO "bond_members" VALUES(1,48);
INSERT INTO "bond_members" VALUES(1,72);
INSERT INTO "bond_members" VALUES(1,19);
INSERT INTO "bond_members" VALUES(1,10);
INSERT INTO "bond_members" VALUES(2,4);
INSERT INTO "bond_members" VALUES(2,44);
INSERT INTO "bond_members" VALUES(2,47);
INSERT INTO "bond_members" VALUES(2,43);
INSERT INTO "bond_members" VALUES(2,2);
INSERT INTO "bond_members" VALUES(3,42);
INSERT INTO "bond_members" VALUES(3,3);
INSERT INTO "bond_members" VALUES(3,33);
INSERT INTO "bond_members" VALUES(4,7);
INSERT INTO "bond_members" VALUES(4,6);
INSERT INTO "bond_members" VALUES(4,18);
INSERT INTO "bond_members" VALUES(4,8);
INSERT INTO "bond_members" VALUES(5,11);
INSERT INTO "bond_members" VALUES(5,7);
INSERT INTO "bond_members" VALUES(5,45);
INSERT INTO "bond_members" VALUES(6,7);
INSERT INTO "bond_members" VALUES(6,45);
INSERT INTO "bond_members" VALUES(6,104);
INSERT INTO "bond_members" VALUES(6,87);
INSERT INTO "bond_members" VALUES(6,100);
INSERT INTO "bond_members" VALUES(7,52);
INSERT INTO "bond_members" VALUES(7,81);
INSERT INTO "bond_members" VALUES(7,9);
INSERT INTO "bond_members" VALUES(8,24);
INSERT INTO "bond_members" VALUES(8,66);
INSERT INTO "bond_members" VALUES(8,10);
INSERT INTO "bond_members" VALUES(9,11);
INSERT INTO "bond_members" VALUES(9,28);
INSERT INTO "bond_members" VALUES(10,52);
INSERT INTO "bond_members" VALUES(10,11);
INSERT INTO "bond_members" VALUES(10,29);
INSERT INTO "bond_members" VALUES(11,75);
INSERT INTO "bond_members" VALUES(11,16);
INSERT INTO "bond_members" VALUES(11,58);
INSERT INTO "bond_members" VALUES(11,13);
INSERT INTO "bond_members" VALUES(12,14);
INSERT INTO "bond_members" VALUES(12,50);
INSERT INTO "bond_members" VALUES(13,14);
INSERT INTO "bond_members" VALUES(13,52);
INSERT INTO "bond_members" VALUES(14,82);
INSERT INTO "bond_members" VALUES(14,20);
INSERT INTO "bond_members" VALUES(14,15);
INSERT INTO "bond_members" VALUES(14,83);
INSERT INTO "bond_members" VALUES(15,16);
INSERT INTO "bond_members" VALUES(15,43);
INSERT INTO "bond_members" VALUES(15,94);
INSERT INTO "bond_members" VALUES(16,16);
INSERT INTO "bond_members" VALUES(16,85);
INSERT INTO "bond_members" VALUES(17,20);
INSERT INTO "bond_members" VALUES(17,103);
INSERT INTO "bond_members" VALUES(17,17);
INSERT INTO "bond_members" VALUES(17,93);
INSERT INTO "bond_members" VALUES(18,17);
INSERT INTO "bond_members" VALUES(18,103);
INSERT INTO "bond_members" VALUES(19,29);
INSERT INTO "bond_members" VALUES(19,66);
INSERT INTO "bond_members" VALUES(19,19);
INSERT INTO "bond_members" VALUES(20,20);
INSERT INTO "bond_members" VALUES(20,32);
INSERT INTO "bond_members" VALUES(21,20);
INSERT INTO "bond_members" VALUES(21,106);
INSERT INTO "bond_members" VALUES(22,21);
INSERT INTO "bond_members" VALUES(22,22);
INSERT INTO "bond_members" VALUES(22,51);
INSERT INTO "bond_members" VALUES(23,32);
INSERT INTO "bond_members" VALUES(23,23);
INSERT INTO "bond_members" VALUES(23,59);
INSERT INTO "bond_members" VALUES(24,30);
INSERT INTO "bond_members" VALUES(24,23);
INSERT INTO "bond_members" VALUES(25,24);
INSERT INTO "bond_members" VALUES(25,30);
INSERT INTO "bond_members" VALUES(26,82);
INSERT INTO "bond_members" VALUES(26,25);
INSERT INTO "bond_members" VALUES(26,83);
INSERT INTO "bond_members" VALUES(27,26);
INSERT INTO "bond_members" VALUES(27,30);
INSERT INTO "bond_members" VALUES(27,29);
INSERT INTO "bond_members" VALUES(27,28);
INSERT INTO "bond_members" VALUES(27,27);
INSERT INTO "bond_members" VALUES(28,31);
INSERT INTO "bond_members" VALUES(28,70);
INSERT INTO "bond_members" VALUES(28,56);
INSERT INTO "bond_members" VALUES(29,82);
INSERT INTO "bond_members" VALUES(29,46);
INSERT INTO "bond_members" VALUES(29,35);
INSERT INTO "bond_members" VALUES(29,60);
INSERT INTO "bond_members" VALUES(30,42);
INSERT INTO "bond_members" VALUES(30,37);
INSERT INTO "bond_members" VALUES(30,41);
INSERT INTO "bond_members" VALUES(30,36);
INSERT INTO "bond_members" VALUES(31,42);
INSERT INTO "bond_members" VALUES(31,36);
INSERT INTO "bond_members" VALUES(32,33);
INSERT INTO "bond_members" VALUES(32,36);
INSERT INTO "bond_members" VALUES(33,63);
INSERT INTO "bond_members" VALUES(33,59);
INSERT INTO "bond_members" VALUES(33,23);
INSERT INTO "bond_members" VALUES(33,64);
INSERT INTO "bond_members" VALUES(33,38);
INSERT INTO "bond_members" VALUES(34,38);
INSERT INTO "bond_members" VALUES(34,15);
INSERT INTO "bond_members" VALUES(35,39);
INSERT INTO "bond_members" VALUES(35,93);
INSERT INTO "bond_members" VALUES(35,20);
INSERT INTO "bond_members" VALUES(35,92);
INSERT INTO "bond_members" VALUES(35,84);
INSERT INTO "bond_members" VALUES(36,97);
INSERT INTO "bond_members" VALUES(36,49);
INSERT INTO "bond_members" VALUES(36,44);
INSERT INTO "bond_members" VALUES(37,47);
INSERT INTO "bond_members" VALUES(37,81);
INSERT INTO "bond_members" VALUES(38,50);
INSERT INTO "bond_members" VALUES(38,52);
INSERT INTO "bond_members" VALUES(39,50);
INSERT INTO "bond_members" VALUES(39,64);
INSERT INTO "bond_members" VALUES(22,55);
INSERT INTO "bond_members" VALUES(40,69);
INSERT INTO "bond_members" VALUES(40,57);
INSERT INTO "bond_members" VALUES(41,29);
INSERT INTO "bond_members" VALUES(41,59);
INSERT INTO "bond_members" VALUES(42,90);
INSERT INTO "bond_members" VALUES(42,62);
INSERT INTO "bond_members" VALUES(43,85);
INSERT INTO "bond_members" VALUES(43,78);
INSERT INTO "bond_members" VALUES(43,89);
INSERT INTO "bond_members" VALUES(43,64);
INSERT INTO "bond_members" VALUES(43,28);
INSERT INTO "bond_members" VALUES(43,65);
INSERT INTO "bond_members" VALUES(43,63);
INSERT INTO "bond_members" VALUES(44,11);
INSERT INTO "bond_members" VALUES(44,65);
INSERT INTO "bond_members" VALUES(45,91);
INSERT INTO "bond_members" VALUES(45,71);
INSERT INTO "bond_members" VALUES(45,73);
INSERT INTO "bond_members" VALUES(45,74);
INSERT INTO "bond_members" VALUES(45,86);
INSERT INTO "bond_members" VALUES(46,72);
INSERT INTO "bond_members" VALUES(46,106);
INSERT INTO "bond_members" VALUES(46,104);
INSERT INTO "bond_members" VALUES(47,80);
INSERT INTO "bond_members" VALUES(47,79);
INSERT INTO "bond_members" VALUES(48,82);
INSERT INTO "bond_members" VALUES(48,105);
INSERT INTO "bond_members" VALUES(48,20);
INSERT INTO "bond_members" VALUES(48,15);
INSERT INTO "bond_members" VALUES(48,83);
INSERT INTO "bond_members" VALUES(48,25);
INSERT INTO "bond_members" VALUES(29,20);
INSERT INTO "bond_members" VALUES(29,15);
INSERT INTO "bond_members" VALUES(29,83);
INSERT INTO "bond_members" VALUES(29,25);
INSERT INTO "bond_members" VALUES(49,84);
INSERT INTO "bond_members" VALUES(49,82);
INSERT INTO "bond_members" VALUES(49,83);
INSERT INTO "bond_members" VALUES(50,100);
INSERT INTO "bond_members" VALUES(50,98);
INSERT INTO "bond_members" VALUES(50,99);
INSERT INTO "bond_members" VALUES(51,99);
INSERT INTO "bond_members" VALUES(51,100);
INSERT INTO "bond_members" VALUES(52,16);
INSERT INTO "bond_members" VALUES(52,101);
INSERT INTO "bond_members" VALUES(53,102);
INSERT INTO "bond_members" VALUES(53,104);
CREATE TABLE bonds (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL UNIQUE,
  activation_count INTEGER,
  effect_raw TEXT,
  verification_status TEXT NOT NULL DEFAULT 'S1参考',
  source_id INTEGER REFERENCES sources(id)
);
INSERT INTO "bonds" VALUES(1,'江表虎臣',2,'部队中缘分武将统率提升10点，受到伤害降低3%','Steam已核',4);
INSERT INTO "bonds" VALUES(2,'五子良将',NULL,'部队中缘分武将破甲提升6%','S1参考',1);
INSERT INTO "bonds" VALUES(3,'道法自然',NULL,'战斗前3回合，部队中缘分武将发动准备战法时，有20%概率跳过1回合','S1参考',1);
INSERT INTO "bonds" VALUES(4,'义薄云天',NULL,'部队中缘分武将破甲提升6%','S1参考',1);
INSERT INTO "bonds" VALUES(5,'桃园结义',NULL,'第3回合时，部队中缘分武将行动前驱散自身随机1种负面状态','S1参考',1);
INSERT INTO "bonds" VALUES(6,'五虎上将',NULL,'部队中缘分武将会心几率提升10%','S1参考',1);
INSERT INTO "bonds" VALUES(7,'虎卫御侮',NULL,'部队中缘分武将普通攻击伤害提升12%','S1参考',1);
INSERT INTO "bonds" VALUES(8,'弯弓饮羽',NULL,'部队中缘分武将普通攻击伤害提升8%','S1参考',1);
INSERT INTO "bonds" VALUES(9,'珠联璧合',NULL,'部队中缘分武将受到谋略伤害降低6%','S1参考',1);
INSERT INTO "bonds" VALUES(10,'三分天下',NULL,'部队中缘分武将受到伤害降低6%','S1参考',1);
INSERT INTO "bonds" VALUES(11,'汉末兴乱',NULL,'部队中缘分武将统率提升20点','S1参考',1);
INSERT INTO "bonds" VALUES(12,'懿范长存',NULL,'部队中缘分武将前3回合受到兵刃伤害降低15%','S1参考',1);
INSERT INTO "bonds" VALUES(13,'武皇宣后',NULL,'部队中缘分武将前3回合受到谋略伤害降低15%','S1参考',1);
INSERT INTO "bonds" VALUES(14,'国之栋梁',NULL,'战斗中造成的前3次谋略伤害提升50%','S1参考',1);
INSERT INTO "bonds" VALUES(15,'骁龙飞将',NULL,'部队中缘分武将反击率提升10%','S1参考',1);
INSERT INTO "bonds" VALUES(16,'秋波送情',NULL,'部队中缘分武将受到普通攻击伤害降低12%','S1参考',1);
INSERT INTO "bonds" VALUES(17,'东吴大都督',NULL,'部队中缘分武将获得8%攻心','S1参考',1);
INSERT INTO "bonds" VALUES(18,'士别三日',NULL,'战斗第3回合开始时，部队中缘分武将受到主动战法伤害降低12%','S1参考',1);
INSERT INTO "bonds" VALUES(19,'折冲左右',NULL,'部队中缘分武将武力提升20点','S1参考',1);
INSERT INTO "bonds" VALUES(20,'顾曲唱和',NULL,'部队中缘分武将主动战法发动率提升4%','S1参考',1);
INSERT INTO "bonds" VALUES(21,'苦肉计',NULL,'部队中缘分武将首次受到来自友方的伤害后，受到主动战法伤害降低12%','S1参考',1);
INSERT INTO "bonds" VALUES(22,'曹魏宗将',NULL,'部队中缘分武将最高属性提升15点','S1参考',1);
INSERT INTO "bonds" VALUES(23,'吴宫冷闭',NULL,'部队中缘分武将智力提升20点','S1参考',1);
INSERT INTO "bonds" VALUES(24,'馨香俎豆',NULL,'部队中缘分武将统率提升20点','S1参考',1);
INSERT INTO "bonds" VALUES(25,'神亭酣战',NULL,'部队中缘分武将武力提升20点','S1参考',1);
INSERT INTO "bonds" VALUES(26,'薪火相传',NULL,'部队中缘分武将智力和统率提升6%','S1参考',1);
INSERT INTO "bonds" VALUES(27,'志继江东',NULL,'部队中缘分武将造成伤害提升7%','S1参考',1);
INSERT INTO "bonds" VALUES(28,'南疆烽沏',NULL,'部队中缘分武将视作夷族，我军每存在一个夷族武将，全体夷族受到伤害降低6%','S1参考',1);
INSERT INTO "bonds" VALUES(29,'西蜀之智',NULL,'部队中缘分武将受到谋略伤害降低8%','S1参考',1);
INSERT INTO "bonds" VALUES(30,'黄巾起义',NULL,'战斗前2回合 ，部队中缘分武将主动战法发动率提升8%','S1参考',1);
INSERT INTO "bonds" VALUES(31,'承继太平',NULL,'部队中缘分武将受到兵刃伤害降低6%','S1参考',1);
INSERT INTO "bonds" VALUES(32,'仙人抚顶',NULL,'部队中缘分武将受到谋略伤害降低6%','S1参考',1);
INSERT INTO "bonds" VALUES(33,'懿德芳姿',NULL,'部队中缘分武将受到伤害时，有35%概率令伤害来源降低5点','S1参考',1);
INSERT INTO "bonds" VALUES(34,'枭鸾同谋',NULL,'部队中缘分武将造成谋略伤害时有35%概率获得1种布阵状态(优先获得不同状态)，每个回合可触发1次','S1参考',1);
INSERT INTO "bonds" VALUES(35,'柱石之臣',NULL,'部队中缘分武将对持有异常状态的目标造成的伤害提升8%','S1参考',1);
INSERT INTO "bonds" VALUES(36,'河北庭将',2,'部队中缘分武将武力提升20点','Steam已核',4);
INSERT INTO "bonds" VALUES(37,'夺射锦袍',NULL,'部队中缘分武将破甲提升5%','S1参考',1);
INSERT INTO "bonds" VALUES(38,'嗣业承乾',NULL,'部队中缘分武将统率提升20点','S1参考',1);
INSERT INTO "bonds" VALUES(39,'魏阙凝妆',NULL,'部队中缘分武将受到兵刃伤害降低6%','S1参考',1);
INSERT INTO "bonds" VALUES(40,'汉末栋梁',NULL,'部队中缘分武将受到伤害降低5%','S1参考',1);
INSERT INTO "bonds" VALUES(41,'共承天地',NULL,'部队中缘分武将前3回合受到伤害降低12%','S1参考',1);
INSERT INTO "bonds" VALUES(42,'陈仓双壁',NULL,'部队中缘分武将前4回合受到伤害降低10%','S1参考',1);
INSERT INTO "bonds" VALUES(43,'乱世红颜',NULL,'战斗开始时，部队中缘分武将获得2层抵御','S1参考',1);
INSERT INTO "bonds" VALUES(44,'缘系皇思',NULL,'部队中缘分武将受到兵刃伤害降低6%','S1参考',1);
INSERT INTO "bonds" VALUES(45,'五谋臣',NULL,'部队中缘分武将看破提升5%，受到伤害降低4%','S1参考',1);
INSERT INTO "bonds" VALUES(46,'老当益壮',NULL,'部队中缘分武将受到伤害降低5%','S1参考',1);
INSERT INTO "bonds" VALUES(47,'四世三公',NULL,' 部队中缘分武将受到谋略伤害降低3%，受到兵刃伤害降低3%','S1参考',1);
INSERT INTO "bonds" VALUES(48,'才堪相配',NULL,'部队中缘分武将受到的治疗效果提升8%','S1参考',1);
INSERT INTO "bonds" VALUES(49,'诸葛望族',NULL,'部队中缘分武将破甲和看破提升，我军每存在一个诸葛望族缘分中的武将，诸葛望族缘分中全体武将破甲和看破提升5%','S1参考',1);
INSERT INTO "bonds" VALUES(50,'西凉铁骑',NULL,'部队中缘分武将追击战法伤害提升8%','S1参考',1);
INSERT INTO "bonds" VALUES(51,'西州雄骏',NULL,'部队中缘分武将兵刃伤害提升5%','S1参考',1);
INSERT INTO "bonds" VALUES(52,'锋矢陷阵',NULL,'部队中缘分武将兵刃伤害提升5%','S1参考',1);
INSERT INTO "bonds" VALUES(53,'义烈同途',NULL,'部队中缘分武将行动时，有50%概率对敌军随机单体施加畏惧效果','S1参考',1);
CREATE TABLE effects (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL UNIQUE,
  category TEXT NOT NULL,
  exact_effect TEXT NOT NULL,
  is_control INTEGER NOT NULL DEFAULT 0,
  is_functional INTEGER NOT NULL DEFAULT 0,
  source_id INTEGER REFERENCES sources(id),
  updated_at TEXT NOT NULL
);
INSERT INTO "effects" VALUES(1,'会心','增益状态','造成兵刃伤害时，有概率使该次伤害提升50%',0,0,2,'2026-08-19T17:01:54+08:00');
INSERT INTO "effects" VALUES(2,'奇谋','增益状态','造成谋略伤害时,有概率使该次伤害提升50%',0,0,2,'2026-08-19T17:01:54+08:00');
INSERT INTO "effects" VALUES(3,'破甲','增益状态','造成兵刃伤害时，无视目标部分统率',0,0,2,'2026-08-19T17:01:54+08:00');
INSERT INTO "effects" VALUES(4,'看破','增益状态','造成谋略伤害时,无视目标部分智力',0,0,2,'2026-08-19T17:01:54+08:00');
INSERT INTO "effects" VALUES(5,'倒戈','增益状态','造成兵刃伤害时,根据伤害恢复自身兵力',0,0,2,'2026-08-19T17:01:54+08:00');
INSERT INTO "effects" VALUES(6,'攻心','增益状态','造成谋略伤害时,根据伤害恢复自身兵力',0,0,2,'2026-08-19T17:01:54+08:00');
INSERT INTO "effects" VALUES(7,'连击','增益状态','可额外进行1次普通攻击',0,0,2,'2026-08-19T17:01:54+08:00');
INSERT INTO "effects" VALUES(8,'反击','增益状态','受到普通攻击后，有概率对攻击方进行1次强力普通攻击(不触发追击战法,每回合最多反击5次)',0,0,2,'2026-08-19T17:01:54+08:00');
INSERT INTO "effects" VALUES(9,'规避','增益状态','受到伤害时,有概率使该次伤害无效',0,0,2,'2026-08-19T17:01:54+08:00');
INSERT INTO "effects" VALUES(10,'特殊增益状态','增益状态','某些特殊战法产生增益状态，包括但不限于:造成伤害提升、受到伤害降低和属性提升等',0,0,2,'2026-08-19T17:01:54+08:00');
INSERT INTO "effects" VALUES(11,'清醒','增益状态','免疫控制状态',0,1,2,'2026-08-19T17:01:54+08:00');
INSERT INTO "effects" VALUES(12,'抵御','增益状态','最多持有2层,受到伤害时,消耗1层抵御使该次伤害降至70-90%',0,1,2,'2026-08-19T17:01:54+08:00');
INSERT INTO "effects" VALUES(13,'必中','增益状态','造成的伤害无法被规避',0,1,2,'2026-08-19T17:01:54+08:00');
INSERT INTO "effects" VALUES(14,'破御','增益状态','造成的伤害无法被抵御',0,1,2,'2026-08-19T17:01:54+08:00');
INSERT INTO "effects" VALUES(15,'布局状态','增益状态','布局后可提供的增益状态：布局一：清醒,布局二：1层抵御,布局三：谋略伤害提升8%,布局四：15%奇谋,布局五：玫心提升10%,布局六：统率提升20点,布局七：智力提升20点,布局八：先攻提升20点。（已持有清醒和抵御时视为持有布局一和二）',0,1,2,'2026-08-19T17:01:54+08:00');
INSERT INTO "effects" VALUES(16,'棋局增益','增益状态','不同阵型提供的棋局增益:单前排阵型:我军前排受到伤害降低12%(受智力影响),受击率固定为85%双前排阵型:我军统率最低单体对前排造成伤害提升20%，每回合行动时对敌军随机1-2人造成160%伤害(伤害类型由武力或智力高的一项决定)三前排阵型:每个回合结束后我军智力最高单体对敌军全体造成60%谋略伤害(额外受全队累积治疗量影响)',0,1,2,'2026-08-19T17:01:54+08:00');
INSERT INTO "effects" VALUES(17,'洪水','异常状态','统率降低20点',0,0,2,'2026-08-19T17:01:54+08:00');
INSERT INTO "effects" VALUES(18,'火攻','异常状态','智力降低15点',0,0,2,'2026-08-19T17:01:54+08:00');
INSERT INTO "effects" VALUES(19,'风暴','异常状态','先攻降低30点',0,0,2,'2026-08-19T17:01:54+08:00');
INSERT INTO "effects" VALUES(20,'畏惧','异常状态','受到伤害提升10%',0,0,2,'2026-08-19T17:01:54+08:00');
INSERT INTO "effects" VALUES(21,'妖术','异常状态','会心和奇谋伤害降低15%',0,0,2,'2026-08-19T17:01:54+08:00');
INSERT INTO "effects" VALUES(22,'震慑','异常状态','无法行动',1,0,2,'2026-08-19T17:01:54+08:00');
INSERT INTO "effects" VALUES(23,'缴械','异常状态','无法普通攻击',1,0,2,'2026-08-19T17:01:54+08:00');
INSERT INTO "effects" VALUES(24,'技穷','异常状态','无法发动主动战法',1,0,2,'2026-08-19T17:01:54+08:00');
INSERT INTO "effects" VALUES(25,'混乱','异常状态','普通攻击、追击战法和主动战法无差别选择目标',1,0,2,'2026-08-19T17:01:54+08:00');
INSERT INTO "effects" VALUES(26,'嘲讽','异常状态','强制普通攻击嘲讽施加者',1,0,2,'2026-08-19T17:01:54+08:00');
INSERT INTO "effects" VALUES(27,'虚弱','异常状态','造成的最终伤害降低70%',1,0,2,'2026-08-19T17:01:54+08:00');
INSERT INTO "effects" VALUES(28,'断粮','异常状态','受到的恢复兵力效果降低70%',1,0,2,'2026-08-19T17:01:54+08:00');
INSERT INTO "effects" VALUES(29,'常规负面状态','异常状态','某些特殊战法产生的负面状态,包括但不限于:造成伤害降低、受到伤害提升和属性降低等',0,0,2,'2026-08-19T17:01:54+08:00');
INSERT INTO "effects" VALUES(30,'传递伤害','异常状态','特殊伤害类型，伤害值只受原伤害值影响，无法多次传递',0,0,2,'2026-08-19T17:01:54+08:00');
INSERT INTO "effects" VALUES(31,'控制状态','异常状态','震慑、缴械、技穷、混乱、嘲讽、虚弱、断粮',1,0,2,'2026-08-19T17:01:54+08:00');
INSERT INTO "effects" VALUES(32,'属性降低状态','异常状态','负面状态、武力、智力、统帅、先攻4种基础属性降低',1,0,2,'2026-08-19T17:01:54+08:00');
CREATE TABLE entity_versions(entity_id TEXT NOT NULL, variant TEXT NOT NULL, platform TEXT, applicable_seasons TEXT, source_note TEXT, PRIMARY KEY(entity_id,variant));
INSERT INTO "entity_versions" VALUES('general:0241f361940611212af0','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:0278350322db68c0fb7a','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:035be51454baa21b0e7b','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:083b612aff32ed77fda8','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:084a5bb9b1c318048a03','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:0c61d8ccd98726c3e4fd','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:0d04bc60f598c1da65da','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:0daa6e8c4a81107b3660','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:0f40f23b662bac06c3b7','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:0f4c4105c1f5bc1b73e7','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:11f66bd3d8003f05b265','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:121d406fe7d172e7f8ea','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:12d700a23b775c08623f','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:13144b0dc85fccd26d2c','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:16e9b12b026f2d40d0fc','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:1c787ea61216883fd85e','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:1fbb0e34373c3146b851','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:21556222ec2ac1e89ba2','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:2157ac6b1d85220f6eee','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:22aa2627da5c33f8c48e','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:22b24edb3bdf2d0a2c72','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:230b319340cc67b6f402','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:25fc0bde1163ca42219a','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:2665384131699d31ae0d','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:2a7e68aa7262c5da7f9f','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:2d0b5eef660945109161','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:305ba64ecb1596140943','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:32ae32453c0b8b8c5e3a','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:35ca90d064630a3cea3c','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:375995287c1b6f3453ff','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:397edec8b12ae66acf2c','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:3db6ab6fdbba6fddc423','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:4b97cac39000f1c8f17e','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:4f57385c8b1cd7e417b7','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:4fbe01ab8d14bc669b3e','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:5109ea07440a2473642b','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:525276a9bc4a7162be8f','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:53081486f9dbff9359d8','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:5508fa98c2d6421d3e3c','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:58b6c02e43ff0623a55f','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:593ee96e11ce91cde8ea','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:596c893874a6a0abe9d3','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:5ba7e78c435dbbbe3d66','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:5d3f27adabcf2be8a310','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:5eeb463fc63a880ad0d8','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:603b840477e3aa4a40b8','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:63655267babca9c136c2','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:63bf93615779c60037e7','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:653eea8eb9c64a51bd60','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:66476632eb31ce501972','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:67e210997dbbf2430955','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:727dbb61cc174f1035db','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:745dc71ccc2c607d55d4','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:7a3e3d0cedc9feb9bec5','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:7a68e94f3d87bf298226','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:7e056ff12a2f1de0d059','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:7e6ebaf83b5273507779','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:7ec989f15850757bb4a3','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:823d59e4b1f09b921470','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:8321c989883724cb13b2','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:83f68b3328def1bac222','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:8460abc20204db9039a8','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:87a4a65f88e7b38b5190','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:8ac44a43f06673d6272e','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:8dc0bfe19c5d81dc129c','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:8e64b2b3040737249797','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:9001e293139ffd6b077e','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:91b50644508b1fb50972','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:943b7a7b14597aba4a9f','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:95264f699dc478478eef','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:96633bbf689f585f17ef','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:9723e8a4f08c7d5d4141','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:979781ac090cb71634a2','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:97faa2c456a914aded58','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:98a7cab00b413a7cd555','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:990961b2ffc3e6140e01','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:9ebe9a7cec93ffc5d3b4','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:9f7272bc767cfa4ad9cd','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:a02cbd2e268c2c5650ff','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:a03830e035dfa5932ce6','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:a5b74013147e47af899b','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:af28979bd438c204232c','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:b0a10e3213fecf035b18','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:b3b9237f88457d7a6edd','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:bd53b54cd679c8e506b3','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:c812f6eeb7d6aa8c14ab','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:c9065395c9a7298a3331','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:ceb3333e1809f65f0759','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:ced9a805145ed4c2bbfb','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:d04269a972ec14e0c95e','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:d09edc72e62e34cdb2da','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:d4632f7a4c7c53ebc4f6','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:d4e07c3461a25a5da3c8','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:d949c9c8d528498c7bc1','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:da92b2d00992af2ab4fe','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:daf7b56cd3aea44f7fdf','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:deb8aed434adbe9bbd21','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:e4039426f9f0f5d96689','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:ee71891a2d47572831ad','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:f2f34af1e7f448967678','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:f88e20a568d008a29c2d','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:ff0ae9c2a3b32145b872','普通',NULL,NULL,NULL);
INSERT INTO "entity_versions" VALUES('general:e4039426f9f0f5d96689','英雄',NULL,NULL,'用户Steam S2截图（2026-09-10，当前武将/战法）');
CREATE TABLE factions(name TEXT PRIMARY KEY);
INSERT INTO "factions" VALUES('魏');
INSERT INTO "factions" VALUES('群');
INSERT INTO "factions" VALUES('蜀');
INSERT INTO "factions" VALUES('吴');
CREATE TABLE formations (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL UNIQUE,
  front_slots INTEGER NOT NULL,
  rear_slots INTEGER NOT NULL,
  effect_raw TEXT NOT NULL,
  verification_status TEXT NOT NULL,
  source_id INTEGER REFERENCES sources(id),
  updated_at TEXT NOT NULL
);
INSERT INTO "formations" VALUES(1,'一字阵',3,0,'前排受到伤害降低8%','效果Steam已核；站位S1参考',4,'2026-08-19T17:01:54+08:00');
INSERT INTO "formations" VALUES(2,'箕形阵',1,2,'前排受到伤害降低6%；后排造成伤害提升12%','效果Steam已核；站位S1参考',4,'2026-08-19T17:01:54+08:00');
INSERT INTO "formations" VALUES(3,'雁形阵',2,1,'前排统率提升20点；后排造成伤害提升15%','Steam已核',4,'2026-08-19T17:01:54+08:00');
INSERT INTO "formations" VALUES(4,'方圆阵',2,1,'前排受到伤害降低5%；后排普通攻击率提升40%','效果Steam已核；站位S1参考',4,'2026-08-19T17:01:54+08:00');
INSERT INTO "formations" VALUES(5,'锥形阵',1,2,'前排造成伤害提升16%；后排受到伤害降低5%','效果Steam已核；站位S1参考',4,'2026-08-19T17:01:54+08:00');
INSERT INTO "formations" VALUES(6,'鱼鳞阵',1,2,'前排规避率提升12%；后排会心、奇谋几率提升8%','效果Steam已核；站位S1参考',4,'2026-08-19T17:01:54+08:00');
CREATE TABLE general_stat_observations (
  id INTEGER PRIMARY KEY,
  general_id INTEGER NOT NULL REFERENCES generals(id),
  level INTEGER NOT NULL,
  advancement INTEGER,
  allocated_force INTEGER NOT NULL DEFAULT 0,
  allocated_intelligence INTEGER NOT NULL DEFAULT 0,
  allocated_command INTEGER NOT NULL DEFAULT 0,
  allocated_initiative INTEGER NOT NULL DEFAULT 0,
  observed_force INTEGER,
  observed_intelligence INTEGER,
  observed_command INTEGER,
  observed_initiative INTEGER,
  context TEXT,
  source_id INTEGER REFERENCES sources(id),
  observed_at TEXT NOT NULL
);
INSERT INTO "general_stat_observations" VALUES(1,23,50,NULL,0,50,0,0,40,242,182,113,'演武大会固定50级，全智力+50',4,'2026-08-05');
INSERT INTO "general_stat_observations" VALUES(2,66,50,NULL,50,0,0,0,275,144,186,188,'演武大会固定50级，全武力+50',4,'2026-08-05');
CREATE TABLE general_strategy_eligibility (
  general_id INTEGER NOT NULL REFERENCES generals(id) ON DELETE CASCADE,
  strategy_book_id INTEGER NOT NULL REFERENCES strategy_books(id) ON DELETE CASCADE,
  verification_status TEXT NOT NULL,
  source_id INTEGER REFERENCES sources(id),
  PRIMARY KEY (general_id, strategy_book_id)
);
CREATE TABLE generals (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL UNIQUE,
  url TEXT,
  faction TEXT,
  quality TEXT,
  troop_type TEXT,
  combat_role TEXT,
  first_season TEXT,
  reference_level INTEGER NOT NULL DEFAULT 5,
  base_force REAL,
  growth_force REAL,
  base_intelligence REAL,
  growth_intelligence REAL,
  base_command REAL,
  growth_command REAL,
  base_initiative REAL,
  growth_initiative REAL,
  self_tactic_id INTEGER REFERENCES tactics(id),
  strategy_recommendation_status TEXT NOT NULL DEFAULT '待可靠来源',
  verification_status TEXT NOT NULL DEFAULT 'S1参考',
  source_id INTEGER REFERENCES sources(id),
  updated_at TEXT NOT NULL
, entity_id TEXT, applicable_seasons TEXT, platform TEXT);
INSERT INTO "generals" VALUES(2,'乐进','https://www.sgmdtx.com/wj/乐进/','魏',NULL,'盾',NULL,'s3',5,113.0,2.35,56.0,0.86,104.0,1.81,92.0,2.33,132,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:da92b2d00992af2ab4fe',NULL,NULL);
INSERT INTO "generals" VALUES(3,'于吉','https://www.sgmdtx.com/wj/于吉/','群',NULL,'弓',NULL,'s4',5,12.0,0.21,103.0,2.51,74.0,1.87,86.0,1.97,219,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:deb8aed434adbe9bbd21',NULL,NULL);
INSERT INTO "generals" VALUES(4,'于禁','https://www.sgmdtx.com/wj/于禁/','魏','金','盾','防御','s1',5,88.0,1.5,70.0,0.79,102.0,2.05,44.0,1.5,99,'待可靠来源','Steam已核',1,'2026-08-19T17:01:54+08:00','general:21556222ec2ac1e89ba2',NULL,NULL);
INSERT INTO "generals" VALUES(5,'公孙瓒','https://www.sgmdtx.com/wj/公孙瓒/','群',NULL,'盾',NULL,'s3',5,99.0,2.01,86.0,1.91,103.0,1.9,96.0,2.3,73,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:a02cbd2e268c2c5650ff',NULL,NULL);
INSERT INTO "generals" VALUES(6,'关平','https://www.sgmdtx.com/wj/关平/','蜀','金','盾','兵刃','s1',5,108.0,2.42,52.0,0.99,100.0,1.67,81.0,2.22,231,'待可靠来源','Steam已核',1,'2026-08-19T17:01:54+08:00','general:5109ea07440a2473642b',NULL,NULL);
INSERT INTO "generals" VALUES(7,'关羽','https://www.sgmdtx.com/wj/关羽/','蜀','金','盾','兵刃','s1',5,120.0,2.75,86.0,1.35,104.0,2.13,79.0,2.43,72,'待可靠来源','Steam已核',1,'2026-08-19T17:01:54+08:00','general:4b97cac39000f1c8f17e',NULL,NULL);
INSERT INTO "generals" VALUES(8,'关银屏','https://www.sgmdtx.com/wj/关银屏/','蜀',NULL,'骑',NULL,'s4',5,108.0,2.55,60.0,0.99,89.0,1.78,86.0,2.36,181,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:230b319340cc67b6f402',NULL,NULL);
INSERT INTO "generals" VALUES(9,'典韦','https://www.sgmdtx.com/wj/典韦/','魏','金','盾','兵刃','s1',5,120.0,2.78,42.0,0.37,114.0,1.75,65.0,2.3,48,'待可靠来源','Steam已核',1,'2026-08-19T17:01:54+08:00','general:2157ac6b1d85220f6eee',NULL,NULL);
INSERT INTO "generals" VALUES(10,'凌统','https://www.sgmdtx.com/wj/凌统/','吴',NULL,'骑',NULL,'s9',5,102.0,2.18,63.0,0.88,89.0,1.42,90.0,2.42,114,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:91b50644508b1fb50972',NULL,NULL);
INSERT INTO "generals" VALUES(11,'刘备','https://www.sgmdtx.com/wj/刘备/','蜀','金','盾','治疗','s1',5,80.0,1.43,94.0,2.31,109.0,2.12,53.0,1.72,104,'待可靠来源','S1参考',1,'2026-08-19T17:01:54+08:00','general:daf7b56cd3aea44f7fdf',NULL,NULL);
INSERT INTO "generals" VALUES(12,'华佗','https://www.sgmdtx.com/wj/华佗/','群','金','盾','辅助','s1',5,13.0,0.35,106.0,2.35,68.0,1.6,55.0,1.73,228,'待可靠来源','S1参考',1,'2026-08-19T17:01:54+08:00','general:084a5bb9b1c318048a03',NULL,NULL);
INSERT INTO "generals" VALUES(13,'华雄','https://www.sgmdtx.com/wj/华雄/','群','金','盾','兵刃','s1',5,105.0,2.39,43.0,0.65,87.0,1.79,83.0,2.48,172,'待可靠来源','S1参考',1,'2026-08-19T17:01:54+08:00','general:9ebe9a7cec93ffc5d3b4',NULL,NULL);
INSERT INTO "generals" VALUES(14,'卞夫人','https://www.sgmdtx.com/wj/卞夫人/','魏',NULL,'弓',NULL,'s10',5,19.0,0.23,105.0,2.18,106.0,1.8,57.0,1.5,167,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:b0a10e3213fecf035b18',NULL,NULL);
INSERT INTO "generals" VALUES(15,'司马懿','https://www.sgmdtx.com/wj/司马懿/','魏',NULL,'盾',NULL,'s3',5,69.0,0.34,119.0,2.8,114.0,2.11,47.0,1.54,227,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:32ae32453c0b8b8c5e3a',NULL,NULL);
INSERT INTO "generals" VALUES(16,'吕布','https://www.sgmdtx.com/wj/吕布/','群','金','盾','兵刃','s1',5,125.0,3.0,38.0,0.7,93.0,1.89,76.0,2.57,225,'待可靠来源','S1参考',1,'2026-08-19T17:01:54+08:00','general:990961b2ffc3e6140e01',NULL,NULL);
INSERT INTO "generals" VALUES(17,'吕蒙','https://www.sgmdtx.com/wj/吕蒙/','吴','金','盾','谋略','s1',5,93.0,1.9,106.0,2.38,103.0,1.8,77.0,2.19,149,'待可靠来源','S1参考',1,'2026-08-19T17:01:54+08:00','general:d09edc72e62e34cdb2da',NULL,NULL);
INSERT INTO "generals" VALUES(18,'周仓','https://www.sgmdtx.com/wj/周仓/','蜀','金','盾','防御','s1',5,89.0,1.7,70.0,1.02,109.0,2.05,71.0,1.92,88,'待可靠来源','Steam已核',1,'2026-08-19T17:01:54+08:00','general:63bf93615779c60037e7',NULL,NULL);
INSERT INTO "generals" VALUES(19,'周泰','https://www.sgmdtx.com/wj/周泰/','吴',NULL,'盾',NULL,'s3',5,87.0,1.5,52.0,0.78,112.0,2.21,63.0,1.45,9,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:97faa2c456a914aded58',NULL,NULL);
INSERT INTO "generals" VALUES(20,'周瑜','https://www.sgmdtx.com/wj/周瑜/','吴','金','盾','谋略','s1',5,77.0,0.95,114.0,2.75,104.0,2.01,62.0,1.73,11,'待可靠来源','Steam已核',1,'2026-08-19T17:01:54+08:00','general:ff0ae9c2a3b32145b872',NULL,NULL);
INSERT INTO "generals" VALUES(21,'夏侯惇','https://www.sgmdtx.com/wj/夏侯惇/','魏','金','盾','兵刃','s1',5,102.0,2.4,72.0,1.02,113.0,2.03,71.0,1.78,37,'待可靠来源','S1参考',1,'2026-08-19T17:01:54+08:00','general:2a7e68aa7262c5da7f9f',NULL,NULL);
INSERT INTO "generals" VALUES(22,'夏侯渊','https://www.sgmdtx.com/wj/夏侯渊/','魏','金','盾','兵刃','s1',5,107.0,2.4,59.0,0.75,101.0,1.74,94.0,2.81,162,'待可靠来源','Steam已核',1,'2026-08-19T17:01:54+08:00','general:727dbb61cc174f1035db',NULL,NULL);
INSERT INTO "generals" VALUES(23,'大乔','https://www.sgmdtx.com/wj/大乔/','吴','金','盾','辅助','s1',5,24.0,0.35,95.0,2.15,106.0,1.69,35.0,1.72,55,'待可靠来源','Steam已核',1,'2026-08-19T17:01:54+08:00','general:8ac44a43f06673d6272e',NULL,NULL);
INSERT INTO "generals" VALUES(24,'太史慈','https://www.sgmdtx.com/wj/太史慈/','吴','金','盾','兵刃','s1',5,110.0,2.49,94.0,1.22,108.0,1.89,80.0,2.54,232,'待可靠来源','S1参考',1,'2026-08-19T17:01:54+08:00','general:5ba7e78c435dbbbe3d66',NULL,NULL);
INSERT INTO "generals" VALUES(25,'姜维','https://www.sgmdtx.com/wj/姜维/','蜀',NULL,'枪',NULL,'s5',5,101.0,2.39,111.0,2.52,91.0,2.01,76.0,1.99,15,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:0c61d8ccd98726c3e4fd',NULL,NULL);
INSERT INTO "generals" VALUES(26,'孙坚','https://www.sgmdtx.com/wj/孙坚/','吴','金','盾','兵刃','s1',5,100.0,2.18,82.0,0.77,113.0,2.3,73.0,1.71,130,'待可靠来源','S1参考',1,'2026-08-19T17:01:54+08:00','general:1fbb0e34373c3146b851',NULL,NULL);
INSERT INTO "generals" VALUES(27,'孙坚2','https://www.sgmdtx.com/wj/孙坚2/','吴',NULL,'盾',NULL,'s13',5,106.0,2.62,70.0,1.55,100.0,2.34,85.0,1.92,188,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:ee71891a2d47572831ad',NULL,NULL);
INSERT INTO "generals" VALUES(28,'孙尚香','https://www.sgmdtx.com/wj/孙尚香/','吴','金','盾','兵刃','s1',5,107.0,2.38,79.0,0.98,97.0,1.66,70.0,2.41,83,'待可靠来源','S1参考',1,'2026-08-19T17:01:54+08:00','general:823d59e4b1f09b921470',NULL,NULL);
INSERT INTO "generals" VALUES(29,'孙权','https://www.sgmdtx.com/wj/孙权/','吴','金','盾','辅助','s1',5,90.0,1.91,96.0,2.08,101.0,2.09,74.0,2.33,183,'待可靠来源','Steam已核',1,'2026-08-19T17:01:54+08:00','general:2d0b5eef660945109161',NULL,NULL);
INSERT INTO "generals" VALUES(30,'孙策','https://www.sgmdtx.com/wj/孙策/','吴','金','盾','兵刃','s1',5,112.0,2.59,77.0,1.3,110.0,2.12,74.0,2.53,38,'待可靠来源','Steam已核',1,'2026-08-19T17:01:54+08:00','general:0278350322db68c0fb7a',NULL,NULL);
INSERT INTO "generals" VALUES(31,'孟获','https://www.sgmdtx.com/wj/孟获/','群',NULL,'盾',NULL,'s11',5,97.0,2.1,67.0,0.64,108.0,2.44,77.0,1.92,212,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:305ba64ecb1596140943',NULL,NULL);
INSERT INTO "generals" VALUES(32,'小乔','https://www.sgmdtx.com/wj/小乔/','吴','金','盾','治疗','s1',5,22.0,0.38,94.0,2.14,88.0,1.64,73.0,2.39,61,'待可靠来源','Steam已核',1,'2026-08-19T17:01:54+08:00','general:67e210997dbbf2430955',NULL,NULL);
INSERT INTO "generals" VALUES(33,'左慈','https://www.sgmdtx.com/wj/左慈/','群',NULL,'盾',NULL,'s4',5,14.0,0.34,112.0,2.65,88.0,2.13,63.0,1.77,18,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:ceb3333e1809f65f0759',NULL,NULL);
INSERT INTO "generals" VALUES(34,'庞德','https://www.sgmdtx.com/wj/庞德/','群','金','盾','兵刃','s1',5,106.0,2.4,71.0,0.78,93.0,1.69,73.0,2.69,211,'待可靠来源','S1参考',1,'2026-08-19T17:01:54+08:00','general:083b612aff32ed77fda8',NULL,NULL);
INSERT INTO "generals" VALUES(35,'庞统','https://www.sgmdtx.com/wj/庞统/','蜀',NULL,'盾',NULL,'s3',5,54.0,0.55,116.0,2.65,83.0,1.75,51.0,1.65,202,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:d04269a972ec14e0c95e',NULL,NULL);
INSERT INTO "generals" VALUES(36,'张宁','https://www.sgmdtx.com/wj/张宁/','群',NULL,'弓',NULL,'s7',5,56.0,0.7,107.0,2.4,102.0,2.85,77.0,1.6,62,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:d4632f7a4c7c53ebc4f6',NULL,NULL);
INSERT INTO "generals" VALUES(37,'张宝','https://www.sgmdtx.com/wj/张宝/','群','金','盾','谋略','s1',5,66.0,0.24,101.0,2.25,99.0,1.73,65.0,1.75,70,'待可靠来源','Steam已核',1,'2026-08-19T17:01:54+08:00','general:35ca90d064630a3cea3c',NULL,NULL);
INSERT INTO "generals" VALUES(38,'张春华','https://www.sgmdtx.com/wj/张春华/','魏',NULL,'盾',NULL,'s8',5,43.0,0.35,96.0,2.19,93.0,2.12,69.0,1.56,179,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:66476632eb31ce501972',NULL,NULL);
INSERT INTO "generals" VALUES(39,'张昭','https://www.sgmdtx.com/wj/张昭/','吴',NULL,'弓',NULL,'s8',5,16.0,0.23,103.0,2.3,83.0,1.65,87.0,1.79,153,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:7ec989f15850757bb4a3',NULL,NULL);
INSERT INTO "generals" VALUES(41,'张梁','https://www.sgmdtx.com/wj/张梁/','群','金','盾','兵刃','s1',5,105.0,2.15,47.0,0.51,109.0,1.98,73.0,2.08,69,'待可靠来源','Steam已核',1,'2026-08-19T17:01:54+08:00','general:e4039426f9f0f5d96689',NULL,NULL);
INSERT INTO "generals" VALUES(42,'张角','https://www.sgmdtx.com/wj/张角/','群','金','盾','谋略','s1',5,35.0,0.43,113.0,2.55,105.0,1.99,62.0,1.53,229,'待可靠来源','Steam已核',1,'2026-08-19T17:01:54+08:00','general:5508fa98c2d6421d3e3c',NULL,NULL);
INSERT INTO "generals" VALUES(43,'张辽','https://www.sgmdtx.com/wj/张辽/','魏',NULL,'盾',NULL,'s2',5,113.0,2.55,92.0,1.49,103.0,1.95,87.0,2.61,220,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:a5b74013147e47af899b',NULL,NULL);
INSERT INTO "generals" VALUES(44,'张郃','https://www.sgmdtx.com/wj/张郃/','魏','金','盾','兵刃','s1',5,104.0,2.59,81.0,0.77,101.0,1.91,67.0,1.93,59,'待可靠来源','Steam已核',1,'2026-08-19T17:01:54+08:00','general:a03830e035dfa5932ce6',NULL,NULL);
INSERT INTO "generals" VALUES(45,'张飞','https://www.sgmdtx.com/wj/张飞/','蜀','金','盾','兵刃','s1',5,121.0,2.78,65.0,1.04,99.0,1.84,79.0,2.29,3,'待可靠来源','Steam已核',1,'2026-08-19T17:01:54+08:00','general:95264f699dc478478eef',NULL,NULL);
INSERT INTO "generals" VALUES(46,'徐庶','https://www.sgmdtx.com/wj/徐庶/','蜀','金','盾',NULL,'s1',5,95.0,1.95,109.0,2.55,93.0,1.59,87.0,2.36,97,'待可靠来源','Steam已核',1,'2026-08-19T17:01:54+08:00','general:8321c989883724cb13b2',NULL,NULL);
INSERT INTO "generals" VALUES(47,'徐晃','https://www.sgmdtx.com/wj/徐晃/','魏','金','盾','兵刃','s1',5,105.0,2.58,79.0,0.88,106.0,1.75,75.0,2.12,209,'待可靠来源','Steam已核',1,'2026-08-19T17:01:54+08:00','general:58b6c02e43ff0623a55f',NULL,NULL);
INSERT INTO "generals" VALUES(48,'徐盛','https://www.sgmdtx.com/wj/徐盛/','吴','金','盾','防御','s1',5,89.0,1.61,87.0,1.89,107.0,2.08,34.0,1.52,151,'待可靠来源','Steam已核',1,'2026-08-19T17:01:54+08:00','general:0d04bc60f598c1da65da',NULL,NULL);
INSERT INTO "generals" VALUES(49,'文丑','https://www.sgmdtx.com/wj/文丑/','群','金','盾','兵刃','s1',5,108.0,2.4,45.0,0.67,91.0,1.68,76.0,2.4,20,'待可靠来源','Steam已核',1,'2026-08-19T17:01:54+08:00','general:0f4c4105c1f5bc1b73e7',NULL,NULL);
INSERT INTO "generals" VALUES(50,'曹丕','https://www.sgmdtx.com/wj/曹丕/','魏',NULL,'弓',NULL,'s9',5,89.0,1.62,97.0,2.28,103.0,2.12,62.0,1.62,124,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:7e056ff12a2f1de0d059',NULL,NULL);
INSERT INTO "generals" VALUES(51,'曹仁','https://www.sgmdtx.com/wj/曹仁/','魏','金','盾','防御','s1',5,81.0,1.35,79.0,1.53,113.0,2.35,44.0,1.55,54,'待可靠来源','S1参考',1,'2026-08-19T17:01:54+08:00','general:121d406fe7d172e7f8ea',NULL,NULL);
INSERT INTO "generals" VALUES(52,'曹操','https://www.sgmdtx.com/wj/曹操/','魏','金','盾','辅助','s1',5,76.0,1.3,102.0,2.3,107.0,2.52,53.0,1.79,16,'待可靠来源','S1参考',1,'2026-08-19T17:01:54+08:00','general:4fbe01ab8d14bc669b3e',NULL,NULL);
INSERT INTO "generals" VALUES(55,'曹纯','https://www.sgmdtx.com/wj/曹纯/','魏',NULL,'骑',NULL,'s4',5,94.0,2.13,68.0,0.67,100.0,1.91,77.0,2.0,60,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:d4e07c3461a25a5da3c8',NULL,NULL);
INSERT INTO "generals" VALUES(56,'木鹿大王','https://www.sgmdtx.com/wj/木鹿大王/','群',NULL,'骑',NULL,'s13',5,73.0,1.22,103.0,2.33,82.0,1.76,88.0,1.98,223,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:0f40f23b662bac06c3b7',NULL,NULL);
INSERT INTO "generals" VALUES(57,'朱儁','https://www.sgmdtx.com/wj/朱儁/','群',NULL,'弓',NULL,'s7',5,82.0,1.9,99.0,2.21,106.0,2.12,88.0,1.67,52,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:c812f6eeb7d6aa8c14ab',NULL,NULL);
INSERT INTO "generals" VALUES(58,'李儒','https://www.sgmdtx.com/wj/李儒/','群','金','盾','谋略','s1',5,27.0,0.35,105.0,2.48,88.0,1.48,60.0,1.99,226,'待可靠来源','S1参考',1,'2026-08-19T17:01:54+08:00','general:593ee96e11ce91cde8ea',NULL,NULL);
INSERT INTO "generals" VALUES(59,'步练师','https://www.sgmdtx.com/wj/步练师/','吴',NULL,'盾',NULL,'s5',5,33.0,0.38,105.0,2.19,97.0,1.69,81.0,2.25,137,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:7a68e94f3d87bf298226',NULL,NULL);
INSERT INTO "generals" VALUES(60,'法正','https://www.sgmdtx.com/wj/法正/','蜀','金','盾',NULL,'s2',5,52.0,0.29,100.0,2.59,83.0,1.64,76.0,2.3,154,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:12d700a23b775c08623f',NULL,NULL);
INSERT INTO "generals" VALUES(62,'王双','https://www.sgmdtx.com/wj/王双/','魏',NULL,'骑',NULL,'s14',5,106.0,2.52,54.0,0.88,88.0,1.68,87.0,2.51,89,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:11f66bd3d8003f05b265',NULL,NULL);
INSERT INTO "generals" VALUES(63,'王异','https://www.sgmdtx.com/wj/王异/','魏',NULL,'枪',NULL,'s6',5,17.0,0.21,110.0,2.58,94.0,1.98,86.0,1.76,80,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:0241f361940611212af0',NULL,NULL);
INSERT INTO "generals" VALUES(64,'甄洛','https://www.sgmdtx.com/wj/甄洛/','魏','金','盾','辅助','s1',5,22.0,0.23,103.0,2.16,103.0,1.62,56.0,1.55,136,'待可靠来源','S1参考',1,'2026-08-19T17:01:54+08:00','general:22b24edb3bdf2d0a2c72',NULL,NULL);
INSERT INTO "generals" VALUES(65,'甘夫人','https://www.sgmdtx.com/wj/甘夫人/','蜀',NULL,'盾',NULL,'s3',5,25.0,0.29,102.0,1.95,106.0,1.62,90.0,1.68,152,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:9723e8a4f08c7d5d4141',NULL,NULL);
INSERT INTO "generals" VALUES(66,'甘宁','https://www.sgmdtx.com/wj/甘宁/','吴','金','盾','兵刃','s1',5,112.0,2.51,84.0,1.32,107.0,1.75,71.0,2.59,208,'待可靠来源','Steam已核',1,'2026-08-19T17:01:54+08:00','general:2665384131699d31ae0d',NULL,NULL);
INSERT INTO "generals" VALUES(67,'田丰','https://www.sgmdtx.com/wj/田丰/','群','金','盾',NULL,'s2',5,50.0,0.33,84.0,2.24,65.0,1.67,66.0,2.12,178,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:25fc0bde1163ca42219a',NULL,NULL);
INSERT INTO "generals" VALUES(69,'皇甫嵩2','https://www.sgmdtx.com/wj/皇甫嵩2/','群',NULL,'盾',NULL,'s7',5,89.0,1.83,85.0,1.96,111.0,2.36,65.0,1.93,30,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:7a3e3d0cedc9feb9bec5',NULL,NULL);
INSERT INTO "generals" VALUES(70,'祝融夫人','https://www.sgmdtx.com/wj/祝融夫人/','群',NULL,'骑',NULL,'s11',5,112.0,2.46,72.0,0.9,91.0,1.95,82.0,2.18,46,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:b3b9237f88457d7a6edd',NULL,NULL);
INSERT INTO "generals" VALUES(71,'程昱','https://www.sgmdtx.com/wj/程昱/','魏','金','盾','谋略','s1',5,47.0,0.57,111.0,2.46,84.0,1.73,73.0,2.24,41,'待可靠来源','Steam已核',1,'2026-08-19T17:01:54+08:00','general:16e9b12b026f2d40d0fc',NULL,NULL);
INSERT INTO "generals" VALUES(72,'程普','https://www.sgmdtx.com/wj/程普/','吴','金','盾','辅助','s1',5,79.0,1.58,81.0,1.54,91.0,2.32,59.0,1.7,29,'待可靠来源','S1参考',1,'2026-08-19T17:01:54+08:00','general:83f68b3328def1bac222',NULL,NULL);
INSERT INTO "generals" VALUES(73,'荀彧','https://www.sgmdtx.com/wj/荀彧/','魏','金','盾','辅助','s1',5,37.0,0.19,120.0,2.7,78.0,1.6,57.0,1.65,82,'待可靠来源','S1参考',1,'2026-08-19T17:01:54+08:00','general:035be51454baa21b0e7b',NULL,NULL);
INSERT INTO "generals" VALUES(74,'荀攸','https://www.sgmdtx.com/wj/荀攸/','魏',NULL,'弓',NULL,'s5',5,41.0,0.59,114.0,2.45,87.0,1.69,59.0,2.15,42,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:9f7272bc767cfa4ad9cd',NULL,NULL);
INSERT INTO "generals" VALUES(75,'董卓','https://www.sgmdtx.com/wj/董卓/','群','金','盾','文武','s1',5,101.0,2.2,87.0,1.42,110.0,2.1,85.0,1.93,123,'待可靠来源','S1参考',1,'2026-08-19T17:01:54+08:00','general:96633bbf689f585f17ef',NULL,NULL);
INSERT INTO "generals" VALUES(78,'蔡文姬','https://www.sgmdtx.com/wj/蔡文姬/','群','金','盾','治疗','s1',5,18.0,0.24,107.0,2.29,94.0,1.59,87.0,1.92,92,'待可靠来源','Steam已核',1,'2026-08-19T17:01:54+08:00','general:8e64b2b3040737249797',NULL,NULL);
INSERT INTO "generals" VALUES(79,'袁术','https://www.sgmdtx.com/wj/袁术/','群',NULL,'盾',NULL,'s6',5,76.0,1.86,89.0,1.83,104.0,2.18,80.0,1.91,26,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:375995287c1b6f3453ff',NULL,NULL);
INSERT INTO "generals" VALUES(80,'袁绍','https://www.sgmdtx.com/wj/袁绍/','群','金','盾','辅助','s1',5,80.0,2.0,92.0,1.8,105.0,2.03,68.0,2.25,49,'待可靠来源','S1参考',1,'2026-08-19T17:01:54+08:00','general:653eea8eb9c64a51bd60',NULL,NULL);
INSERT INTO "generals" VALUES(81,'许褚','https://www.sgmdtx.com/wj/许褚/','魏','金','盾','兵刃','s1',5,114.0,2.75,45.0,0.43,95.0,1.64,69.0,2.6,184,'待可靠来源','S1参考',1,'2026-08-19T17:01:54+08:00','general:7e6ebaf83b5273507779',NULL,NULL);
INSERT INTO "generals" VALUES(82,'诸葛亮','https://www.sgmdtx.com/wj/诸葛亮/','蜀','金','盾','谋略','s1',5,50.0,0.52,125.0,3.0,111.0,2.3,57.0,1.65,177,'待可靠来源','S1参考',1,'2026-08-19T17:01:54+08:00','general:53081486f9dbff9359d8',NULL,NULL);
INSERT INTO "generals" VALUES(83,'诸葛亮2','https://www.sgmdtx.com/wj/诸葛亮2/','蜀',NULL,'盾',NULL,'s8',5,53.0,0.56,125.0,3.0,104.0,2.24,61.0,1.71,117,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:1c787ea61216883fd85e',NULL,NULL);
INSERT INTO "generals" VALUES(84,'诸葛瑾','https://www.sgmdtx.com/wj/诸葛瑾/','吴',NULL,'弓',NULL,'s12',5,38.0,0.55,104.0,2.35,86.0,2.28,78.0,1.32,94,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:98a7cab00b413a7cd555',NULL,NULL);
INSERT INTO "generals" VALUES(85,'貂蝉','https://www.sgmdtx.com/wj/貂蝉/','群','金','盾','防御','s1',5,20.0,0.41,104.0,2.22,97.0,1.75,55.0,2.03,210,'待可靠来源','Steam已核',1,'2026-08-19T17:01:54+08:00','general:5d3f27adabcf2be8a310',NULL,NULL);
INSERT INTO "generals" VALUES(86,'贾诩','https://www.sgmdtx.com/wj/贾诩/','魏','金','盾',NULL,'s2',5,58.0,0.21,106.0,2.75,81.0,1.73,56.0,2.06,189,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:397edec8b12ae66acf2c',NULL,NULL);
INSERT INTO "generals" VALUES(87,'赵云','https://www.sgmdtx.com/wj/赵云/','蜀','金','盾','兵刃','s1',5,117.0,2.65,77.0,1.52,107.0,2.15,66.0,2.29,2,'待可靠来源','Steam已核',1,'2026-08-19T17:01:54+08:00','general:d949c9c8d528498c7bc1',NULL,NULL);
INSERT INTO "generals" VALUES(88,'邓艾','https://www.sgmdtx.com/wj/邓艾/','魏','金','盾','治疗','s1',5,94.0,1.8,101.0,2.1,100.0,1.73,66.0,1.75,77,'待可靠来源','S1参考',1,'2026-08-19T17:01:54+08:00','general:4f57385c8b1cd7e417b7',NULL,NULL);
INSERT INTO "generals" VALUES(89,'邹氏','https://www.sgmdtx.com/wj/邹氏/','群','金','盾','辅助','s1',5,16.0,0.25,94.0,1.85,88.0,1.65,64.0,1.73,216,'待可靠来源','S1参考',1,'2026-08-19T17:01:54+08:00','general:13144b0dc85fccd26d2c',NULL,NULL);
INSERT INTO "generals" VALUES(90,'郝昭','https://www.sgmdtx.com/wj/郝昭/','魏',NULL,'盾',NULL,'s14',5,92.0,1.42,97.0,2.02,101.0,2.32,56.0,1.68,44,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:3db6ab6fdbba6fddc423',NULL,NULL);
INSERT INTO "generals" VALUES(91,'郭嘉','https://www.sgmdtx.com/wj/郭嘉/','魏','金','盾','谋略','s1',5,36.0,0.21,118.0,2.74,92.0,1.7,53.0,1.81,166,'待可靠来源','S1参考',1,'2026-08-19T17:01:54+08:00','general:525276a9bc4a7162be8f',NULL,NULL);
INSERT INTO "generals" VALUES(92,'陆抗','https://www.sgmdtx.com/wj/陆抗/','吴',NULL,'弓',NULL,'s12',5,78.0,1.73,109.0,2.6,108.0,1.9,64.0,1.85,33,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:745dc71ccc2c607d55d4',NULL,NULL);
INSERT INTO "generals" VALUES(93,'陆逊','https://www.sgmdtx.com/wj/陆逊/','吴','金','盾',NULL,'s2',5,66.0,0.44,104.0,2.74,94.0,1.96,40.0,1.88,141,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:f88e20a568d008a29c2d',NULL,NULL);
INSERT INTO "generals" VALUES(94,'陈宫','https://www.sgmdtx.com/wj/陈宫/','群','金','盾',NULL,'s2',5,52.0,0.63,98.0,2.54,77.0,1.87,64.0,1.94,118,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:87a4a65f88e7b38b5190',NULL,NULL);
INSERT INTO "generals" VALUES(97,'颜良','https://www.sgmdtx.com/wj/颜良/','群','金','盾','兵刃','s1',5,107.0,2.4,50.0,0.76,92.0,1.69,77.0,2.56,174,'待可靠来源','Steam已核',1,'2026-08-19T17:01:54+08:00','general:f2f34af1e7f448967678',NULL,NULL);
INSERT INTO "generals" VALUES(98,'马云禄','https://www.sgmdtx.com/wj/马云禄/','蜀','金','盾',NULL,'s2',5,104.0,2.43,53.0,1.24,89.0,1.65,93.0,2.54,168,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:943b7a7b14597aba4a9f',NULL,NULL);
INSERT INTO "generals" VALUES(99,'马腾','https://www.sgmdtx.com/wj/马腾/','群',NULL,'骑',NULL,'s6',5,84.0,2.07,59.0,0.73,101.0,2.23,91.0,1.87,213,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:5eeb463fc63a880ad0d8',NULL,NULL);
INSERT INTO "generals" VALUES(100,'马超','https://www.sgmdtx.com/wj/马超/','蜀','金','盾','兵刃','s1',5,118.0,2.78,57.0,1.01,103.0,1.72,75.0,2.53,169,'待可靠来源','S1参考',1,'2026-08-19T17:01:54+08:00','general:63655267babca9c136c2',NULL,NULL);
INSERT INTO "generals" VALUES(101,'高顺','https://www.sgmdtx.com/wj/高顺/','群',NULL,'盾',NULL,'s9',5,101.0,2.12,78.0,0.75,109.0,2.21,75.0,1.74,185,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:ced9a805145ed4c2bbfb',NULL,NULL);
INSERT INTO "generals" VALUES(102,'魏延','https://www.sgmdtx.com/wj/魏延/','蜀',NULL,'盾',NULL,'s10',5,118.0,2.66,93.0,1.6,102.0,2.16,56.0,1.63,74,'待可靠来源','跨赛季参考',1,'2026-08-19T17:01:54+08:00','general:9001e293139ffd6b077e',NULL,NULL);
INSERT INTO "generals" VALUES(103,'鲁肃','https://www.sgmdtx.com/wj/鲁肃/','吴','金','盾','防御','s1',5,72.0,0.36,109.0,2.4,98.0,1.65,80.0,2.09,36,'待可靠来源','Steam已核',1,'2026-08-19T17:01:54+08:00','general:8dc0bfe19c5d81dc129c',NULL,NULL);
INSERT INTO "generals" VALUES(104,'黄忠','https://www.sgmdtx.com/wj/黄忠/','蜀','金','盾','兵刃','s1',5,115.0,2.51,71.0,1.32,101.0,1.69,58.0,2.23,75,'待可靠来源','S1参考',1,'2026-08-19T17:01:54+08:00','general:c9065395c9a7298a3331',NULL,NULL);
INSERT INTO "generals" VALUES(105,'黄月英','https://www.sgmdtx.com/wj/黄月英/','蜀','金','盾','辅助','s1',5,31.0,0.33,109.0,2.28,93.0,1.62,46.0,2.0,120,'待可靠来源','S1参考',1,'2026-08-19T17:01:54+08:00','general:979781ac090cb71634a2',NULL,NULL);
INSERT INTO "generals" VALUES(106,'黄盖','https://www.sgmdtx.com/wj/黄盖/','吴','金','盾','防御','s1',5,94.0,1.58,92.0,1.62,113.0,2.18,83.0,1.91,176,'待可靠来源','Steam已核',1,'2026-08-19T17:01:54+08:00','general:af28979bd438c204232c',NULL,NULL);
INSERT INTO "generals" VALUES(107,'杨修',NULL,'魏','紫',NULL,NULL,'s1',5,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'待可靠来源','截图已核',NULL,'2026-09-10','general:bd53b54cd679c8e506b3',NULL,NULL);
INSERT INTO "generals" VALUES(108,'刘晔',NULL,'魏','紫',NULL,NULL,'s1',5,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'待可靠来源','截图已核',NULL,'2026-09-10','general:0daa6e8c4a81107b3660',NULL,NULL);
INSERT INTO "generals" VALUES(109,'文聘',NULL,'魏','紫',NULL,NULL,'s1',5,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'待可靠来源','截图已核',NULL,'2026-09-10','general:596c893874a6a0abe9d3',NULL,NULL);
INSERT INTO "generals" VALUES(110,'曹洪',NULL,'魏','紫',NULL,NULL,'s1',5,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'待可靠来源','截图已核',NULL,'2026-09-10','general:8460abc20204db9039a8',NULL,NULL);
INSERT INTO "generals" VALUES(111,'钟繇',NULL,'魏','紫',NULL,NULL,'s1',5,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'待可靠来源','截图已核',NULL,'2026-09-10','general:22aa2627da5c33f8c48e',NULL,NULL);
INSERT INTO "generals" VALUES(112,'曹真',NULL,'魏','紫',NULL,NULL,'s1',5,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'待可靠来源','截图已核',NULL,'2026-09-10','general:603b840477e3aa4a40b8',NULL,NULL);
CREATE TABLE meta (
  key TEXT PRIMARY KEY,
  value TEXT NOT NULL
);
INSERT INTO "meta" VALUES('network_source_id','1');
INSERT INTO "meta" VALUES('default_platform','Steam');
INSERT INTO "meta" VALUES('last_sync_at','2026-08-19T17:01:54+08:00');
INSERT INTO "meta" VALUES('schema_version','4');
CREATE TABLE progression_rules (
  id INTEGER PRIMARY KEY,
  rule_key TEXT NOT NULL UNIQUE,
  formula TEXT NOT NULL,
  description TEXT NOT NULL,
  verification_status TEXT NOT NULL,
  source_id INTEGER REFERENCES sources(id)
);
INSERT INTO "progression_rules" VALUES(1,'level_stat','displayed_estimate = round(base_level5 + displayed_growth * (level - 5)) + allocated','网络基础四维为5级基准；公开成长只显示两位小数，推算裸面板可能与客户端相差1点。阈值判断优先使用general_stat_observations中的实测面板。','Steam截图交叉核验；估算值需保留±1误差',4);
INSERT INTO "progression_rules" VALUES(2,'level_free_points','10 * floor(level / 10)','武将每到10的倍数等级获得10点自由属性；50级共50点。','Steam截图与官方攻略交叉核验',5);
INSERT INTO "progression_rules" VALUES(3,'advancement_free_points','10 * advancement','武将每升一阶获得10点自由分配属性。','官方社区攻略',5);
CREATE TABLE sources (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  url TEXT NOT NULL,
  source_type TEXT NOT NULL,
  platform TEXT,
  season TEXT,
  trust_rank INTEGER NOT NULL,
  fetched_at TEXT,
  notes TEXT,
  UNIQUE(name, url)
);
INSERT INTO "sources" VALUES(1,'三谋助手资料站','https://www.sgmdtx.com','第三方结构化资料',NULL,NULL,60,'2026-08-19T17:01:54+08:00','保存基础属性、成长、自带战法、缘分与战法正文；按赛季字段过滤。');
INSERT INTO "sources" VALUES(2,'三谋助手状态词典','https://www.sgmdtx.com/buff/','第三方状态资料',NULL,NULL,65,'2026-08-19T17:01:54+08:00',NULL);
INSERT INTO "sources" VALUES(3,'雷电模拟器三谋图鉴','https://wiki.ldmnq.com/sanguo_modingtianxia/','第三方品质参考',NULL,NULL,50,'2026-08-19T17:01:54+08:00','仅补充金/紫/蓝品质和武将主定位；不覆盖Steam截图。');
INSERT INTO "sources" VALUES(4,'用户Steam S1截图','local:evidence/steam_s1/','截图','Steam','s1',100,'2026-08-19T17:01:54+08:00','按日期保存的当前账号游戏内截图；较新截图优先并覆盖网络资料。');
INSERT INTO "sources" VALUES(5,'武将系统说明','https://www.taptap.cn/moment/531478269581592397','官方社区攻略',NULL,'s1',80,'2026-08-19T17:01:54+08:00','每升一阶获得10点自由属性。');
INSERT INTO "sources" VALUES(6,'韬略重修说明','https://www.taptap.cn/moment/531462563137849323','官方社区攻略',NULL,'s1',80,'2026-08-19T17:01:54+08:00','三个韬略位、重修随机三选一、专属韬略限制与保底。');
INSERT INTO "sources" VALUES(7,'用户当前机制说明','local:conversation/2026-08-05','用户口述','Steam','s1',90,'2026-08-19T17:01:54+08:00','每名武将可查看自己的可能获得韬略列表；抽取规则未知。');
INSERT INTO "sources" VALUES(8,'用户Steam S2截图-料事如神10级','references/S2演武战报/2026-09-04/30-料事如神10级详情.png','游戏内截图','Steam','s2',100,'2026-09-10T17:37:59+08:00','演武大会10级满级战法详情');
INSERT INTO "sources" VALUES(9,'用户Steam S2截图-上智为间10级','references/S2演武战报/2026-09-04/31-上智为间10级详情.png','游戏内截图','Steam','s2',100,'2026-09-10T17:37:59+08:00','演武大会10级满级战法详情');
INSERT INTO "sources" VALUES(10,'用户Steam S2截图-束手无策10级','references/S2演武战报/2026-09-04/32-束手无策10级详情.png','游戏内截图','Steam','s2',100,'2026-09-10T17:37:59+08:00','演武大会10级满级战法详情');
INSERT INTO "sources" VALUES(11,'用户Steam S2截图-横征暴敛10级','references/S2演武战报/2026-09-04/34-横征暴敛10级详情.png','游戏内截图','Steam','s2',100,'2026-09-10T17:36:00+08:00','演武大会10级满级战法详情');
INSERT INTO "sources" VALUES(12,'用户Steam S2截图-固若金汤10级','references/S2演武战报/2026-09-04/35-固若金汤10级详情.png','游戏内截图','Steam','s2',100,'2026-09-10T17:36:00+08:00','演武大会10级满级战法详情');
INSERT INTO "sources" VALUES(13,'用户Steam S2截图-谈笑诛心10级预览','references/S2演武战报/2026-09-04/36-谈笑诛心10级预览.png','游戏内截图','Steam','s2',100,'2026-09-10T17:37:59+08:00','1级战法界面切换至10级满级预览');
INSERT INTO "sources" VALUES(14,'用户Steam S2截图-2026-09-10-烈火焚营10级','local:conversation/2026-09-10/烈火焚营','游戏内截图','Steam','s2',100,'2026-09-10T17:37:59+08:00','用户提供截图；部分为满级预览');
INSERT INTO "sources" VALUES(15,'用户Steam S2截图-2026-09-10-断敌粮道10级','local:conversation/2026-09-10/断敌粮道','游戏内截图','Steam','s2',100,'2026-09-10T17:37:59+08:00','用户提供截图；部分为满级预览');
INSERT INTO "sources" VALUES(16,'用户Steam S2截图-2026-09-10-铁骑横冲10级','local:conversation/2026-09-10/铁骑横冲','游戏内截图','Steam','s2',100,'2026-09-10T17:37:59+08:00','用户提供截图；部分为满级预览');
INSERT INTO "sources" VALUES(17,'用户Steam S2截图-2026-09-10-水淹七军10级','local:conversation/2026-09-10/水淹七军','游戏内截图','Steam','s2',100,'2026-09-10T17:37:59+08:00','用户提供截图；部分为满级预览');
INSERT INTO "sources" VALUES(18,'用户Steam S2截图-2026-09-10-威名显赫10级','local:conversation/2026-09-10/威名显赫','游戏内截图','Steam','s2',100,'2026-09-10T17:37:59+08:00','用户提供截图；部分为满级预览');
INSERT INTO "sources" VALUES(19,'用户Steam S2截图-2026-09-10-勇冠三军10级','local:conversation/2026-09-10/勇冠三军','游戏内截图','Steam','s2',100,'2026-09-10T17:37:59+08:00','用户提供截图；部分为满级预览');
INSERT INTO "sources" VALUES(20,'用户Steam S2截图-2026-09-10-胜敌益强10级','local:conversation/2026-09-10/胜敌益强','游戏内截图','Steam','s2',100,'2026-09-10T17:37:59+08:00','用户提供截图；部分为满级预览');
INSERT INTO "sources" VALUES(21,'用户Steam S2截图-2026-09-10-出其不意10级','local:conversation/2026-09-10/出其不意','游戏内截图','Steam','s2',100,'2026-09-10T17:37:59+08:00','用户提供截图；部分为满级预览');
INSERT INTO "sources" VALUES(22,'用户Steam S2截图-2026-09-10-无难之志10级','local:conversation/2026-09-10/无难之志','游戏内截图','Steam','s2',100,'2026-09-10T17:37:59+08:00','用户提供截图；部分为满级预览');
INSERT INTO "sources" VALUES(23,'用户Steam S2截图-2026-09-10-锐不可当10级','local:conversation/2026-09-10/锐不可当','游戏内截图','Steam','s2',100,'2026-09-10T17:37:59+08:00','用户提供截图；部分为满级预览');
INSERT INTO "sources" VALUES(24,'用户Steam S2截图-2026-09-10-狂风大作10级','local:conversation/2026-09-10/狂风大作','游戏内截图','Steam','s2',100,'2026-09-10T17:37:59+08:00','用户提供截图；部分为满级预览');
INSERT INTO "sources" VALUES(25,'用户Steam S2截图-2026-09-10-趁火打劫10级','local:conversation/2026-09-10/趁火打劫','游戏内截图','Steam','s2',100,'2026-09-10T17:37:59+08:00','用户提供截图；部分为满级预览');
INSERT INTO "sources" VALUES(26,'用户Steam S2截图-2026-09-10-披坚执锐10级','local:conversation/2026-09-10/披坚执锐','游戏内截图','Steam','s2',100,'2026-09-10T17:37:59+08:00','用户提供截图；部分为满级预览');
INSERT INTO "sources" VALUES(27,'用户Steam S2截图-2026-09-10-攻其不备10级','local:conversation/2026-09-10/攻其不备','游戏内截图','Steam','s2',100,'2026-09-10T17:37:59+08:00','用户提供截图；部分为满级预览');
INSERT INTO "sources" VALUES(28,'用户Steam S2截图-2026-09-10-横征暴敛10级','local:conversation/2026-09-10/横征暴敛','游戏内截图','Steam','s2',100,'2026-09-10T17:37:59+08:00','用户提供截图；部分为满级预览');
INSERT INTO "sources" VALUES(29,'用户Steam S2截图-2026-09-10-百战不殆10级','local:conversation/2026-09-10/百战不殆','游戏内截图','Steam','s2',100,'2026-09-10T17:37:59+08:00','用户提供截图；部分为满级预览');
INSERT INTO "sources" VALUES(30,'用户Steam S2截图-2026-09-10-王佐之才10级','local:conversation/2026-09-10/王佐之才','游戏内截图','Steam','s2',100,'2026-09-10T17:37:59+08:00','用户提供截图；部分为满级预览');
INSERT INTO "sources" VALUES(31,'用户Steam S2截图-2026-09-10-蓄势待发10级','local:conversation/2026-09-10/蓄势待发','游戏内截图','Steam','s2',100,'2026-09-10T17:37:59+08:00','用户提供截图；部分为满级预览');
INSERT INTO "sources" VALUES(32,'用户Steam S2截图-2026-09-10-知人善任10级','local:conversation/2026-09-10/知人善任','游戏内截图','Steam','s2',100,'2026-09-10T17:37:59+08:00','用户提供截图；部分为满级预览');
INSERT INTO "sources" VALUES(33,'用户Steam S2截图-2026-09-10-乘间投隙10级','local:conversation/2026-09-10/乘间投隙','游戏内截图','Steam','s2',100,'2026-09-10T17:37:59+08:00','用户提供截图；部分为满级预览');
INSERT INTO "sources" VALUES(34,'用户Steam S2截图-2026-09-10-韬光养晦10级','local:conversation/2026-09-10/韬光养晦','游戏内截图','Steam','s2',100,'2026-09-10T17:37:59+08:00','用户提供截图；部分为满级预览');
INSERT INTO "sources" VALUES(35,'用户Steam S2截图-2026-09-10-固若金汤10级','local:conversation/2026-09-10/固若金汤','游戏内截图','Steam','s2',100,'2026-09-10T17:37:59+08:00','用户提供截图；部分为满级预览');
INSERT INTO "sources" VALUES(36,'用户Steam S2截图-2026-09-10-万夫莫当10级','local:conversation/2026-09-10/万夫莫当','游戏内截图','Steam','s2',100,'2026-09-10T17:37:59+08:00','用户提供截图；部分为满级预览');
INSERT INTO "sources" VALUES(37,'用户Steam S2截图-2026-09-10-清风驱疾10级','local:conversation/2026-09-10/清风驱疾','游戏内截图','Steam','s2',100,'2026-09-10T17:37:59+08:00','用户提供截图；部分为满级预览');
INSERT INTO "sources" VALUES(38,'用户Steam S2截图-2026-09-10-势如破竹10级','local:conversation/2026-09-10/势如破竹','游戏内截图','Steam','s2',100,'2026-09-10T17:37:59+08:00','用户提供截图；部分为满级预览');
INSERT INTO "sources" VALUES(39,'用户Steam S2截图-2026-09-10-乘虚而入10级','local:conversation/2026-09-10/乘虚而入','游戏内截图','Steam','s2',100,'2026-09-10T17:37:59+08:00','用户提供截图；部分为满级预览');
INSERT INTO "sources" VALUES(40,'用户Steam S2截图-2026-09-10-三军夺气10级','local:conversation/2026-09-10/三军夺气','游戏内截图','Steam','s2',100,'2026-09-10T17:37:59+08:00','用户提供截图；部分为满级预览');
INSERT INTO "sources" VALUES(41,'用户Steam S2截图-2026-09-10-伏兵四起10级','local:conversation/2026-09-10/伏兵四起','游戏内截图','Steam','s2',100,'2026-09-10T17:37:59+08:00','用户提供截图；部分为满级预览');
INSERT INTO "sources" VALUES(42,'用户Steam S2截图-2026-09-10-五雷轰顶10级','local:conversation/2026-09-10/五雷轰顶','游戏内截图','Steam','s2',100,'2026-09-10T17:37:59+08:00','用户提供截图；部分为满级预览');
INSERT INTO "sources" VALUES(43,'用户Steam S2截图-2026-09-10-战八方10级','local:conversation/2026-09-10/战八方','游戏内截图','Steam','s2',100,'2026-09-10T17:37:59+08:00','用户提供截图；部分为满级预览');
INSERT INTO "sources" VALUES(44,'用户Steam S2截图-2026-09-10-破军袭敌10级','local:conversation/2026-09-10/破军袭敌','游戏内截图','Steam','s2',100,'2026-09-10T17:37:59+08:00','用户提供截图；部分为满级预览');
CREATE TABLE strategy_books (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL UNIQUE,
  quality TEXT,
  book_scope TEXT NOT NULL DEFAULT '通用',
  role_pool TEXT,
  exclusive_general_id INTEGER REFERENCES generals(id),
  acquisition_method TEXT,
  effect_raw TEXT,
  source_id INTEGER REFERENCES sources(id)
);
INSERT INTO "strategy_books" VALUES(1,'神勇','金','金色候选（归属待确认）',NULL,NULL,NULL,'自身规避率和倒戈提升5%',4);
INSERT INTO "strategy_books" VALUES(2,'作战·善本','紫','通用候选',NULL,NULL,NULL,'兵刃伤害提升6.5%',4);
INSERT INTO "strategy_books" VALUES(3,'胜战·善本','紫','通用候选',NULL,NULL,NULL,'战斗前4回合，兵刃伤害提升8%',4);
INSERT INTO "strategy_books" VALUES(4,'久战·善本','紫','通用候选',NULL,NULL,NULL,'造成兵刃伤害后，兵刃伤害提升1.8%，最多叠加5次',4);
CREATE TABLE strategy_rules (
  id INTEGER PRIMARY KEY,
  rule_key TEXT NOT NULL UNIQUE,
  rule_text TEXT NOT NULL,
  verification_status TEXT NOT NULL,
  source_id INTEGER REFERENCES sources(id)
);
INSERT INTO "strategy_rules" VALUES(1,'unlock_slots','25、30、35级分别解锁第1、2、3个韬略位。','官方社区攻略',5);
INSERT INTO "strategy_rules" VALUES(2,'refit_requires_three','三本韬略全部研读后才能开启重修。','官方社区攻略',6);
INSERT INTO "strategy_rules" VALUES(3,'refit_three_choices','每次选择一本韬略重修，该韬略随机出现3个选项，可保留重修前结果。','官方社区攻略',6);
INSERT INTO "strategy_rules" VALUES(4,'exclusive_limit','一名武将同时只能应用1个专属韬略；同一武将可能存在多个专属候选。','官方社区攻略',6);
INSERT INTO "strategy_rules" VALUES(5,'exclusive_guarantee','单将10次重修内必出专属；出过专属且仍有其他专属时，后续3次内再出专属，但可能重复。','官方社区攻略',6);
INSERT INTO "strategy_rules" VALUES(6,'candidate_list','每名武将均可查看自己的可能获得韬略列表；应按武将逐项保存候选关系。','Steam截图已核',4);
INSERT INTO "strategy_rules" VALUES(7,'draw_algorithm','候选列表如何生成、各韬略抽取权重及是否按职业共享池，目前未知。','待Steam或官方规则核验',7);
CREATE TABLE sync_runs (
  id INTEGER PRIMARY KEY,
  started_at TEXT NOT NULL,
  finished_at TEXT,
  status TEXT NOT NULL,
  generals_count INTEGER DEFAULT 0,
  tactics_count INTEGER DEFAULT 0,
  effects_count INTEGER DEFAULT 0,
  error_text TEXT
);
INSERT INTO "sync_runs" VALUES(1,'2026-08-19T17:01:54+08:00','2026-08-19T17:01:54+08:00','complete',106,231,32,NULL);
CREATE TABLE tactic_effects (
  tactic_id INTEGER NOT NULL REFERENCES tactics(id) ON DELETE CASCADE,
  effect_id INTEGER NOT NULL REFERENCES effects(id) ON DELETE CASCADE,
  relation TEXT NOT NULL DEFAULT '产生或依赖',
  evidence_text TEXT,
  PRIMARY KEY (tactic_id, effect_id, relation)
);
INSERT INTO "tactic_effects" VALUES(5,30,'产生或依赖','普攻后60%对目标两名队友造成该次普攻103%传递伤害；自身武力高于目标时额外30.9%兵刃伤害。');
INSERT INTO "tactic_effects" VALUES(8,25,'产生或依赖','使敌军随机单体混乱，持续1回合，并造成300%谋略伤害，若目标已持有混乱状态，则额外对其造成150%谋略伤害');
INSERT INTO "tactic_effects" VALUES(13,27,'产生或依赖','普攻后随机单体280%兵刃伤害；目标虚弱则伤害提升30%，否则80%施加虚弱1回合。');
INSERT INTO "tactic_effects" VALUES(14,25,'产生或依赖','普攻后对敌军随机单体混乱1回合并180%谋略伤害；若已混乱，对其友军随机单体100%谋略伤害。');
INSERT INTO "tactic_effects" VALUES(19,17,'产生或依赖','准备1回合，对敌军随机单体160%谋略伤害，施放5次；命中洪水目标该次伤害提升40%。');
INSERT INTO "tactic_effects" VALUES(25,1,'产生或依赖','对敌军随机单体110%兵刃伤害，触发4次，发动期间附带25%会心几率。');
INSERT INTO "tactic_effects" VALUES(39,1,'产生或依赖','提升自身20%会心2回合，再对敌军全体140%兵刃伤害。');
INSERT INTO "tactic_effects" VALUES(40,5,'产生或依赖','自身倒戈提升30.9%；普攻后自身兵刃伤害提升6.18%，可叠6次；累计3次普攻后随机单体206%兵刃伤害。');
INSERT INTO "tactic_effects" VALUES(53,26,'产生或依赖','自身统率提升20%；第2回合起每回合开始60%概率嘲讽敌军随机2-3人2回合。');
INSERT INTO "tactic_effects" VALUES(71,5,'产生或依赖','提升自身30%倒戈2回合；对敌军随机两人造成226.6%兵刃伤害。');
INSERT INTO "tactic_effects" VALUES(95,20,'产生或依赖','对敌军全体造成130%兵刃伤害，并施加畏惧2回合。');
INSERT INTO "tactic_effects" VALUES(106,24,'产生或依赖','普攻后对目标280%兵刃伤害并施加技穷1回合；已有技穷时50%震慑1回合。');
INSERT INTO "tactic_effects" VALUES(106,22,'产生或依赖','普攻后对目标280%兵刃伤害并施加技穷1回合；已有技穷时50%震慑1回合。');
INSERT INTO "tactic_effects" VALUES(110,24,'产生或依赖','对敌军随机两人造成180%谋略伤害，并有50%概率施加技穷，持续1回合');
INSERT INTO "tactic_effects" VALUES(113,28,'产生或依赖','回合开始对敌军单体施加断粮2回合；回合结束对其造成113.3%谋略伤害。');
INSERT INTO "tactic_effects" VALUES(115,5,'产生或依赖','提升两名队友45%连击率和20%倒戈，持续2回合。');
INSERT INTO "tactic_effects" VALUES(115,7,'产生或依赖','提升两名队友45%连击率和20%倒戈，持续2回合。');
INSERT INTO "tactic_effects" VALUES(125,24,'产生或依赖','对敌军随机单体造成200%谋略伤害，并施加技穷，持续1回合');
INSERT INTO "tactic_effects" VALUES(133,24,'产生或依赖','准备1回合，对敌军全体施加洪水2回合并造成267.8%兵刃伤害；66.95%概率施加技穷、缴械各1回合。');
INSERT INTO "tactic_effects" VALUES(133,17,'产生或依赖','准备1回合，对敌军全体施加洪水2回合并造成267.8%兵刃伤害；66.95%概率施加技穷、缴械各1回合。');
INSERT INTO "tactic_effects" VALUES(133,23,'产生或依赖','准备1回合，对敌军全体施加洪水2回合并造成267.8%兵刃伤害；66.95%概率施加技穷、缴械各1回合。');
INSERT INTO "tactic_effects" VALUES(144,18,'产生或依赖','对敌军全体造成84.8%谋略伤害，并施加火攻2回合；再3次焚营，风暴目标焚营伤害提升30%。');
INSERT INTO "tactic_effects" VALUES(144,19,'产生或依赖','对敌军全体造成84.8%谋略伤害，并施加火攻2回合；再3次焚营，风暴目标焚营伤害提升30%。');
INSERT INTO "tactic_effects" VALUES(145,19,'产生或依赖','第2、4回合开始敌我全体陷入风暴2回合；奇数回合60%全体100%谋略伤害，偶数回合60%随机单体280%谋略伤害。');
INSERT INTO "tactic_effects" VALUES(147,2,'产生或依赖','自身奇谋几率提升24%；谋略伤害后50%提升10智力2回合，可叠4次。');
INSERT INTO "tactic_effects" VALUES(157,12,'产生或依赖','我军智力最高单体受伤降低25%（受智力影响）2回合，并获1层抵御。');
INSERT INTO "tactic_effects" VALUES(194,25,'产生或依赖','准备1回合，敌军随机两人220%谋略和兵刃伤害；火攻目标额外混乱2回合。');
INSERT INTO "tactic_effects" VALUES(194,18,'产生或依赖','准备1回合，敌军随机两人220%谋略和兵刃伤害；火攻目标额外混乱2回合。');
INSERT INTO "tactic_effects" VALUES(205,1,'产生或依赖','普攻后提升自身20.6%会心2回合，再对当前目标造成412%兵刃伤害；伤害系数每回合降低25%。');
INSERT INTO "tactic_effects" VALUES(207,3,'产生或依赖','提升自身16%破甲和35%造成伤害。');
CREATE TABLE tactic_level_observations (
  id INTEGER PRIMARY KEY,
  tactic_id INTEGER NOT NULL REFERENCES tactics(id) ON DELETE CASCADE,
  level INTEGER NOT NULL,
  activation_rate TEXT,
  effect_raw TEXT NOT NULL,
  effect_json TEXT,
  observed_context TEXT,
  verification_status TEXT NOT NULL,
  source_id INTEGER REFERENCES sources(id),
  observed_at TEXT NOT NULL,
  UNIQUE(tactic_id, level, source_id, observed_context)
);
INSERT INTO "tactic_level_observations" VALUES(1,110,10,'45%','对敌军随机两人造成180%谋略伤害，并有50%概率施加技穷，持续1回合','{"targets": "敌军随机两人", "strategy_damage_rate_per_target": 180, "status": "技穷", "status_probability": 50, "status_duration_rounds": 1}','S2演武大会满级战法详情','Steam已核',8,'2026-09-04T00:00:00+08:00');
INSERT INTO "tactic_level_observations" VALUES(2,8,10,'45%','使敌军随机单体混乱，持续1回合，并造成300%谋略伤害，若目标已持有混乱状态，则额外对其造成150%谋略伤害','{"targets": "敌军随机单体", "status": "混乱", "status_duration_rounds": 1, "strategy_damage_rate": 300, "condition": "目标已持有混乱状态", "conditional_extra_strategy_damage_rate": 150}','S2演武大会满级战法详情','Steam已核',9,'2026-09-04T00:00:00+08:00');
INSERT INTO "tactic_level_observations" VALUES(3,125,10,'45%','对敌军随机单体造成200%谋略伤害，并施加技穷，持续1回合','{"targets": "敌军随机单体", "strategy_damage_rate": 200, "status": "技穷", "status_probability": 100, "status_duration_rounds": 1}','S2演武大会满级战法详情','Steam已核',10,'2026-09-04T00:00:00+08:00');
INSERT INTO "tactic_level_observations" VALUES(4,127,10,'100%','战斗中，施加负面效果后恢复自身兵力（治疗率40%，受智力和统率影响），并使自身受到伤害降低10%，持续2回合，可叠加4次。每回合最多触发10次','{"trigger": "施加负面效果后", "healing_rate": 40, "healing_affected_by": ["智力", "统率"], "self_damage_taken_reduction": 10, "duration_rounds": 2, "max_stacks": 4, "max_triggers_per_round": 10}','S2演武大会满级战法详情','Steam已核',11,'2026-09-04T00:00:00+08:00');
INSERT INTO "tactic_level_observations" VALUES(5,53,10,'100%','自身统率提升20%，第2回合起，每个回合开始时有60%概率（受统率影响）嘲讽敌军随机2-3人，持续2回合','{"self_command_increase": 20, "starts_from_round": 2, "trigger_timing": "每个回合开始时", "taunt_probability": 60, "probability_affected_by": "统率", "targets": "敌军随机2-3人", "status": "嘲讽", "status_duration_rounds": 2}','S2演武大会满级战法详情','Steam已核',12,'2026-09-04T00:00:00+08:00');
INSERT INTO "tactic_level_observations" VALUES(6,192,10,'100%','敌军被施加负面状态时，有60%概率对敌军随机单体造成119.9%谋略伤害，每回合最多触发2次','{"trigger": "敌军被施加负面状态时", "trigger_probability": 60, "targets": "敌军随机单体", "strategy_damage_rate": 119.9, "max_triggers_per_round": 2}','S2演武大会1级战法的10级满级预览','Steam已核',13,'2026-09-04T00:00:00+08:00');
INSERT INTO "tactic_level_observations" VALUES(7,144,10,NULL,'对敌军全体造成84.8%谋略伤害，并施加火攻2回合；再3次焚营，风暴目标焚营伤害提升30%。','{}','2026-09-10用户Steam S2截图10级满级效果/满级预览','Steam已核',14,'2026-09-10T00:00:00+08:00');
INSERT INTO "tactic_level_observations" VALUES(8,113,10,NULL,'回合开始对敌军单体施加断粮2回合；回合结束对其造成113.3%谋略伤害。','{}','2026-09-10用户Steam S2截图10级满级效果/满级预览','Steam已核',15,'2026-09-10T00:00:00+08:00');
INSERT INTO "tactic_level_observations" VALUES(9,205,10,NULL,'普攻后提升自身20.6%会心2回合，再对当前目标造成412%兵刃伤害；伤害系数每回合降低25%。','{}','2026-09-10用户Steam S2截图10级满级效果/满级预览','Steam已核',16,'2026-09-10T00:00:00+08:00');
INSERT INTO "tactic_level_observations" VALUES(10,133,10,NULL,'准备1回合，对敌军全体施加洪水2回合并造成267.8%兵刃伤害；66.95%概率施加技穷、缴械各1回合。','{}','2026-09-10用户Steam S2截图10级满级效果/满级预览','Steam已核',17,'2026-09-10T00:00:00+08:00');
INSERT INTO "tactic_level_observations" VALUES(11,71,10,NULL,'提升自身30%倒戈2回合；对敌军随机两人造成226.6%兵刃伤害。','{}','2026-09-10用户Steam S2截图10级满级效果/满级预览','Steam已核',18,'2026-09-10T00:00:00+08:00');
INSERT INTO "tactic_level_observations" VALUES(12,40,10,NULL,'自身倒戈提升30.9%；普攻后自身兵刃伤害提升6.18%，可叠6次；累计3次普攻后随机单体206%兵刃伤害。','{}','2026-09-10用户Steam S2截图10级满级效果/满级预览','Steam已核',19,'2026-09-10T00:00:00+08:00');
INSERT INTO "tactic_level_observations" VALUES(13,173,10,NULL,'造成兵刃伤害后提升16.48武力、造成谋略伤害后提升16.48智力，均可叠8次。','{}','2026-09-10用户Steam S2截图10级满级效果/满级预览','Steam已核',20,'2026-09-10T00:00:00+08:00');
INSERT INTO "tactic_level_observations" VALUES(14,35,10,NULL,'对敌军随机单体350%谋略伤害；目标有负面状态时伤害提升25%。','{}','2026-09-10用户Steam S2截图10级满级效果/满级预览','Steam已核',21,'2026-09-10T00:00:00+08:00');
INSERT INTO "tactic_level_observations" VALUES(15,115,10,NULL,'提升两名队友45%连击率和20%倒戈，持续2回合。','{}','2026-09-10用户Steam S2截图10级满级效果/满级预览','Steam已核',22,'2026-09-10T00:00:00+08:00');
INSERT INTO "tactic_level_observations" VALUES(16,207,10,NULL,'提升自身16%破甲和35%造成伤害。','{}','2026-09-10用户Steam S2截图10级满级效果/满级预览','Steam已核',23,'2026-09-10T00:00:00+08:00');
INSERT INTO "tactic_level_observations" VALUES(17,145,10,NULL,'第2、4回合开始敌我全体陷入风暴2回合；奇数回合60%全体100%谋略伤害，偶数回合60%随机单体280%谋略伤害。','{}','2026-09-10用户Steam S2截图10级满级效果/满级预览','Steam已核',24,'2026-09-10T00:00:00+08:00');
INSERT INTO "tactic_level_observations" VALUES(18,194,10,NULL,'准备1回合，敌军随机两人220%谋略和兵刃伤害；火攻目标额外混乱2回合。','{}','2026-09-10用户Steam S2截图10级满级效果/满级预览','Steam已核',25,'2026-09-10T00:00:00+08:00');
INSERT INTO "tactic_level_observations" VALUES(19,98,10,NULL,'战斗开始使我军随机单体获得披坚并受兵刃伤害降低20%；武力最高单体获执锐，普攻后50%随机单体100%兵刃伤害。','{}','2026-09-10用户Steam S2截图10级满级效果/满级预览','Steam已核',26,'2026-09-10T00:00:00+08:00');
INSERT INTO "tactic_level_observations" VALUES(20,106,10,NULL,'普攻后对目标280%兵刃伤害并施加技穷1回合；已有技穷时50%震慑1回合。','{}','2026-09-10用户Steam S2截图10级满级效果/满级预览','Steam已核',27,'2026-09-10T00:00:00+08:00');
INSERT INTO "tactic_level_observations" VALUES(21,127,10,NULL,'施加负面效果后治疗率40%恢复自身兵力并受伤降低10%，持续2回合、可叠4次。','{}','2026-09-10用户Steam S2截图10级满级效果/满级预览','Steam已核',28,'2026-09-10T00:00:00+08:00');
INSERT INTO "tactic_level_observations" VALUES(22,150,10,NULL,'我军统率/智力/武力最高单体受伤时60%对应提升7点属性，可叠8次至战斗结束。','{}','2026-09-10用户Steam S2截图10级满级效果/满级预览','Steam已核',29,'2026-09-10T00:00:00+08:00');
INSERT INTO "tactic_level_observations" VALUES(23,147,10,NULL,'自身奇谋几率提升24%；谋略伤害后50%提升10智力2回合，可叠4次。','{}','2026-09-10用户Steam S2截图10级满级效果/满级预览','Steam已核',30,'2026-09-10T00:00:00+08:00');
INSERT INTO "tactic_level_observations" VALUES(24,180,10,NULL,'每回合开始提升两名队友7%造成伤害，可叠加至战斗结束。','{}','2026-09-10用户Steam S2截图10级满级效果/满级预览','Steam已核',31,'2026-09-10T00:00:00+08:00');
INSERT INTO "tactic_level_observations" VALUES(25,157,10,NULL,'我军智力最高单体受伤降低25%（受智力影响）2回合，并获1层抵御。','{}','2026-09-10用户Steam S2截图10级满级效果/满级预览','Steam已核',32,'2026-09-10T00:00:00+08:00');
INSERT INTO "tactic_level_observations" VALUES(26,14,10,NULL,'普攻后对敌军随机单体混乱1回合并180%谋略伤害；若已混乱，对其友军随机单体100%谋略伤害。','{}','2026-09-10用户Steam S2截图10级满级效果/满级预览','Steam已核',33,'2026-09-10T00:00:00+08:00');
INSERT INTO "tactic_level_observations" VALUES(27,215,10,NULL,'自身主动战法发动率提升6%（受智力影响）；每回合开始自身谋略伤害提升8%，可叠加至结束。','{}','2026-09-10用户Steam S2截图10级满级效果/满级预览','Steam已核',34,'2026-09-10T00:00:00+08:00');
INSERT INTO "tactic_level_observations" VALUES(28,53,10,NULL,'自身统率提升20%；第2回合起每回合开始60%概率嘲讽敌军随机2-3人2回合。','{}','2026-09-10用户Steam S2截图10级满级效果/满级预览','Steam已核',35,'2026-09-10T00:00:00+08:00');
INSERT INTO "tactic_level_observations" VALUES(29,5,10,NULL,'普攻后60%对目标两名队友造成该次普攻103%传递伤害；自身武力高于目标时额外30.9%兵刃伤害。','{}','2026-09-10用户Steam S2截图10级满级效果/满级预览','Steam已核',36,'2026-09-10T00:00:00+08:00');
INSERT INTO "tactic_level_observations" VALUES(30,138,10,NULL,'驱散我军随机两人1种负面状态，并治疗率180%恢复兵力。','{}','2026-09-10用户Steam S2截图10级满级效果/满级预览','Steam已核',37,'2026-09-10T00:00:00+08:00');
INSERT INTO "tactic_level_observations" VALUES(31,39,10,NULL,'提升自身20%会心2回合，再对敌军全体140%兵刃伤害。','{}','2026-09-10用户Steam S2截图10级满级效果/满级预览','Steam已核',38,'2026-09-10T00:00:00+08:00');
INSERT INTO "tactic_level_observations" VALUES(32,13,10,NULL,'普攻后随机单体280%兵刃伤害；目标虚弱则伤害提升30%，否则80%施加虚弱1回合。','{}','2026-09-10用户Steam S2截图10级满级效果/满级预览','Steam已核',39,'2026-09-10T00:00:00+08:00');
INSERT INTO "tactic_level_observations" VALUES(33,6,10,NULL,'普攻后使目标武力、智力、统率降低30点3回合，最多叠5次。','{}','2026-09-10用户Steam S2截图10级满级效果/满级预览','Steam已核',40,'2026-09-10T00:00:00+08:00');
INSERT INTO "tactic_level_observations" VALUES(34,25,10,NULL,'对敌军随机单体110%兵刃伤害，触发4次，发动期间附带25%会心几率。','{}','2026-09-10用户Steam S2截图10级满级效果/满级预览','Steam已核',41,'2026-09-10T00:00:00+08:00');
INSERT INTO "tactic_level_observations" VALUES(35,19,10,NULL,'准备1回合，对敌军随机单体160%谋略伤害，施放5次；命中洪水目标该次伤害提升40%。','{}','2026-09-10用户Steam S2截图10级满级效果/满级预览','Steam已核',42,'2026-09-10T00:00:00+08:00');
INSERT INTO "tactic_level_observations" VALUES(36,95,10,NULL,'对敌军全体造成130%兵刃伤害，并施加畏惧2回合。','{}','2026-09-10用户Steam S2截图10级满级效果/满级预览','Steam已核',43,'2026-09-10T00:00:00+08:00');
INSERT INTO "tactic_level_observations" VALUES(37,158,10,NULL,'准备1回合，对敌军全体造成300%兵刃伤害。','{}','2026-09-10用户Steam S2截图10级满级效果/满级预览','Steam已核',44,'2026-09-10T00:00:00+08:00');
CREATE TABLE tactics (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL UNIQUE,
  url TEXT,
  quality TEXT,
  tactic_type TEXT,
  damage_type TEXT,
  activation_rate TEXT,
  troop_limit TEXT,
  is_self_tactic INTEGER NOT NULL DEFAULT 0,
  description_raw TEXT,
  first_season TEXT,
  verification_status TEXT NOT NULL DEFAULT 'S1参考',
  source_id INTEGER REFERENCES sources(id),
  updated_at TEXT NOT NULL
, description_level INTEGER CHECK(description_level=10), entity_id TEXT, applicable_seasons TEXT, platform TEXT);
INSERT INTO "tactics" VALUES(1,'一计决胜','https://www.sgmdtx.com/zf/一计决胜/','紫','主动','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','Steam已核',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:e1ed9b33be13ad5d3a06',NULL,NULL);
INSERT INTO "tactics" VALUES(2,'七进七出','https://www.sgmdtx.com/zf/七进七出/',NULL,'被动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:a8640b2da2ae2a09a57f',NULL,NULL);
INSERT INTO "tactics" VALUES(3,'万人之敌','https://www.sgmdtx.com/zf/万人之敌/',NULL,'主动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:eff9cc39398af8fb80f3',NULL,NULL);
INSERT INTO "tactics" VALUES(4,'万军辟易','https://www.sgmdtx.com/zf/万军辟易/',NULL,'追击','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:3a91b8121dfb0b5745d7',NULL,NULL);
INSERT INTO "tactics" VALUES(5,'万夫莫当','https://www.sgmdtx.com/zf/万夫莫当/','金','被动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',0,'普攻后60%对目标两名队友造成该次普攻103%传递伤害；自身武力高于目标时额外30.9%兵刃伤害。','s1','Steam已核',36,'2026-09-10T17:37:59+08:00',10,'tactic:faf52c6b522d5bdb2f91',NULL,NULL);
INSERT INTO "tactics" VALUES(6,'三军夺气','https://www.sgmdtx.com/zf/三军夺气/','金','追击','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',0,'普攻后使目标武力、智力、统率降低30点3回合，最多叠5次。','s2','Steam已核',40,'2026-09-10T17:37:59+08:00',10,'tactic:68bb4cc72dffe0f53dd2',NULL,NULL);
INSERT INTO "tactics" VALUES(7,'上兵伐谋','https://www.sgmdtx.com/zf/上兵伐谋/','紫','指挥','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','Steam已核',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:86e16d1572182950b52b',NULL,NULL);
INSERT INTO "tactics" VALUES(8,'上智为间','https://www.sgmdtx.com/zf/上智为间/','金','主动','谋略','45%','盾兵、弓兵、长枪兵、骑兵',0,'使敌军随机单体混乱，持续1回合，并造成300%谋略伤害，若目标已持有混乱状态，则额外对其造成150%谋略伤害','s1','Steam已核',9,'2026-09-10T17:37:59+08:00',10,'tactic:062052d6226cb87de367',NULL,NULL);
INSERT INTO "tactics" VALUES(9,'不屈意志','https://www.sgmdtx.com/zf/不屈意志/',NULL,'被动','防御',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:f0a0a3763094adee4560',NULL,NULL);
INSERT INTO "tactics" VALUES(10,'临危勇烈','https://www.sgmdtx.com/zf/临危勇烈/','紫','被动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','Steam已核',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:512627950c6846c27984',NULL,NULL);
INSERT INTO "tactics" VALUES(11,'临机制胜','https://www.sgmdtx.com/zf/临机制胜/',NULL,'指挥','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:26898f87a110d6840900',NULL,NULL);
INSERT INTO "tactics" VALUES(12,'临阵突袭','https://www.sgmdtx.com/zf/临阵突袭/','紫','追击','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','Steam已核',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:9090d66942f323653183',NULL,NULL);
INSERT INTO "tactics" VALUES(13,'乘虚而入','https://www.sgmdtx.com/zf/乘虚而入/','金','追击','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',0,'普攻后随机单体280%兵刃伤害；目标虚弱则伤害提升30%，否则80%施加虚弱1回合。','s1','Steam已核',39,'2026-09-10T17:37:59+08:00',10,'tactic:3ffa580e6e0c122ceeda',NULL,NULL);
INSERT INTO "tactics" VALUES(14,'乘间投隙','https://www.sgmdtx.com/zf/乘间投隙/','金','追击','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',0,'普攻后对敌军随机单体混乱1回合并180%谋略伤害；若已混乱，对其友军随机单体100%谋略伤害。','s2','Steam已核',33,'2026-09-10T17:37:59+08:00',10,'tactic:07aab51174594384ce88',NULL,NULL);
INSERT INTO "tactics" VALUES(15,'九伐中原','https://www.sgmdtx.com/zf/九伐中原/',NULL,'指挥','文武',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:7d55d10a615fd93c190e',NULL,NULL);
INSERT INTO "tactics" VALUES(16,'乱世奸雄','https://www.sgmdtx.com/zf/乱世奸雄/',NULL,'指挥','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:0da02b61e0c8c8ec13b5',NULL,NULL);
INSERT INTO "tactics" VALUES(17,'乱敌方阵','https://www.sgmdtx.com/zf/乱敌方阵/','紫','追击','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','Steam已核',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:a8616adfb429c29db6b2',NULL,NULL);
INSERT INTO "tactics" VALUES(18,'云行雨施','https://www.sgmdtx.com/zf/云行雨施/',NULL,'指挥','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:22772f25c39ce693e013',NULL,NULL);
INSERT INTO "tactics" VALUES(19,'五雷轰顶','https://www.sgmdtx.com/zf/五雷轰顶/','金','主动','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',0,'准备1回合，对敌军随机单体160%谋略伤害，施放5次；命中洪水目标该次伤害提升40%。','s1','Steam已核',42,'2026-09-10T17:37:59+08:00',10,'tactic:4f37cca376b8b2bc4c66',NULL,NULL);
INSERT INTO "tactics" VALUES(20,'交锋震威','https://www.sgmdtx.com/zf/交锋震威/',NULL,'追击','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:5284a62d20df0b0d8926',NULL,NULL);
INSERT INTO "tactics" VALUES(21,'以战养战','https://www.sgmdtx.com/zf/以战养战/','紫','被动','治疗',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','Steam已核',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:a231dcaa1e494847d92f',NULL,NULL);
INSERT INTO "tactics" VALUES(22,'以静制动','https://www.sgmdtx.com/zf/以静制动/','金','被动','防御',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:0e805dafe4ac6dced483',NULL,NULL);
INSERT INTO "tactics" VALUES(23,'任人唯贤','https://www.sgmdtx.com/zf/任人唯贤/','紫','主动','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s2','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:0311b14b82c6442df693',NULL,NULL);
INSERT INTO "tactics" VALUES(24,'任人择势','https://www.sgmdtx.com/zf/任人择势/','金','指挥','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:5fef69da4e08a7c1acf1',NULL,NULL);
INSERT INTO "tactics" VALUES(25,'伏兵四起','https://www.sgmdtx.com/zf/伏兵四起/','金','主动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',0,'对敌军随机单体110%兵刃伤害，触发4次，发动期间附带25%会心几率。','s1','Steam已核',41,'2026-09-10T17:37:59+08:00',10,'tactic:67009355fa355be9ba84',NULL,NULL);
INSERT INTO "tactics" VALUES(26,'僭号天子','https://www.sgmdtx.com/zf/僭号天子/',NULL,'指挥','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:eed31ddb373b7964c2db',NULL,NULL);
INSERT INTO "tactics" VALUES(27,'克敌如风','https://www.sgmdtx.com/zf/克敌如风/','紫','主动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','Steam已核',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:ec85c924a04920096a5d',NULL,NULL);
INSERT INTO "tactics" VALUES(28,'八虎雄首','https://www.sgmdtx.com/zf/八虎雄首/',NULL,'主动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:f3e89b85bebdd5e68e6f',NULL,NULL);
INSERT INTO "tactics" VALUES(29,'兴王定霸','https://www.sgmdtx.com/zf/兴王定霸/',NULL,'指挥','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:9891d3403eca3935b46f',NULL,NULL);
INSERT INTO "tactics" VALUES(30,'兵动若神','https://www.sgmdtx.com/zf/兵动若神/',NULL,'指挥','防御',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:1e65696a036b194f36b7',NULL,NULL);
INSERT INTO "tactics" VALUES(31,'兵贵神速','https://www.sgmdtx.com/zf/兵贵神速/','金','追击','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:f217f263c5141babbde8',NULL,NULL);
INSERT INTO "tactics" VALUES(32,'冲锐巧变','https://www.sgmdtx.com/zf/冲锐巧变/',NULL,'主动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:0025389ce687140e94cb',NULL,NULL);
INSERT INTO "tactics" VALUES(33,'决堰倾涛','https://www.sgmdtx.com/zf/决堰倾涛/',NULL,'指挥','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:ceaac53e7c49d32f0e8e',NULL,NULL);
INSERT INTO "tactics" VALUES(34,'决水破敌','https://www.sgmdtx.com/zf/决水破敌/','紫','主动','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','Steam已核',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:cb8cc13dc9eaed066ee7',NULL,NULL);
INSERT INTO "tactics" VALUES(35,'出其不意','https://www.sgmdtx.com/zf/出其不意/','金','主动','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',0,'对敌军随机单体350%谋略伤害；目标有负面状态时伤害提升25%。','s1','Steam已核',21,'2026-09-10T17:37:59+08:00',10,'tactic:a608c3a5e036b6527224',NULL,NULL);
INSERT INTO "tactics" VALUES(36,'划湘分荆','https://www.sgmdtx.com/zf/划湘分荆/',NULL,'主动','防御',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:b4396c15e973f5030acc',NULL,NULL);
INSERT INTO "tactics" VALUES(37,'刚烈','https://www.sgmdtx.com/zf/刚烈/',NULL,'被动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:faeffa408f0f700ae6b6',NULL,NULL);
INSERT INTO "tactics" VALUES(38,'制霸江东','https://www.sgmdtx.com/zf/制霸江东/',NULL,'主动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:32ac58689784e8c29c6c',NULL,NULL);
INSERT INTO "tactics" VALUES(39,'势如破竹','https://www.sgmdtx.com/zf/势如破竹/','金','主动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',0,'提升自身20%会心2回合，再对敌军全体140%兵刃伤害。','s1','Steam已核',38,'2026-09-10T17:37:59+08:00',10,'tactic:727f580d200e0d7b0707',NULL,NULL);
INSERT INTO "tactics" VALUES(40,'勇冠三军','https://www.sgmdtx.com/zf/勇冠三军/','金','被动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',0,'自身倒戈提升30.9%；普攻后自身兵刃伤害提升6.18%，可叠6次；累计3次普攻后随机单体206%兵刃伤害。','s1','Steam已核',19,'2026-09-10T17:37:59+08:00',10,'tactic:9208631e88171e5b0977',NULL,NULL);
INSERT INTO "tactics" VALUES(41,'勇冠贲育','https://www.sgmdtx.com/zf/勇冠贲育/',NULL,'主动','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:a5128942e86412a27356',NULL,NULL);
INSERT INTO "tactics" VALUES(42,'十二奇策','https://www.sgmdtx.com/zf/十二奇策/',NULL,'主动','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:3fb1e6e9d56208e9d7d1',NULL,NULL);
INSERT INTO "tactics" VALUES(43,'十面埋伏','https://www.sgmdtx.com/zf/十面埋伏/',NULL,'主动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:3e7e88b5306cfa4598ce',NULL,NULL);
INSERT INTO "tactics" VALUES(44,'千机重城','https://www.sgmdtx.com/zf/千机重城/',NULL,'指挥','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:10be212a8b556a158b92',NULL,NULL);
INSERT INTO "tactics" VALUES(45,'千里突袭','https://www.sgmdtx.com/zf/千里突袭/','金','追击','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:57fb8219ac298ebfa8fd',NULL,NULL);
INSERT INTO "tactics" VALUES(46,'南疆烈刃','https://www.sgmdtx.com/zf/南疆烈刃/',NULL,'被动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:42c5498eae61a8892bbc',NULL,NULL);
INSERT INTO "tactics" VALUES(47,'及锋而试','https://www.sgmdtx.com/zf/及锋而试/',NULL,'主动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:7605f833d013035a0b4e',NULL,NULL);
INSERT INTO "tactics" VALUES(48,'古之恶来','https://www.sgmdtx.com/zf/古之恶来/',NULL,'被动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:3bdcc8a776b965de5b42',NULL,NULL);
INSERT INTO "tactics" VALUES(49,'合聚群雄','https://www.sgmdtx.com/zf/合聚群雄/',NULL,'指挥','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:af5b13adfc211914bc6b',NULL,NULL);
INSERT INTO "tactics" VALUES(50,'同舟共济','https://www.sgmdtx.com/zf/同舟共济/',NULL,'指挥','治疗',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:23903c69f61ad201ad47',NULL,NULL);
INSERT INTO "tactics" VALUES(51,'咏歌尝酒','https://www.sgmdtx.com/zf/咏歌尝酒/','紫','主动','治疗',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','Steam已核',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:defce723039bb48c8a5f',NULL,NULL);
INSERT INTO "tactics" VALUES(52,'围师必阙','https://www.sgmdtx.com/zf/围师必阙/',NULL,'主动','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:1950a40b5444d20d1e06',NULL,NULL);
INSERT INTO "tactics" VALUES(53,'固若金汤','https://www.sgmdtx.com/zf/固若金汤/','金','指挥','防御',NULL,'盾兵、弓兵、长枪兵、骑兵',0,'自身统率提升20%；第2回合起每回合开始60%概率嘲讽敌军随机2-3人2回合。','s2','Steam已核',35,'2026-09-10T17:37:59+08:00',10,'tactic:343749cab32d242b4147',NULL,NULL);
INSERT INTO "tactics" VALUES(54,'固镇襄樊','https://www.sgmdtx.com/zf/固镇襄樊/',NULL,'指挥','防御',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:532ecee7751c9982d10a',NULL,NULL);
INSERT INTO "tactics" VALUES(55,'国色','https://www.sgmdtx.com/zf/国色/',NULL,'指挥','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:c4dfeba590f054f29928',NULL,NULL);
INSERT INTO "tactics" VALUES(56,'坚壁清野','https://www.sgmdtx.com/zf/坚壁清野/','紫','主动','防御',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','Steam已核',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:2719eef84e7b80a5e50d',NULL,NULL);
INSERT INTO "tactics" VALUES(57,'坚如磐石','https://www.sgmdtx.com/zf/坚如磐石/','金','主动','防御',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:95090d923b3857ceac8f',NULL,NULL);
INSERT INTO "tactics" VALUES(58,'夜袭','https://www.sgmdtx.com/zf/夜袭/','紫','追击','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','Steam已核',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:fcb0db6a018ed3fddca6',NULL,NULL);
INSERT INTO "tactics" VALUES(59,'大破街亭','https://www.sgmdtx.com/zf/大破街亭/',NULL,'主动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:5062c51ad2fb613a82c8',NULL,NULL);
INSERT INTO "tactics" VALUES(60,'天下骁锐','https://www.sgmdtx.com/zf/天下骁锐/',NULL,'指挥','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:54b8dbfa282d26753a20',NULL,NULL);
INSERT INTO "tactics" VALUES(61,'天香','https://www.sgmdtx.com/zf/天香/',NULL,'主动','治疗',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:73cf3b5b3043f61ea88b',NULL,NULL);
INSERT INTO "tactics" VALUES(62,'太平余响','https://www.sgmdtx.com/zf/太平余响/',NULL,'指挥','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:4e8a602f589437aabdae',NULL,NULL);
INSERT INTO "tactics" VALUES(63,'奇正相生','https://www.sgmdtx.com/zf/奇正相生/',NULL,'指挥','治疗',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:789a1412ef5a010da75e',NULL,NULL);
INSERT INTO "tactics" VALUES(64,'奇计迭出','https://www.sgmdtx.com/zf/奇计迭出/','紫','追击','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','Steam已核',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:a06112ea7e9e80a55bfd',NULL,NULL);
INSERT INTO "tactics" VALUES(65,'奇门遁甲','https://www.sgmdtx.com/zf/奇门遁甲/','金','主动','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:b123e1f04311f204a94b',NULL,NULL);
INSERT INTO "tactics" VALUES(66,'奋勇当先','https://www.sgmdtx.com/zf/奋勇当先/',NULL,'追击','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:f63b1fa818477f8c5bea',NULL,NULL);
INSERT INTO "tactics" VALUES(67,'如有神助','https://www.sgmdtx.com/zf/如有神助/','紫','被动','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','Steam已核',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:f4a01e444d61aebe28ce',NULL,NULL);
INSERT INTO "tactics" VALUES(68,'如沐春风','https://www.sgmdtx.com/zf/如沐春风/','紫','被动','治疗',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','Steam已核',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:190177d3e064c3489a5f',NULL,NULL);
INSERT INTO "tactics" VALUES(69,'妖武','https://www.sgmdtx.com/zf/妖武/',NULL,'主动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:806f1bea230b9f7aad85',NULL,NULL);
INSERT INTO "tactics" VALUES(70,'妖风大作','https://www.sgmdtx.com/zf/妖风大作/',NULL,'主动','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:af0400cfb477f4e3f8f9',NULL,NULL);
INSERT INTO "tactics" VALUES(71,'威名显赫','https://www.sgmdtx.com/zf/威名显赫/','金','主动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',0,'提升自身30%倒戈2回合；对敌军随机两人造成226.6%兵刃伤害。','s1','Steam已核',18,'2026-09-10T17:37:59+08:00',10,'tactic:379f54a5ed6f5ba3c80f',NULL,NULL);
INSERT INTO "tactics" VALUES(72,'威震华夏','https://www.sgmdtx.com/zf/威震华夏/',NULL,'主动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:28e8cb7ce49a30f7488b',NULL,NULL);
INSERT INTO "tactics" VALUES(73,'威震塞外','https://www.sgmdtx.com/zf/威震塞外/',NULL,'追击','文武',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:f56e2c4869ca0f1e3487',NULL,NULL);
INSERT INTO "tactics" VALUES(74,'子午奇谋','https://www.sgmdtx.com/zf/子午奇谋/',NULL,'指挥','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:6ab2067a59c1c7abe3e0',NULL,NULL);
INSERT INTO "tactics" VALUES(75,'定军扬威','https://www.sgmdtx.com/zf/定军扬威/',NULL,'追击','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:7abee37b3007fa0a4009',NULL,NULL);
INSERT INTO "tactics" VALUES(76,'屈人之兵','https://www.sgmdtx.com/zf/屈人之兵/','紫','主动','防御',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','Steam已核',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:ebeea4078b5583710261',NULL,NULL);
INSERT INTO "tactics" VALUES(77,'屯田令','https://www.sgmdtx.com/zf/屯田令/',NULL,'指挥','治疗',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:e00ff7430a14bdea255e',NULL,NULL);
INSERT INTO "tactics" VALUES(78,'岿然不动','https://www.sgmdtx.com/zf/岿然不动/',NULL,'指挥','防御',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:848e85ac9d6baf725032',NULL,NULL);
INSERT INTO "tactics" VALUES(79,'巧利天灾','https://www.sgmdtx.com/zf/巧利天灾/','金','主动','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:fdaa5a5e9b9ed860aa25',NULL,NULL);
INSERT INTO "tactics" VALUES(80,'巧策引锋','https://www.sgmdtx.com/zf/巧策引锋/',NULL,'被动','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:6dbfd7b9d05ece3efac4',NULL,NULL);
INSERT INTO "tactics" VALUES(81,'平乱定叛','https://www.sgmdtx.com/zf/平乱定叛/',NULL,'指挥','防御',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:4b2ed8ce04c917dec6b5',NULL,NULL);
INSERT INTO "tactics" VALUES(82,'建计举人','https://www.sgmdtx.com/zf/建计举人/',NULL,'指挥','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:8184d89c1742b3399ae8',NULL,NULL);
INSERT INTO "tactics" VALUES(83,'弓腰姬','https://www.sgmdtx.com/zf/弓腰姬/',NULL,'追击','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:0475f8f709a8935bd4d1',NULL,NULL);
INSERT INTO "tactics" VALUES(84,'弦无虛发','https://www.sgmdtx.com/zf/弦无虛发/',NULL,'被动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:a0a46cde6126fb40fecb',NULL,NULL);
INSERT INTO "tactics" VALUES(85,'强袭','https://www.sgmdtx.com/zf/强袭/','紫','被动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','Steam已核',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:6b6d72bdbf77ba61b7de',NULL,NULL);
INSERT INTO "tactics" VALUES(86,'御敌临前','https://www.sgmdtx.com/zf/御敌临前/',NULL,'主动','防御',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:3aa9b43ff1830c49055e',NULL,NULL);
INSERT INTO "tactics" VALUES(87,'忘私相助','https://www.sgmdtx.com/zf/忘私相助/','金','被动','治疗',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:08ea3238229b37e68042',NULL,NULL);
INSERT INTO "tactics" VALUES(88,'忠烈勇武','https://www.sgmdtx.com/zf/忠烈勇武/',NULL,'被动','防御',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:dcee8b217f049b25dc2b',NULL,NULL);
INSERT INTO "tactics" VALUES(89,'恃勇克敌','https://www.sgmdtx.com/zf/恃勇克敌/',NULL,'追击','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:d3cf8fc71b6742a30f28',NULL,NULL);
INSERT INTO "tactics" VALUES(90,'恩威并行','https://www.sgmdtx.com/zf/恩威并行/',NULL,'指挥','防御',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:8d7b0d286fb0e12c0993',NULL,NULL);
INSERT INTO "tactics" VALUES(91,'悍战无畏','https://www.sgmdtx.com/zf/悍战无畏/',NULL,'主动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:2d848ec4c12a9e58426f',NULL,NULL);
INSERT INTO "tactics" VALUES(92,'悲愤诗','https://www.sgmdtx.com/zf/悲愤诗/',NULL,'主动','治疗',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:b669481c9f89ce0a2cce',NULL,NULL);
INSERT INTO "tactics" VALUES(93,'惩前毖后','https://www.sgmdtx.com/zf/惩前毖后/',NULL,'指挥','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:3cbf003f5a9678abc47f',NULL,NULL);
INSERT INTO "tactics" VALUES(94,'慎思笃行','https://www.sgmdtx.com/zf/慎思笃行/',NULL,'指挥','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:44a5796b6c49c4d4cee1',NULL,NULL);
INSERT INTO "tactics" VALUES(95,'战八方','https://www.sgmdtx.com/zf/战八方/','金','主动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',0,'对敌军全体造成130%兵刃伤害，并施加畏惧2回合。','s1','Steam已核',43,'2026-09-10T17:37:59+08:00',10,'tactic:6484094ddf7e23ccd003',NULL,NULL);
INSERT INTO "tactics" VALUES(96,'折冲御侮','https://www.sgmdtx.com/zf/折冲御侮/',NULL,'指挥','防御',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:14dfb8e6574492c0e05a',NULL,NULL);
INSERT INTO "tactics" VALUES(97,'折节学问','https://www.sgmdtx.com/zf/折节学问/',NULL,'主动','文武',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:a090f051d7dd652bd54d',NULL,NULL);
INSERT INTO "tactics" VALUES(98,'披坚执锐','https://www.sgmdtx.com/zf/披坚执锐/','金','指挥','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',0,'战斗开始使我军随机单体获得披坚并受兵刃伤害降低20%；武力最高单体获执锐，普攻后50%随机单体100%兵刃伤害。','s1','Steam已核',26,'2026-09-10T17:37:59+08:00',10,'tactic:ce7505e773f930a6fb3e',NULL,NULL);
INSERT INTO "tactics" VALUES(99,'持军毅重','https://www.sgmdtx.com/zf/持军毅重/',NULL,'被动','防御',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:194f38c5990aac42cfe0',NULL,NULL);
INSERT INTO "tactics" VALUES(100,'指点乾坤','https://www.sgmdtx.com/zf/指点乾坤/','金','主动','文武',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:41a965ac27196665294c',NULL,NULL);
INSERT INTO "tactics" VALUES(101,'挫锐折锋','https://www.sgmdtx.com/zf/挫锐折锋/',NULL,'指挥','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:e138d8975dde0ed99f65',NULL,NULL);
INSERT INTO "tactics" VALUES(102,'掠阵破军','https://www.sgmdtx.com/zf/掠阵破军/',NULL,'被动','文武',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:05716e26463cc37506af',NULL,NULL);
INSERT INTO "tactics" VALUES(103,'揭竿而起','https://www.sgmdtx.com/zf/揭竿而起/','紫','主动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','Steam已核',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:33709403c93fc96ec553',NULL,NULL);
INSERT INTO "tactics" VALUES(104,'携民渡江','https://www.sgmdtx.com/zf/携民渡江/',NULL,'指挥','治疗',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:d336340d6a12615c6aa3',NULL,NULL);
INSERT INTO "tactics" VALUES(105,'摧坚克难','https://www.sgmdtx.com/zf/摧坚克难/',NULL,'被动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:f15358a92b7318ab3014',NULL,NULL);
INSERT INTO "tactics" VALUES(106,'攻其不备','https://www.sgmdtx.com/zf/攻其不备/','金','追击','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',0,'普攻后对目标280%兵刃伤害并施加技穷1回合；已有技穷时50%震慑1回合。','s1','Steam已核',27,'2026-09-10T17:37:59+08:00',10,'tactic:63c0f875b84aefef8bc4',NULL,NULL);
INSERT INTO "tactics" VALUES(107,'文武双全','https://www.sgmdtx.com/zf/文武双全/','金','主动','文武',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:1d43e8aca6fd102380f4',NULL,NULL);
INSERT INTO "tactics" VALUES(108,'文治武功','https://www.sgmdtx.com/zf/文治武功/','紫','指挥','文武',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','Steam已核',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:c642061609192c177882',NULL,NULL);
INSERT INTO "tactics" VALUES(109,'文韬武略','https://www.sgmdtx.com/zf/文韬武略/',NULL,'追击','文武',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:8b04f76581a7a7612f72',NULL,NULL);
INSERT INTO "tactics" VALUES(110,'料事如神','https://www.sgmdtx.com/zf/料事如神/','金','主动','谋略','45%','盾兵、弓兵、长枪兵、骑兵',0,'对敌军随机两人造成180%谋略伤害，并有50%概率施加技穷，持续1回合','s1','Steam已核',8,'2026-09-10T17:37:59+08:00',10,'tactic:60268bfc2722a6dadd14',NULL,NULL);
INSERT INTO "tactics" VALUES(111,'斩将夺旗','https://www.sgmdtx.com/zf/斩将夺旗/','金','主动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:6f0c3d95d2cd10f37776',NULL,NULL);
INSERT INTO "tactics" VALUES(112,'断戈夺锋','https://www.sgmdtx.com/zf/断戈夺锋/',NULL,'主动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:83a114f4241d09d165e5',NULL,NULL);
INSERT INTO "tactics" VALUES(113,'断敌粮道','https://www.sgmdtx.com/zf/断敌粮道/','金','指挥','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',0,'回合开始对敌军单体施加断粮2回合；回合结束对其造成113.3%谋略伤害。','s1','Steam已核',15,'2026-09-10T17:37:59+08:00',10,'tactic:e87a6add52ed58080f91',NULL,NULL);
INSERT INTO "tactics" VALUES(114,'旋略勇进','https://www.sgmdtx.com/zf/旋略勇进/',NULL,'追击','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:0c4544fa5e7616982127',NULL,NULL);
INSERT INTO "tactics" VALUES(115,'无难之志','https://www.sgmdtx.com/zf/无难之志/','金','主动','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',0,'提升两名队友45%连击率和20%倒戈，持续2回合。','s1','Steam已核',22,'2026-09-10T17:37:59+08:00',10,'tactic:059b15da21f1da5251fe',NULL,NULL);
INSERT INTO "tactics" VALUES(116,'明其虚实','https://www.sgmdtx.com/zf/明其虚实/',NULL,'主动','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:d2e3f3f5ccb0377c11ae',NULL,NULL);
INSERT INTO "tactics" VALUES(117,'星罗棋布','https://www.sgmdtx.com/zf/星罗棋布/',NULL,'指挥','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:1d8dc79d9c3307519105',NULL,NULL);
INSERT INTO "tactics" VALUES(118,'智令从计','https://www.sgmdtx.com/zf/智令从计/',NULL,'指挥','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:76614917a7d7eb3c364a',NULL,NULL);
INSERT INTO "tactics" VALUES(119,'智破千军','https://www.sgmdtx.com/zf/智破千军/',NULL,'追击','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:54794f7e0b2d5ac8a26b',NULL,NULL);
INSERT INTO "tactics" VALUES(120,'木牛流马','https://www.sgmdtx.com/zf/木牛流马/',NULL,'指挥','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:587985d3057fb8251ae0',NULL,NULL);
INSERT INTO "tactics" VALUES(121,'未雨绸缪','https://www.sgmdtx.com/zf/未雨绸缪/',NULL,'主动','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:604a2fcf99fae23e225b',NULL,NULL);
INSERT INTO "tactics" VALUES(122,'机变无穷','https://www.sgmdtx.com/zf/机变无穷/',NULL,'被动','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:ad146022b594173fe0bb',NULL,NULL);
INSERT INTO "tactics" VALUES(123,'权倾朝野','https://www.sgmdtx.com/zf/权倾朝野/',NULL,'指挥','文武',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:c0274cba8c6e2b62d366',NULL,NULL);
INSERT INTO "tactics" VALUES(124,'权御九锡','https://www.sgmdtx.com/zf/权御九锡/',NULL,'指挥','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:5867786776d97087e0e1',NULL,NULL);
INSERT INTO "tactics" VALUES(125,'束手无策','https://www.sgmdtx.com/zf/束手无策/','紫','主动','谋略','45%','盾兵、弓兵、长枪兵、骑兵',0,'对敌军随机单体造成200%谋略伤害，并施加技穷，持续1回合','s1','Steam已核',10,'2026-09-10T17:37:59+08:00',10,'tactic:b912dccd89978d1f2040',NULL,NULL);
INSERT INTO "tactics" VALUES(126,'来好息师','https://www.sgmdtx.com/zf/来好息师/','紫','被动','治疗',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','Steam已核',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:15208bb4d258ae927282',NULL,NULL);
INSERT INTO "tactics" VALUES(127,'横征暴敛','https://www.sgmdtx.com/zf/横征暴敛/','金','被动','防御',NULL,'盾兵、弓兵、长枪兵、骑兵',0,'施加负面效果后治疗率40%恢复自身兵力并受伤降低10%，持续2回合、可叠4次。','s1','Steam已核',28,'2026-09-10T17:37:59+08:00',10,'tactic:101bd90623365c3c208c',NULL,NULL);
INSERT INTO "tactics" VALUES(128,'横扫千军','https://www.sgmdtx.com/zf/横扫千军/','金','追击','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:c737dd6eca594efc9c5c',NULL,NULL);
INSERT INTO "tactics" VALUES(129,'步步为营','https://www.sgmdtx.com/zf/步步为营/',NULL,'指挥','防御',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:44096ac0e7270bb197be',NULL,NULL);
INSERT INTO "tactics" VALUES(130,'武烈破虏','https://www.sgmdtx.com/zf/武烈破虏/',NULL,'主动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:da7a6fb53691403a8e15',NULL,NULL);
INSERT INTO "tactics" VALUES(131,'武略江洪','https://www.sgmdtx.com/zf/武略江洪/',NULL,'主动','文武',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:4ab2e239018d4b661a53',NULL,NULL);
INSERT INTO "tactics" VALUES(132,'每战先登','https://www.sgmdtx.com/zf/每战先登/',NULL,'指挥','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:f288953b0a38bf741c69',NULL,NULL);
INSERT INTO "tactics" VALUES(133,'水淹七军','https://www.sgmdtx.com/zf/水淹七军/','金','主动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',0,'准备1回合，对敌军全体施加洪水2回合并造成267.8%兵刃伤害；66.95%概率施加技穷、缴械各1回合。','s1','Steam已核',17,'2026-09-10T17:37:59+08:00',10,'tactic:d312f12e723387aad752',NULL,NULL);
INSERT INTO "tactics" VALUES(134,'洗筋伐髓','https://www.sgmdtx.com/zf/洗筋伐髓/',NULL,'被动','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:a80eceb451bc382c21b3',NULL,NULL);
INSERT INTO "tactics" VALUES(135,'洞若观火','https://www.sgmdtx.com/zf/洞若观火/','金','主动','治疗',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:b26097af47c57064a4ae',NULL,NULL);
INSERT INTO "tactics" VALUES(136,'流风回雪','https://www.sgmdtx.com/zf/流风回雪/',NULL,'指挥','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:4228680309ed81136b21',NULL,NULL);
INSERT INTO "tactics" VALUES(137,'淑懿之德','https://www.sgmdtx.com/zf/淑懿之德/',NULL,'主动','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:41f15c57cc4a332b9fc6',NULL,NULL);
INSERT INTO "tactics" VALUES(138,'清风驱疾','https://www.sgmdtx.com/zf/清风驱疾/','金','主动','治疗',NULL,'盾兵、弓兵、长枪兵、骑兵',0,'驱散我军随机两人1种负面状态，并治疗率180%恢复兵力。','s1','Steam已核',37,'2026-09-10T17:37:59+08:00',10,'tactic:f62577aa18a9be541993',NULL,NULL);
INSERT INTO "tactics" VALUES(139,'渊然难测','https://www.sgmdtx.com/zf/渊然难测/',NULL,'指挥','防御',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:4c7cfa8e7239e7b930cd',NULL,NULL);
INSERT INTO "tactics" VALUES(140,'潜龙在渊','https://www.sgmdtx.com/zf/潜龙在渊/',NULL,'指挥','文武',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:59ee5b22e47019ccb541',NULL,NULL);
INSERT INTO "tactics" VALUES(141,'火烧连营','https://www.sgmdtx.com/zf/火烧连营/',NULL,'主动','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:49b98e1bf703c8853a54',NULL,NULL);
INSERT INTO "tactics" VALUES(142,'火羽','https://www.sgmdtx.com/zf/火羽/','紫','主动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','Steam已核',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:bd17584383517f145e42',NULL,NULL);
INSERT INTO "tactics" VALUES(143,'烈火张天','https://www.sgmdtx.com/zf/烈火张天/',NULL,'主动','文武',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:eafeae2e76580f2a2417',NULL,NULL);
INSERT INTO "tactics" VALUES(144,'烈火焚营','https://www.sgmdtx.com/zf/烈火焚营/','金','主动','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',0,'对敌军全体造成84.8%谋略伤害，并施加火攻2回合；再3次焚营，风暴目标焚营伤害提升30%。','s1','Steam已核',14,'2026-09-10T17:37:59+08:00',10,'tactic:2dd59b3e8429ac4febac',NULL,NULL);
INSERT INTO "tactics" VALUES(145,'狂风大作','https://www.sgmdtx.com/zf/狂风大作/','金','指挥','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',0,'第2、4回合开始敌我全体陷入风暴2回合；奇数回合60%全体100%谋略伤害，偶数回合60%随机单体280%谋略伤害。','s1','Steam已核',24,'2026-09-10T17:37:59+08:00',10,'tactic:f29622e061754dbbdbaa',NULL,NULL);
INSERT INTO "tactics" VALUES(146,'猿臂善射','https://www.sgmdtx.com/zf/猿臂善射/',NULL,'被动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:5aa819e89ca0bfe6e425',NULL,NULL);
INSERT INTO "tactics" VALUES(147,'王佐之才','https://www.sgmdtx.com/zf/王佐之才/','金','被动','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',0,'自身奇谋几率提升24%；谋略伤害后50%提升10智力2回合，可叠4次。','s1','Steam已核',30,'2026-09-10T17:37:59+08:00',10,'tactic:53e18266b512159d87e8',NULL,NULL);
INSERT INTO "tactics" VALUES(148,'疾行侧击','https://www.sgmdtx.com/zf/疾行侧击/','紫','主动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','Steam已核',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:fd360dc72c2aa84b9747',NULL,NULL);
INSERT INTO "tactics" VALUES(149,'白衣渡江','https://www.sgmdtx.com/zf/白衣渡江/',NULL,'主动','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:70815a597e8173927431',NULL,NULL);
INSERT INTO "tactics" VALUES(150,'百战不殆','https://www.sgmdtx.com/zf/百战不殆/','金','指挥','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',0,'我军统率/智力/武力最高单体受伤时60%对应提升7点属性，可叠8次至战斗结束。','s1','Steam已核',29,'2026-09-10T17:37:59+08:00',10,'tactic:ac6b4c0e3783a3aaf96e',NULL,NULL);
INSERT INTO "tactics" VALUES(151,'百里疑城','https://www.sgmdtx.com/zf/百里疑城/',NULL,'指挥','防御',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:0749222dc980f8f7a479',NULL,NULL);
INSERT INTO "tactics" VALUES(152,'皇思淑仁','https://www.sgmdtx.com/zf/皇思淑仁/',NULL,'指挥','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:3cbd7042509362687e04',NULL,NULL);
INSERT INTO "tactics" VALUES(153,'直谏固政','https://www.sgmdtx.com/zf/直谏固政/',NULL,'主动','治疗',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:65ac53bec3c2046b71a4',NULL,NULL);
INSERT INTO "tactics" VALUES(154,'睹事知机','https://www.sgmdtx.com/zf/睹事知机/',NULL,'主动','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:e4684f5caef1da9c34ec',NULL,NULL);
INSERT INTO "tactics" VALUES(155,'睿虑合图','https://www.sgmdtx.com/zf/睿虑合图/',NULL,'指挥','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:b9ab579b78a770f9add6',NULL,NULL);
INSERT INTO "tactics" VALUES(156,'瞋目横矛','https://www.sgmdtx.com/zf/瞋目横矛/',NULL,'指挥','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:1a4751354afa22e326e4',NULL,NULL);
INSERT INTO "tactics" VALUES(157,'知人善任','https://www.sgmdtx.com/zf/知人善任/','金','主动','防御',NULL,'盾兵、弓兵、长枪兵、骑兵',0,'我军智力最高单体受伤降低25%（受智力影响）2回合，并获1层抵御。','s2','Steam已核',32,'2026-09-10T17:37:59+08:00',10,'tactic:3e8e778583664d66866f',NULL,NULL);
INSERT INTO "tactics" VALUES(158,'破军袭敌','https://www.sgmdtx.com/zf/破军袭敌/','金','主动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',0,'准备1回合，对敌军全体造成300%兵刃伤害。','s1','Steam已核',44,'2026-09-10T17:37:59+08:00',10,'tactic:80ceac1729fa0b2d2172',NULL,NULL);
INSERT INTO "tactics" VALUES(159,'破阵驰围','https://www.sgmdtx.com/zf/破阵驰围/','金','主动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:d63b395d5863736c5bdf',NULL,NULL);
INSERT INTO "tactics" VALUES(160,'神上使','https://www.sgmdtx.com/zf/神上使/',NULL,'被动','防御',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:6617c9e8bf68e340e4bf',NULL,NULL);
INSERT INTO "tactics" VALUES(161,'神略制变','https://www.sgmdtx.com/zf/神略制变/',NULL,'主动','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:8366c40a710f5683fe6a',NULL,NULL);
INSERT INTO "tactics" VALUES(162,'神速奔袭','https://www.sgmdtx.com/zf/神速奔袭/',NULL,'被动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:b389459002ba4424c92a',NULL,NULL);
INSERT INTO "tactics" VALUES(163,'穷追不舍','https://www.sgmdtx.com/zf/穷追不舍/','紫','被动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s2','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:434e5368f6dfdb5870c7',NULL,NULL);
INSERT INTO "tactics" VALUES(164,'空城计','https://www.sgmdtx.com/zf/空城计/',NULL,'指挥','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:19ef5096de13387b4930',NULL,NULL);
INSERT INTO "tactics" VALUES(165,'筹划良策','https://www.sgmdtx.com/zf/筹划良策/','紫','主动','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','Steam已核',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:37fb8dc61352833fd228',NULL,NULL);
INSERT INTO "tactics" VALUES(166,'算无遗策','https://www.sgmdtx.com/zf/算无遗策/',NULL,'指挥','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:29cd790ad537f3547562',NULL,NULL);
INSERT INTO "tactics" VALUES(167,'素衣约俭','https://www.sgmdtx.com/zf/素衣约俭/',NULL,'指挥','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:339e85e34bbe4a973584',NULL,NULL);
INSERT INTO "tactics" VALUES(168,'红妆缭乱','https://www.sgmdtx.com/zf/红妆缭乱/',NULL,'追击','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:ee97bbff13505c42d381',NULL,NULL);
INSERT INTO "tactics" VALUES(169,'纵马横枪','https://www.sgmdtx.com/zf/纵马横枪/',NULL,'被动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:e659c1a66759e83c2d99',NULL,NULL);
INSERT INTO "tactics" VALUES(170,'经天纬地','https://www.sgmdtx.com/zf/经天纬地/',NULL,'主动','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:72f1a4c5ca14a463cf86',NULL,NULL);
INSERT INTO "tactics" VALUES(171,'缮甲厉兵','https://www.sgmdtx.com/zf/缮甲厉兵/',NULL,'被动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:5cfc1c24e1b7ace99f05',NULL,NULL);
INSERT INTO "tactics" VALUES(172,'耀武扬威','https://www.sgmdtx.com/zf/耀武扬威/',NULL,'主动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:a712101a95db54a7d5ed',NULL,NULL);
INSERT INTO "tactics" VALUES(173,'胜敌益强','https://www.sgmdtx.com/zf/胜敌益强/','金','被动','文武',NULL,'盾兵、弓兵、长枪兵、骑兵',0,'造成兵刃伤害后提升16.48武力、造成谋略伤害后提升16.48智力，均可叠8次。','s2','Steam已核',20,'2026-09-10T17:37:59+08:00',10,'tactic:4c955c4c3f1089e93588',NULL,NULL);
INSERT INTO "tactics" VALUES(174,'膂力过人','https://www.sgmdtx.com/zf/膂力过人/',NULL,'追击','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:a4434743a502ffda5fd5',NULL,NULL);
INSERT INTO "tactics" VALUES(175,'舍生取义','https://www.sgmdtx.com/zf/舍生取义/','金','指挥','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:e64bb6ec86e199f1f16f',NULL,NULL);
INSERT INTO "tactics" VALUES(176,'苦肉计','https://www.sgmdtx.com/zf/苦肉计/',NULL,'主动','防御',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:d4152f5e5c9c76136fc3',NULL,NULL);
INSERT INTO "tactics" VALUES(177,'草船借箭','https://www.sgmdtx.com/zf/草船借箭/',NULL,'指挥','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:b8b9d6c27fedfd90f8d9',NULL,NULL);
INSERT INTO "tactics" VALUES(178,'荐计阻敌','https://www.sgmdtx.com/zf/荐计阻敌/',NULL,'主动','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:c0cf83fb701e52ee240d',NULL,NULL);
INSERT INTO "tactics" VALUES(179,'荼蘼心计','https://www.sgmdtx.com/zf/荼蘼心计/',NULL,'指挥','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:91b51a5bb7495e641cac',NULL,NULL);
INSERT INTO "tactics" VALUES(180,'蓄势待发','https://www.sgmdtx.com/zf/蓄势待发/','金','指挥','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',0,'每回合开始提升两名队友7%造成伤害，可叠加至战斗结束。','s1','Steam已核',31,'2026-09-10T17:37:59+08:00',10,'tactic:62bbd903f61b9c8f919f',NULL,NULL);
INSERT INTO "tactics" VALUES(181,'虎啸生威','https://www.sgmdtx.com/zf/虎啸生威/',NULL,'被动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:668f0594d60022be5952',NULL,NULL);
INSERT INTO "tactics" VALUES(182,'虎步连环','https://www.sgmdtx.com/zf/虎步连环/',NULL,'追击','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:a6ebab8c3ea1af537089',NULL,NULL);
INSERT INTO "tactics" VALUES(183,'虎踞江东','https://www.sgmdtx.com/zf/虎踞江东/',NULL,'指挥','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:f83f439fcf070eaef198',NULL,NULL);
INSERT INTO "tactics" VALUES(184,'裸衣血战','https://www.sgmdtx.com/zf/裸衣血战/',NULL,'被动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:0744143b4be4741efab0',NULL,NULL);
INSERT INTO "tactics" VALUES(185,'誓死无退','https://www.sgmdtx.com/zf/誓死无退/',NULL,'指挥','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:b84442289531e42e0311',NULL,NULL);
INSERT INTO "tactics" VALUES(186,'计袭粮仓','https://www.sgmdtx.com/zf/计袭粮仓/','金','追击','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:1ebe1c66d527d7992788',NULL,NULL);
INSERT INTO "tactics" VALUES(187,'计逐穷寇','https://www.sgmdtx.com/zf/计逐穷寇/','紫','被动','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','Steam已核',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:7e9f36d1419b92294283',NULL,NULL);
INSERT INTO "tactics" VALUES(188,'诛凶殄逆','https://www.sgmdtx.com/zf/诛凶殄逆/',NULL,'主动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:e19bf84fa5ea32091480',NULL,NULL);
INSERT INTO "tactics" VALUES(189,'诡道玄机','https://www.sgmdtx.com/zf/诡道玄机/',NULL,'指挥','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:5a8966c7e72ec0c51a34',NULL,NULL);
INSERT INTO "tactics" VALUES(190,'诱敌深入','https://www.sgmdtx.com/zf/诱敌深入/',NULL,'主动','防御',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:c263a9d0366017bccc98',NULL,NULL);
INSERT INTO "tactics" VALUES(191,'调和阴阳','https://www.sgmdtx.com/zf/调和阴阳/',NULL,'指挥','防御',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:0dc4df5fe706422915d7',NULL,NULL);
INSERT INTO "tactics" VALUES(192,'谈笑诛心','https://www.sgmdtx.com/zf/谈笑诛心/','紫','被动','谋略','100%','盾兵、弓兵、长枪兵、骑兵',0,'敌军被施加负面状态时，有60%概率对敌军随机单体造成119.9%谋略伤害，每回合最多触发2次','s1','Steam已核',13,'2026-09-10T17:37:59+08:00',10,'tactic:e6b284a80b21f9aa0da8',NULL,NULL);
INSERT INTO "tactics" VALUES(193,'谋而后动','https://www.sgmdtx.com/zf/谋而后动/',NULL,'追击','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:89e17a2585027edfb0f3',NULL,NULL);
INSERT INTO "tactics" VALUES(194,'趁火打劫','https://www.sgmdtx.com/zf/趁火打劫/','金','主动','文武',NULL,'盾兵、弓兵、长枪兵、骑兵',0,'准备1回合，敌军随机两人220%谋略和兵刃伤害；火攻目标额外混乱2回合。','s1','Steam已核',25,'2026-09-10T17:37:59+08:00',10,'tactic:320f7a0d6e28e0f607e0',NULL,NULL);
INSERT INTO "tactics" VALUES(195,'践墨随敌','https://www.sgmdtx.com/zf/践墨随敌/',NULL,'被动','防御',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:dd51065b719045b9613b',NULL,NULL);
INSERT INTO "tactics" VALUES(196,'蹈锋饮血','https://www.sgmdtx.com/zf/蹈锋饮血/',NULL,'被动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:a798715f6fa889de4c38',NULL,NULL);
INSERT INTO "tactics" VALUES(197,'轻装驰援','https://www.sgmdtx.com/zf/轻装驰援/','金','追击','防御',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:a7ac7d7c0e50c88e4e67',NULL,NULL);
INSERT INTO "tactics" VALUES(198,'辕门射戟','https://www.sgmdtx.com/zf/辕门射戟/','金','追击','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:bb6d0cb5745cca479938',NULL,NULL);
INSERT INTO "tactics" VALUES(199,'迎敌','https://www.sgmdtx.com/zf/迎敌/','紫','主动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','Steam已核',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:7624d1699c0d0d85548d',NULL,NULL);
INSERT INTO "tactics" VALUES(200,'运智铺谋','https://www.sgmdtx.com/zf/运智铺谋/',NULL,'被动','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:1d4d902c80ba7d93ee83',NULL,NULL);
INSERT INTO "tactics" VALUES(201,'运筹帷幄','https://www.sgmdtx.com/zf/运筹帷幄/','金','主动','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:2bdc72edc661c61ef353',NULL,NULL);
INSERT INTO "tactics" VALUES(202,'连环计','https://www.sgmdtx.com/zf/连环计/',NULL,'指挥','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:d198911d4713ef1831bf',NULL,NULL);
INSERT INTO "tactics" VALUES(203,'避其锐气','https://www.sgmdtx.com/zf/避其锐气/','紫','指挥','防御',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','Steam已核',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:569140a6f79a8df6a042',NULL,NULL);
INSERT INTO "tactics" VALUES(204,'金城汤池','https://www.sgmdtx.com/zf/金城汤池/',NULL,'指挥','防御',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:5af9fae1be615dc4674a',NULL,NULL);
INSERT INTO "tactics" VALUES(205,'铁骑横冲','https://www.sgmdtx.com/zf/铁骑横冲/','金','追击','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',0,'普攻后提升自身20.6%会心2回合，再对当前目标造成412%兵刃伤害；伤害系数每回合降低25%。','s1','Steam已核',16,'2026-09-10T17:37:59+08:00',10,'tactic:f79a21585b0730e28363',NULL,NULL);
INSERT INTO "tactics" VALUES(206,'铸甲销戈','https://www.sgmdtx.com/zf/铸甲销戈/','紫','指挥','防御',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','Steam已核',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:209cd4cbd1a4b56ae15e',NULL,NULL);
INSERT INTO "tactics" VALUES(207,'锐不可当','https://www.sgmdtx.com/zf/锐不可当/','金','被动','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',0,'提升自身16%破甲和35%造成伤害。','s1','Steam已核',23,'2026-09-10T17:37:59+08:00',10,'tactic:b68eb67708499b2ff2af',NULL,NULL);
INSERT INTO "tactics" VALUES(208,'锦帆渠魁','https://www.sgmdtx.com/zf/锦帆渠魁/',NULL,'被动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:161e37440eb40dff418b',NULL,NULL);
INSERT INTO "tactics" VALUES(209,'长驱直入','https://www.sgmdtx.com/zf/长驱直入/',NULL,'主动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:35b204762e467be39bda',NULL,NULL);
INSERT INTO "tactics" VALUES(210,'闭月','https://www.sgmdtx.com/zf/闭月/',NULL,'被动','防御',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:51ea5c7a755c12e24942',NULL,NULL);
INSERT INTO "tactics" VALUES(211,'陷阵蹈难','https://www.sgmdtx.com/zf/陷阵蹈难/',NULL,'被动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:f45d41b9eccf83dbd2ad',NULL,NULL);
INSERT INTO "tactics" VALUES(212,'雄护南疆','https://www.sgmdtx.com/zf/雄护南疆/',NULL,'指挥','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:0d901ee06f752f58f286',NULL,NULL);
INSERT INTO "tactics" VALUES(213,'雄踞西凉','https://www.sgmdtx.com/zf/雄踞西凉/',NULL,'指挥','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:3ba8afc27c4ce4b3440e',NULL,NULL);
INSERT INTO "tactics" VALUES(214,'青囊急救','https://www.sgmdtx.com/zf/青囊急救/','金','主动','治疗',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:0ab570eb68ceb3bdfc43',NULL,NULL);
INSERT INTO "tactics" VALUES(215,'韬光养晦','https://www.sgmdtx.com/zf/韬光养晦/','金','被动','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',0,'自身主动战法发动率提升6%（受智力影响）；每回合开始自身谋略伤害提升8%，可叠加至结束。','s2','Steam已核',34,'2026-09-10T17:37:59+08:00',10,'tactic:90aacda6cfdfc7296c53',NULL,NULL);
INSERT INTO "tactics" VALUES(216,'顾盼生姿','https://www.sgmdtx.com/zf/顾盼生姿/',NULL,'被动','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:05832cb1bbc6506e24f5',NULL,NULL);
INSERT INTO "tactics" VALUES(217,'风助火势','https://www.sgmdtx.com/zf/风助火势/',NULL,'主动','文武',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:bea3f75f9ced763cf404',NULL,NULL);
INSERT INTO "tactics" VALUES(218,'风卷残云','https://www.sgmdtx.com/zf/风卷残云/','金','主动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:732f31d3802bbac61f71',NULL,NULL);
INSERT INTO "tactics" VALUES(219,'风急雨晦','https://www.sgmdtx.com/zf/风急雨晦/',NULL,'主动','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:d3d335c6912f6ea482a3',NULL,NULL);
INSERT INTO "tactics" VALUES(220,'风袭逍遥','https://www.sgmdtx.com/zf/风袭逍遥/',NULL,'被动','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:2efe8e31fdfa4d1e84f0',NULL,NULL);
INSERT INTO "tactics" VALUES(221,'飞身断虹','https://www.sgmdtx.com/zf/飞身断虹/',NULL,'被动','防御',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:fd8d6c382921ddbc17f6',NULL,NULL);
INSERT INTO "tactics" VALUES(222,'驰军截刃','https://www.sgmdtx.com/zf/驰军截刃/',NULL,'被动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:216de799d659dbcfd6cd',NULL,NULL);
INSERT INTO "tactics" VALUES(223,'驱兽御象','https://www.sgmdtx.com/zf/驱兽御象/',NULL,'指挥','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:14e807ab0880f61f73b5',NULL,NULL);
INSERT INTO "tactics" VALUES(224,'骁勇之姿','https://www.sgmdtx.com/zf/骁勇之姿/','紫','被动','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,'s1','Steam已核',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:2af85d95bcd850ae486a',NULL,NULL);
INSERT INTO "tactics" VALUES(225,'骁勇无前','https://www.sgmdtx.com/zf/骁勇无前/',NULL,'主动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:cda3667401ac93c7e643',NULL,NULL);
INSERT INTO "tactics" VALUES(226,'鸩饮毒弑','https://www.sgmdtx.com/zf/鸩饮毒弑/',NULL,'主动','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:2541c379556be1e964cc',NULL,NULL);
INSERT INTO "tactics" VALUES(227,'鹰视狼顾','https://www.sgmdtx.com/zf/鹰视狼顾/',NULL,'主动','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:afcf5c193f1c1e95500a',NULL,NULL);
INSERT INTO "tactics" VALUES(228,'麻沸散','https://www.sgmdtx.com/zf/麻沸散/',NULL,'指挥','辅助',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:0bc9f1d45c3f7d1436e8',NULL,NULL);
INSERT INTO "tactics" VALUES(229,'黄天当立','https://www.sgmdtx.com/zf/黄天当立/',NULL,'主动','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:b8cdc491ee6053f12446',NULL,NULL);
INSERT INTO "tactics" VALUES(230,'黄天惑心','https://www.sgmdtx.com/zf/黄天惑心/',NULL,'主动','谋略',NULL,'盾兵、弓兵、长枪兵、骑兵',0,NULL,NULL,'跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:d69c2eea4eb80c15323b',NULL,NULL);
INSERT INTO "tactics" VALUES(231,'龙吟四海','https://www.sgmdtx.com/zf/龙吟四海/',NULL,'被动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:c2427376c43aef7611a5',NULL,NULL);
INSERT INTO "tactics" VALUES(232,'弦无虚发','https://www.sgmdtx.com/zf/%E5%BC%A6%E6%97%A0%E8%99%9A%E5%8F%91/',NULL,'被动','兵刃',NULL,'盾兵、弓兵、长枪兵、骑兵',1,NULL,'s1','跨赛季参考',1,'2026-08-19T17:01:54+08:00',NULL,'tactic:ea93e058bb08c7d6afbd',NULL,NULL);
CREATE VIEW v_general_level50_estimate AS
SELECT
  name,
  faction,
  troop_type,
  CAST(base_force + growth_force * (50 - reference_level) + 0.5 AS INTEGER) AS force,
  CAST(base_intelligence + growth_intelligence * (50 - reference_level) + 0.5 AS INTEGER) AS intelligence,
  CAST(base_command + growth_command * (50 - reference_level) + 0.5 AS INTEGER) AS command,
  CAST(base_initiative + growth_initiative * (50 - reference_level) + 0.5 AS INTEGER) AS initiative
FROM generals
WHERE base_force IS NOT NULL;
CREATE VIEW v_s1_generals AS
SELECT * FROM generals WHERE lower(first_season) = 's1';
CREATE VIEW v_s1_tactics AS
SELECT * FROM tactics WHERE lower(first_season) = 's1';
CREATE VIEW v_s1_gold_generals AS
SELECT * FROM v_s1_generals WHERE quality = '金';
CREATE VIEW v_recommendable_tactics AS
SELECT * FROM v_s1_tactics
WHERE quality IN ('金','紫') AND is_self_tactic = 0;
CREATE VIEW v_recommendable_strategy_books AS
SELECT * FROM strategy_books
WHERE quality = '紫' OR book_scope LIKE '%专属%';
CREATE INDEX idx_generals_season ON generals(first_season);
CREATE INDEX idx_tactics_type ON tactics(tactic_type);
CREATE INDEX idx_effects_category ON effects(category);
CREATE INDEX idx_tactic_level_observations_lookup
ON tactic_level_observations(tactic_id, level);
CREATE UNIQUE INDEX idx_generals_entity ON generals(entity_id);
CREATE UNIQUE INDEX idx_tactics_entity ON tactics(entity_id);
COMMIT;
