蘇清的容器升级 1.0.1 — Build 42.21 单人

语言 / Languages: 中文在前，完整英文说明在后。Chinese first; complete English instructions follow.
作者当前单人档合集：https://steamcommunity.com/sharedfiles/filedetails/?id=3823981387
作者确认当前合集在自己的B42.21单人档游玩正常；该反馈对应完整204个启用Mod ID，含32个未公开本地补丁。
工坊合集不会下载这32个补丁，不能单独完整复现作者配置。完整列表、来源与启用顺序：
https://github.com/suching8848/suqing-container-upgrade/blob/main/docs/current-single-player-modlist.md


1.0.0整理为独立发布包，核心机制沿用已测试的0.2.2，并新增专用图标与封面。
维护者已确认v1.0.0在个人Build 42.21单人环境中使用正常。
v1.0.0客户端验证覆盖单人代表项；本次四项新增仅离线检查，172项不代表全部逐件游戏内实测。
已发布Steam创意工坊版本3823988025；GitHub同时提供源码与手动安装包。

安装
完全退出游戏并备份后，将本目录整体放入 %UserProfile%\Zomboid\mods\。
应保留42与common目录；42/mod.info中的Mod ID为 SuQingContainerUpgrade_4221。
在模组列表和目标单人存档中启用，停用重复旧版/测试版，再重启游戏。

1.0.1新增适配
注射器盒CombatStims.InjectorCase、生化胸挂CodexCBRT.SST02_ChestRig、HavenFall前后腰包ESHF.Qwe_Backpack与ESHF.Qwe_BackpackFront。
保留针剂过滤、最大物品尺寸10、腰包换位及既有有效强化记录；材料、技能、返料规则沿用。新增适配尚待游戏内验收。HavenFall大背包EX仍属于独立扩展。

范围与名单
当前启用模组按实际加载顺序清点，原版86个、模组105个可穿戴容器ID。
支持172个（原版84、模组88）；1个仅供旧强化记录还原；18个明确排除。
“最终适配物品名单.txt”逐件列出全部支持项，“适配名单.csv”列出全部191项与理由。
名称相同但ID不同的朝向、尺寸、颜色分别统计，不代表172种独立外观。
苏别璃原始装备的4件容器全部纳入；不改该模组原始装备机制。

液体容器注意事项
水袋背包、水袋胸挂等带储液功能的容器，强化或还原前必须排空全部液体。
只移走普通物品不算清空；哪怕剩少量水或其他液体，也无法制作。
升级只改变普通物品容量和减重，不增加储水升数；完成后可重新装水。

入口与操作
只使用制作菜单“蘇清”分类和游戏原生快捷制作入口。
没有自建右键菜单、悬浮信息、额外等级名称或成功失败弹字；技术结果写日志。
将容器卸下、放入人物主物品栏、清空内部物品；有液体组件的容器还需排空液体。
准备针、普通线、干净碎布条及皮革条，再选择当前下一档配方。
针保留，普通满卷线20用量。材料、技能、制作时间沿用既有配方。

制作面板的旧档位仍可能亮起；整体候选或缓存状态不代表当前这件包可以制作该档。
同一件包只允许当前下一档；旧档会在前置检查中正常拒绝，不扣材料、不重复强化或降级。
若原生动作已进入队列，仍可能播放动作或耗时；动作结束不等于强化成功。

档位   名义容量/减重  碎布条  皮革条  线用量  裁缝等级
I          12/90%       4       0       2        0
II         20/93%       6       2       4        1
III        30/95%      10       4       6        2
IV         40/97%      14       6       8        3
V          49/99%      20      10      10        4

容量和减重同时达到某档规格时，自动跳过该档；仅单项较高时保留该高值。
角色特性仍可调整有效容量。
普通重包与新增模组包按floor(50-物品实际自重)安全取整；因此部分包满级为46至48，
这些是本补丁保留自重时采用的安全上限。原始自重不改，流体量不计入此固定自重。
50/60标称容量的背包系统三件和SafeWay包只提高减重，绝不写入物理容量，
避免游戏容量getter上限50把原始60误写为50。已有99或100减重不降级。
浣熊市背包和背带沿用原沙盒基础容量及特性算法，仅对有效蘇清记录叠加升级下限；
不改物理容量，不修改原模组函数源。沙盒容量较大时保留较大值；还原回当前沙盒值。
物品原始脚本容量、游戏读取容量、角色有效容量并不总相同，名单分别说明。

