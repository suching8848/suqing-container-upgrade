# 前置、补丁与加载关系 | Requirements, Patches and Load Relationships

[中文 README](../README.md) · [English README](../README.en.md) · [补丁合集 / Patch collection](https://github.com/suching8848/suqing-project-zomboid-patches)

## 中文

普通容器升级的 Mod ID 是 `SuQingContainerUpgrade_4221`。基础功能不强制依赖补丁合集；升级某个模组的容器时，必须另装提供该物品的原模组。当前源码与作者本地普通升级均为 **1.0.3 未发布候选**，配套餐盒为rc.5；不要用历史旧包覆盖当前源码或安装。

| 使用场景 | 所需项目与补丁 | 性质及加载关系 |
| --- | --- | --- |
| 普通已适配容器强化、还原 | 本模组；目标物品所属原模组 | 基础功能，无额外通用补丁前置 |
| 返鲜餐盒的普通五档与还原 | 本模组1.0.3候选及独立 `SuQingFreshnessLunchbox` | 精确ID内置原生配方，无需独立餐盒兼容子模组；返鲜盒来源不是其他容器的强制前置 |
| 注射器盒、Chemical 胸挂、HavenFall 前后腰包的普通升级 | 对应物品来源模组 | 1.0.1 已内置四项精确 ID 的普通升级适配；仅为它们进行普通升级，无须另装旧注册桥接 |
| 针剂轻量化、肾上腺素笔及额外针剂盒收纳兼容 | 合集中的 `Codex_StimCompatibility_4221`；其声明前置 `TarkovCombatStims,AdrenalineShot` | 独立小扩展，按其文档使用；不是普通容器升级的基础前置 |
| HavenFall 大背包的 EX 超级升级桥接 | [背包超级升级](https://github.com/suching8848/suqing-backpack-super-upgrade) 与 `Codex_SuQingWearableCompat_4221` | 条件补丁；它声明依赖普通升级、EX 和 `HavenFall`，必须先满足这些前置。旧普通注册适配器只接受 1.0.0，在 1.0.1/1.0.3 会因版本门禁跳过普通注册；独立 EX 桥接仍按其 EX 版本检查工作 |
| 猫又背包的 EX 超级升级 | [EX 项目说明](https://github.com/suching8848/suqing-backpack-super-upgrade) 及其猫又兼容/升级补丁 | 属于 EX 体系，不由普通容器升级提供 |
| 自动发现未知容器 | [容器自动识别实验版](https://github.com/suching8848/suqing-container-auto-upgrade) | 替代实验项目，不是普通版的必装补丁。不要同时启用两套普通升级实现；遵循实验版说明 |

补丁合集中的每项仍是独立 Mod ID，不能把整个合集当成一个全选安装包。按目标项目说明启用必要子项，满足声明前置并让桥接在被桥接的主模组之后加载；不要重排其他已有模组。`Codex_SuQingWearableCompat_4221` 的 HavenFall 桥接有 EX 版本校验，升级 EX 后应重新核对。

2026-11-06只读核对：现用旧补丁的 `Codex_SuQingHavenFallEX.lua` 独立要求EX版本 `1.0.0-rc.2`，并校验HavenFall20个原生容量变体、配方、猫又包装链和hook身份；它不以普通核心版本为总开关。个人普通已部署1.0.3，旧补丁保持；1.0.3不放宽旧门禁，也不把整项补丁标为冗余。完整新旧EX组合仍待用户游戏内验收。

当前单人档的实际启用顺序见 [清单](current-single-player-modlist.md)。源码归档和离线校验不代表所有可选组合都经过游戏内验证。

## English

The main Mod ID is `SuQingContainerUpgrade_4221`. Basic upgrades do **not** require the patch collection. To upgrade another mod's item, install its original item provider separately. The source and author's installed ordinary upgrade are both the **unpublished 1.0.3 candidate**, with lunchbox rc.5. Do not overwrite current source or installation with historical packages.

| Scenario | Required projects or patches | Relationship |
| --- | --- | --- |
| Upgrade and restore supported ordinary containers | This mod and the original provider of each target item | No additional universal patch requirement |
| Ordinary five tiers/restoration for the freshness lunchbox | This 1.0.3 candidate and independent `SuQingFreshnessLunchbox` | Exact ID built into native recipes; no separate lunchbox adapter. Its optional provider is not required for other containers |
| Ordinary upgrades for the injector case, Chemical rig and HavenFall rear/front waist packs | Their original item providers | Version 1.0.1 already registers all four exact IDs; ordinary upgrades alone do not require the old registration bridge |
| Stim weight changes, Adrenapen integration and additional injector-case compatibility | `Codex_StimCompatibility_4221`, with its declared requirements `TarkovCombatStims,AdrenalineShot` | Separate optional extension; not a prerequisite for basic container upgrades |
| EX upgrades for HavenFall large backpacks | [Backpack Super Upgrades](https://github.com/suching8848/suqing-backpack-super-upgrade) and `Codex_SuQingWearableCompat_4221` | Conditional bridge declaring the ordinary mod, EX and `HavenFall` as requirements. The old ordinary-registration adapter only accepts 1.0.0 and declines ordinary registration on 1.0.1/1.0.3; the separate EX bridge still performs its own EX-version checks |
| EX upgrades for Nekomata backpacks | The [EX project](https://github.com/suching8848/suqing-backpack-super-upgrade) and its Nekomata compatibility/extension patches | Part of the EX system, not provided by ordinary upgrades |
| Automatic discovery of unknown containers | [Automatic Container Upgrades — Experimental](https://github.com/suching8848/suqing-container-auto-upgrade) | Alternative experimental implementation, not a required patch. Do not enable both ordinary upgrade implementations together |

Every collection entry retains its own Mod ID. Select the entries required by your scenario, satisfy their declared dependencies and load integration bridges after their host mods without reorganizing unrelated entries. The HavenFall EX bridge checks the EX version and needs review when EX changes.

Read-only audit on 2026-11-06: the installed patch's `Codex_SuQingHavenFallEX.lua` independently requires EX `1.0.0-rc.2` and validates 20 native-capacity HavenFall variants, recipes, MaoMao wrapper ownership and hook identities. It does not use the ordinary core version as a global off switch. The personal ordinary mod is now 1.0.3; the old patch remains unchanged. This candidate neither relaxes their gates nor labels the entire patch redundant; the complete gameplay combination remains unaccepted.

The [enabled-list snapshot](current-single-player-modlist.md) records the author's actual order. Source synchronization and offline checks do not establish in-game acceptance of every optional combination.