生化背包和生化背带的容量显示
修正浣熊市原有的容量提示行，显示该角色当前实际可用容量，不新增强化等级悬浮信息。
原生白字容量仍为物理属性参考行；实际容量以修正后的提示行和穿戴容器栏为准。
基础容量保留沙盒值与已付强化值中较大的一个，再计算一次角色特性。
例如若生化背包沙盒基础98、减重99%，井井有条后容量128，已满足普通V档。
若生化背带沙盒基础30、减重99%，普通IV档基础40时为52；V档基础49时为64。
以上例子不代表修改原模组默认配置；不同沙盒设置会得到不同结果。
本版不增加EX，不把储水容量或换弹加速与物品容量混为一项。

原模组特性与收纳限制
强化和还原修改原物品实例，只改受管的容量、减重及蘇清记录。
名称、外观、收藏、耐久、穿戴槽、挂点、原ModData和液体组件不改。
不改加速换弹/装弹标签，不包装武器换弹、弹药插入函数。
MFS自动装弹设备保留其原生每次动画最多装入5发及佩戴/随身判定。
胸挂仍保留MaxItemSize，子弹/霰弹带仍按原过滤函数收纳。
肩挂枪套即使容量提高，也仍然最多2个手枪弹匣；不增加武器挂点。
液体混合包只加强普通物品收纳，储水升数、成分和流体机制保持原值。

原生换位和尺寸转换
对清单内精确前后腰包、同ID穿戴替换，以及8条已核对的原生尺寸转换配方，
仅在源物品有合法且一致的蘇清记录时，保留强化规格和记录。
原生代码继续负责外观、改名、耐久、收藏、内容物及原ModData复制。
目标需为该动作新建的实例；人物主物品栏和目标槽位必须能安全容纳。
前后换位前，先把目标槽上的另一件腰包卸入人物主物品栏，让目标槽空闲。
不会自动挤掉、卸下或丢掉另一件包；目标被占用时，在动作预检中正常拒绝。
本版包含0.2.1修订，不再用destination_occupied异常处理正常占用。
其他物品、无有效记录的动作、普通CopyClothing和无关配方保持原来的处理链。
加码/减码保留原配方材料和消耗；不通过全局物品复制钩子传播强化。
用已强化包作为新制作配方的消耗材料，并不保证新产物继承强化；请先还原，
例如用原版生存者背包制作近轨航行背包属于新制作而非尺寸转换。

原生升级链与无需强化项
踏行千山六件沿用其原模组升级链；粗制皮包和粗制防水布包沿用原版扩容配方。
踏行千山五仅为已有有效蘇清记录保留免费还原，未强化的物品无需操作。
传奇背包10件和Estate39的Miku背包已达到目标，不加入收费强化。
非穿戴箱子/板条箱不在此次容器衣物范围，不按外观或名称泛化支持。

还原与故障恢复
清空卸下后使用“还原首次强化前的规格”；不加经验。
成功还原时，返还本版支付账本中布、皮革、普通线各自累计实付量的50%，向下取整。
完整真实支付I至V档的例子：返27碎布条、11皮革条、15普通线用量；普通满卷线20用量。
线按实际用量返还，可能得到部分线轴。跳过的档位和免费、未实际消耗的操作不产生返料。
没有付款记录的旧强化仍可免费还原，但旧材料不追溯计算；0.2.2起已有的合法实付记录继续有效。
例如未记账的旧IV档物品之后真实支付V档，成功还原只返V档这一笔的一半。
还原与返料一起结算，成功后清除付款记录，重复点击不会重复领取。
这仍是还原至首次强化前的操作，不新增逐级降档配方。取消制作不按50%规则结算。
普通物理容量恢复第一次强化前值；容量保留方案不写容量；浣熊市恢复当前沙盒机制。
单纯停用补丁不会自动还原已保存的物理属性；所属衣物模组仍需保留。
旧schema1保留读取，成功后续强化才写schema2；不扫描或批量改写世界物品。
新记录保存当时应用值、原始值、方案版本和安全容量阈值。
记录损坏拒绝收费；合法但与当前方案不符的记录仍可还原。
制作前先验证属性setter能工作，后续失败独立尝试恢复目标和原材料实例/线用量。
换位/尺寸转换故障也尝试恢复内容物、原穿戴槽和双手，不删除仍含内容的新容器。
原生已发出的事件、经验和制作历史无法全部撤销；永久性的外部setter错误可能阻止恢复，
日志会标明失败。一次成功命令或动作动画本身不等同于游戏内功能验收。

维护与验证
compatibility/registry.json 是唯一适配名单。运行Python3：
  python tools/build_compatibility.py
  python tools/build_compatibility.py --check
生成运行时白名单、六个配方目标和名单；游戏运行不需要Python。
未知ID默认不支持。没有周期扫描、世界扫描、掉落表改动或工坊文件覆盖。
独立Debug测试若在原生配方调试的图标面板遇到setPlaceholderText空引用，
请避开该原生调试UI入口，改用Debug物品列表生成器准备物品，再用正常制作面板测试。
该提示只说明测试入口，不增加自定义界面，也不把原生调试UI错误当作强化结果。
本版面向Build 42.21单人模式。客户端代表项包括容量显示与还原返料等具体项目，
维护者已确认v1.0.0在个人单人环境中使用正常。
离线回归和源审计单独记录，不与游戏内验证混算。
172项是适配支持范围，不表示172项均已逐件实测，也不据此扩大保存重进、装弹或其他场景的验收范围。
多人和专用服务器未验证，当前前置检查不开放联机强化与还原。
验证扣料和返料时请关闭Debug免费制作/无限材料，用正常制作面板检查真实材料差额。
完全退出并重启游戏后才加载新版Lua。本版不含EX。

源码与素材
公开源码，尚未单独指定开源许可证；兼容原模组的权利归各自作者。
封面、头像与配方图标由AI辅助生成并依据维护者确认的角色参考制作，未统一授予MIT等素材许可。
公开仓库中的docs/ASSETS.md说明素材与第三方权利边界。


=== English: complete player and maintenance guide ===

蘇清的容器升级 | SuQing's Container Upgrades

简体中文: https://github.com/suching8848/suqing-container-upgrade/blob/main/README.md · English: https://github.com/suching8848/suqing-container-upgrade/blob/main/README.en.md

> This mod greatly changes realism and balance. Add it with care. It is intended for players who enjoy collecting and stockpiling supplies.
>
> Larger capacities and strong weight reduction substantially ease inventory management and transport decisions. Choose it to suit your play style.


v1.0.1 · Project Zomboid Build 42.21 · Single-player

Upgrade existing wearable containers with clean ripped sheets, leather strips and thread. The original item and its functions remain in place. Recipes use the native crafting category and quick-crafting entry points.

The Steam Workshop release: https://steamcommunity.com/sharedfiles/filedetails/?id=3823988025 is available; GitHub provides the source and files for manual installation. This release does not include EX upgrades.

The author's current single-player save and collection

Current Workshop collection: https://steamcommunity.com/sharedfiles/filedetails/?id=3823981387 · Complete mod list and enabled order: https://github.com/suching8848/suqing-container-upgrade/blob/main/docs/current-single-player-modlist.md

The author reports normal play with this current collection in their own B42.21 single-player save. This report concerns the author's full configuration: 204 enabled Mod IDs, including 32 unpublished local patches. It is not a claim that every supported item, every mod combination or multiplayer has been tested.

The Steam collection lists publicly subscribable Workshop items. It does not include unpublished local patches, and it does not replace the complete enabled order. Consult the full list for local patches, source differences and the actual order. Subscribing to the collection alone does not reproduce the entire environment.

Features and supported scope

- Explicit support for 172 exact item IDs: 84 vanilla and 88 audited mod items. Facing, size and color variants count separately.
- Five upgrade tiers, restoration to the original pre-upgrade specification, and a refund after successful restoration.
- Supported front/back swaps, same-ID clothing replacements and 8 native size-conversion recipes preserve valid upgrade records.
- The two Raccoon City containers retain their sandbox and character-trait calculations; their existing capacity tooltip line is corrected.
- Dedicated portrait, upgrade/restore icons and cover. No custom context menu, extra tier tooltip area or success/failure floating text.

See the 172 supported IDs: https://github.com/suching8848/suqing-container-upgrade/blob/main/SuQingContainerUpgrade/最终适配物品名单.txt and the complete classification of 191 entries and restrictions: https://github.com/suching8848/suqing-container-upgrade/blob/main/SuQingContainerUpgrade/适配名单.csv. The latter also contains 1 restore-only entry and 18 exclusions. Unknown IDs are unsupported.

Specified containers from Fantasy Workshop, 2DimensionWardrobe, Backpack System, SuPrimitiveEquipment, They Knew Continued, Raccoon City, SafeWayHamlet and MFS are supported. You do not need all these mods to upgrade vanilla containers. Each source mod still supplies its own items.

Added in 1.0.1

- CombatStims.InjectorCase: injector case; retains the upstream injector filter and maximum item size 10. Extra Adrenapen storage remains part of a separate compatibility patch.
- CodexCBRT.SST02_ChestRig: combat rig from the independent Chemical compatibility build. It requires that build; this mod does not distribute third-party equipment assets.
- ESHF.Qwe_Backpack and ESHF.Qwe_BackpackFront: HavenFall rear/front waist packs. Valid upgrade records and destination-slot protection are preserved during supported swaps.

Materials, skills, payment ledgers and restoration refunds are unchanged. Valid records previously written by the independent compatibility patch remain usable. HavenFall large-backpack EX upgrades remain a separate extension. These four integrations are optional and require their source mods.

Five tiers and costs

Each row is the cost of that individual tier, not a cumulative total. Capacity and weight reduction are target minimums; higher existing values are preserved.

| Tier | Nominal base capacity | Weight reduction | Clean ripped sheets | Leather strips | Thread uses | Tailoring level |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| I | 12 | 90% | 4 | 0 | 2 | 0 |
| II | 20 | 93% | 6 | 2 | 4 | 1 |
| III | 30 | 95% | 10 | 4 | 6 | 2 |
| IV | 40 | 97% | 14 | 6 | 8 | 3 |
| V | Up to 49 | 99% | 20 | 10 | 10 | 4 |

The needle is retained. A full ordinary Base.Thread spool has 20 uses: the table counts uses, not spools. Material IDs are Base.RippedSheets, Base.LeatherStrips and Base.Thread; needles use the native sewing-needle tag.

A tier is skipped when both capacity and weight reduction already meet it. Only the actual next tier is charged. A higher value in either attribute is never reduced.

Ordinary tier V reaches at most base capacity 49. Some heavy bags retain their actual weight and use the safety cap floor(50 - item weight), so their final capacity can be 46, 47 or 48. Character traits still affect effective capacity. Specified native 50/60-capacity bags receive weight reduction only; their physical capacity is unchanged. The two Raccoon City containers preserve larger sandbox base values. Consult the item list for exact policies.

Installation and use

Choose either Steam subscription or a manual Git download. Both use Mod ID SuQingContainerUpgrade_4221; keep only one installation source for that ID. Before switching, fully exit the game, back up the save and old files, move duplicate local copies out of the mod directory, and disable old test versions.

Steam subscription

1. Open the Workshop page: https://steamcommunity.com/sharedfiles/filedetails/?id=3823988025 and select Subscribe.
2. Wait for Steam to finish downloading, then launch Build 42.21.
3. Enable SuQing's Container Upgrades in both the game mod list and the target single-player save's mod management.
4. Fully exit and restart the game so the new Lua and resources load, then enter the target save.

Manual Git download

1. Select Code → Download ZIP. Extract it and copy the SuQingContainerUpgrade folder to %UserProfile%\Zomboid\mods\.
2. Check for %UserProfile%\Zomboid\mods\SuQingContainerUpgrade\42\mod.info, keeping sibling folders such as common. The repository root itself is not the mod folder.
3. Enable the mod in the game list and the target single-player save, then fully exit and restart. Manual installations require manually downloading future updates.

Upgrading an item

Unequip the container, place it in the character's main inventory and remove all contents. Prepare the materials and select the current next tier in the “蘇清” crafting category. Vanilla containers do not require all optional source mods.

Fluid containers such as hydration backpacks and rigs must have all liquid drained before upgrading or restoring. Removing ordinary items is insufficient: even a little remaining water or other fluid blocks crafting. Only ordinary-item storage improves; fluid capacity and components are unchanged.

Old tiers may still appear selectable in the crafting panel. Cached candidates do not establish that the current item can perform that tier. Only its next tier is allowed; old tiers are rejected without payment. A queued native action may still take time. The end of an animation alone does not prove success.

Before swapping a front/back pack, unequip any other pack from the destination slot into the main inventory. An occupied slot is rejected normally; the other pack is not displaced or dropped.

Restoration and refunds

Empty and unequip the container, then use the recipe to restore its first pre-upgrade specification. This is a full restoration, not a step-down recipe, and grants no experience.

A successful restoration refunds 50% of each material's cumulative actual payment in a valid ledger, rounded down separately. Cloth and leather are returned as items; thread is returned in uses and can produce a partial spool. Actually paying all five tiers costs 54 cloth, 22 leather and 30 thread uses, yielding 27 cloth, 11 leather and 15 thread uses on restoration.

Only successfully consumed materials are recorded. Skipped tiers, free crafting and operations with no actual consumption create no refund entitlement. Older payments without a ledger are not reconstructed. Valid ledgers from 0.2.2 remain supported: for example, if only tier V was paid after an unrecorded old tier IV, only half of that tier-V payment is refunded. Successful restoration clears the ledger, preventing repeated collection. Crafting cancellation does not use this 50% refund rule.

Disabling the mod does not automatically restore saved physical attributes. Restore items as needed before removing it, and keep the mod that supplies the container.

Preserved functions and restrictions

Upgrades change managed capacity, weight reduction and this mod's records on the original item instance. Original weight, name, appearance, condition, favorite state, clothing slots, attachment points and other ModData are retained.

- Reload tags, MFS automatic-loading checks and loading logic are unchanged. More storage does not increase rounds loaded per animation.
- Rig item-size limits, ammunition-belt filters and the shoulder holster's maximum of 2 pistol magazines remain active.
- Only audited native swaps and size conversions preserve records. Other crafting recipes consuming an upgraded bag need not transfer them to the new product; restore it first.
- The six 踏行千山 containers and vanilla crude leather/tarp bags retain their own native upgrade chains instead of paid upgrades. 踏行千山五 is restore-only for valid old records.
- The 10 Legendary Backpack colors and Estate 39's Miku bag already meet ordinary targets and are excluded from paid upgrading. Non-wearable crates are outside the scope.

Validation scope

The maintainer confirmed normal use of v1.0.0 in their own Build 42.21 single-player environment, covering representative items. v1.0.1 incorporates four ordinary integrations from an existing independent patch. Offline checks and gameplay acceptance for the additions are tracked separately. The support count of 172 does not mean every item has been tested individually, or that all reload, save/reload or mod-combination scenarios have passed.

This release is single-player only. Multiplayer and dedicated servers are unvalidated; the current preconditions do not allow upgrading or restoration in multiplayer. See testing guidance: https://github.com/suching8848/suqing-container-upgrade/blob/main/docs/TESTING.en.md.

Maintaining the supported list

SuQingContainerUpgrade/compatibility/registry.json is the single registry source. From the repository root, use Python 3:

cd SuQingContainerUpgrade
python tools/build_compatibility.py
python tools/build_compatibility.py --check

The generator updates the runtime allowlist, six recipes and readable lists. --check only verifies that generated outputs match. Scope changes must also audit original capacity, restrictions, native upgrade chains and swap/size-conversion behavior. Python is not required while playing.

Source and assets

The repository currently has no open-source license attached. Icons and cover artwork were made with AI assistance. The original game and supported mods belong to their authors. See asset notes: https://github.com/suching8848/suqing-container-upgrade/blob/main/docs/ASSETS.en.md.

See CHANGELOG: https://github.com/suching8848/suqing-container-upgrade/blob/main/CHANGELOG.md for release history and the Workshop guide: https://github.com/suching8848/suqing-container-upgrade/blob/main/docs/WORKSHOP.en.md for publishing and updates. tools/prepare_workshop.py prepares the upload folder recognized by the game.

Additional detailed behavior and recovery notes

The audited source inventory contains 191 wearable-container IDs: 86 vanilla and 105 mod IDs. Of these, 172 are supported (84 vanilla + 88 mod), 1 is restore-only and 18 are excluded. Identically named facing/size/color variants count as separate IDs, not 172 distinct appearances. All 4 SuPrimitiveEquipment containers are included without replacing that mod's equipment mechanics.

The mod adds no custom floating tier names or success/failure text; technical results go to the log. Recipe materials, skill gates and action times follow the existing recipes. Higher existing weight reduction, including 99 or 100, is not reduced. The safety cap uses actual fixed item weight, not the current amount of fluid.

The specified three Backpack System items and SafeWay bag have native nominal capacities of 50/60. Only their weight reduction is written. This avoids overwriting an original 60 with the game's capacity getter limit of 50. Script capacity, physical/getter capacity and trait-adjusted effective capacity need not be identical; the item list distinguishes them.

Raccoon City backpack and rig capacity display
The existing tooltip line shows that character's usable capacity; there is no added upgrade-tier tooltip. The native white capacity line remains a physical reference. The sandbox base and paid upgrade floor are compared first; character traits are then applied once. Physical capacity and the original source functions are not rewritten. Restoration returns to the current sandbox mechanism.
For example, sandbox base 98 and weight reduction 99% on the backpack gives effective capacity 128 with Organized and already meets ordinary tier V. A rig with sandbox base 30 gives 52 at ordinary tier IV's base 40, or 64 at tier V's base 49. These examples do not change source-mod defaults. Different sandbox settings can give different results. Fluid storage and reload speed are separate from item capacity.

Original storage and loading mechanics
The original item instance and fluid component stay in place. Upgrade/restore does not wrap weapon reloading or ammunition-insertion functions. MFS automatic loading keeps its original limit of up to 5 rounds per animation and its own worn/carried checks. Rig MaxItemSize and bullet/shotgun-belt filters remain active. A shoulder holster still accepts at most 2 pistol magazines, with no added weapon attachment points. Fluid type, mixture and fluid-capacity mechanics are unchanged.

Native swaps and size conversions
Only the exact audited front/back swaps, same-ID worn replacement actions and 8 native size conversions are bridged, and only with a legal, consistent upgrade record. Native code still copies appearance, renamed text, condition, favorite state, contents and original ModData. The destination must be the newly created instance from the relevant action, with safe room in the main inventory and destination slot. An occupied destination is rejected normally; the other bag is never automatically displaced, unequipped or dropped. The 0.2.1 change avoids treating normal slot occupancy as a destination_occupied exception.
Other items, actions with no valid record, ordinary CopyClothing and unrelated recipes keep their original handling chain. Size changes retain native materials and costs. No global item-copy hook spreads upgrades. Consuming an upgraded bag in a new crafting recipe does not guarantee inheritance: for example, crafting another backpack from a vanilla survivor backpack is new crafting, not an audited size conversion. Restore it first.

Restoration and failure recovery
Restoration has no experience reward and is not a per-tier downgrade. Physical-capacity policies restore the original first-upgrade value; capacity-preserving policies never write capacity; the Raccoon City policy restores current sandbox behavior. The source clothing mod must remain installed.
Old schema1 records remain readable. Schema2 is written only after a successful later upgrade; there is no world scan or bulk rewrite. New records keep applied values, original values, policy version and safety-cap information. Damaged records reject payment. A legal record that no longer matches the current policy can still be restored.
Property setters are checked before crafting. A later failure independently attempts to recover the target and original material instances/thread uses. Swap/conversion failure also attempts to recover contents, the original worn slot and both hands. A new container still holding contents is not deleted. Recovery avoids retaining two separately redeemable refund entitlements.
Already emitted native events, experience and crafting history cannot all be undone. A permanent failure in an external setter may prevent recovery; the log reports failure. One successful command or action animation does not establish gameplay acceptance.

Debug and validation
Python is needed only for registry maintenance, not gameplay. Unknown IDs remain unsupported. The mod adds no periodic/world scan, loot-table changes or overwrites of Workshop source files. If the native recipe debug icon panel raises a setPlaceholderText null-reference error, use the debug item-list spawner to prepare items and then use the normal crafting panel. That debug-UI error is not proof of upgrade success or failure.
Disable Debug free-crafting/infinite-material settings when checking actual payment and refunds. Observe real inventory differences in the normal crafting panel. Restart the game completely before testing updated Lua. Representative v1.0.0 client checks and offline regression/source audits are separate; 172 supported IDs do not mean 172 individually tested items or complete save/reload/loading coverage. Multiplayer and dedicated servers remain unvalidated and their upgrade/restore preconditions are rejected. EX is not included.

Source and artwork
The source is public but has no separately attached open-source license. The cover, portrait and recipe icons were made with AI assistance using the maintainer-approved character reference. No blanket MIT or other asset license is granted. The original game's and supported mods' rights remain with their authors. See the linked asset notes for the boundaries.
