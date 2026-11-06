# 蘇清的容器升级模组 | SuQing's Container Upgrades Mod

[简体中文](README.md) · [English](README.en.md)

> **This mod greatly changes realism and balance. Add it with care. It is intended for players who enjoy collecting and stockpiling supplies.**
>
> Larger capacities and strong weight reduction substantially ease inventory management and transport decisions. Choose it to suit your play style.

<p align="center"><img src="docs/images/cover.png" alt="SuQing's Container Upgrades cover" width="760"></p>

**v1.0.3 · Project Zomboid Build 42.21 · Single-player**

Upgrade existing wearable containers and the specified single-handed freshness lunchbox with clean ripped sheets, leather strips and thread. The original item and its functions remain in place. Recipes use the native crafting category and quick-crafting entry points.

An earlier [Steam Workshop release](https://steamcommunity.com/sharedfiles/filedetails/?id=3823988025) is available; GitHub provides the source and files for manual installation. The 1.0.3 candidate is unpublished and does not include EX upgrades.

Publication status (2026-11-06): three native attempts to upload 1.0.3 explicitly failed; the online item remains 1.0.1. Retry the same Workshop ID after the user switches nodes. Prepared source/local files and Git synchronization do not establish a successful Workshop update. See [publication status](publishing/release-status-20261106.json).

## The author’s historical single-player setup and collection

[Workshop collection](https://steamcommunity.com/sharedfiles/filedetails/?id=3823981387) · [Single-player enabled snapshot: 205 IDs on 2026-11-02 01:10 UTC+08:00](docs/current-single-player-modlist.md) · [Ten source repositories and 42 Mod IDs](docs/project-index.md)

The historical snapshot from 2026-11-02 01:10 UTC+08:00 contains **205 Mod IDs, 161 Workshop items and 33 separately installed local mods or patches not included in collection downloads**; these are not current counts. The author previously reported normal play with their full B42.21 single-player setup; this is not individual acceptance of every project or new version. Multiplayer and dedicated servers remain untested.

Source repositories are now linked for the local projects. Subscribing to the Steam collection alone still does not reproduce the full setup. See [requirements and patch relationships](docs/PATCH_DEPENDENCIES.md) for mandatory dependencies and conditional integrations.

## Features and supported scope

- Explicit support for **173 exact item IDs: 84 vanilla and 89 audited mod items**. Facing, size and color variants count separately.
- Five upgrade tiers, restoration to the original pre-upgrade specification, and a refund after successful restoration.
- Supported front/back swaps, same-ID clothing replacements and **8 native size-conversion recipes** preserve valid upgrade records.
- The two Raccoon City containers retain their sandbox and character-trait calculations; their existing capacity tooltip line is corrected.
- Dedicated portrait, upgrade/restore icons and cover. No custom context menu, extra tier tooltip area or success/failure floating text.

See the [173 supported IDs](SuQingContainerUpgrade/最终适配物品名单.txt) and the [complete classification of 192 entries and restrictions](SuQingContainerUpgrade/适配名单.csv). The latter also contains 1 restore-only entry and 18 exclusions. Unknown IDs are unsupported.

Specified containers from Fantasy Workshop, 2DimensionWardrobe, Backpack System, SuPrimitiveEquipment, They Knew Continued, Raccoon City, SafeWayHamlet and MFS are supported. **You do not need all these mods to upgrade vanilla containers.** Each source mod still supplies its own items.

### Built-in freshness lunchbox support in 1.0.3 (unpublished candidate)

The current companion is freshness lunchbox **0.1.0-rc.5**, with ordinary Container Upgrades **1.0.3**. Both are installed in the author's local single-player setup and remain unpublished. This update changes neither the exact supported ID nor upgrade rules. The rc.5 outline, five-tier/restoration behavior and full EX combination retain separate acceptance limits.

Adds the exact `SuQingFreshnessLunchbox.FreshnessLunchbox` ID to the native five upgrade recipes and restoration recipe. No separate lunchbox adapter is needed. The independent `SuQingFreshnessLunchbox` mod still supplies the item; existing containers remain usable when that optional provider is absent.

Food filtering, maximum item size 1, the absence of wearable slots and left/right single-hand appearances are retained. Empty the box, remove it from both hands and put it in the main inventory before upgrading. Materials, skills, actual-payment ledgers and 50% paid-material refunds stay unchanged. The first upgrade records the instance's actual baseline; restoration returns to that baseline while retaining freshness switches, progress and other ModData. The default lunchbox capacity is 4, but an initialized sandbox baseline or existing upgrade is never forcibly reset to 4.

Version 1.0.3 was installed in the author's local single-player setup on 2026-11-06 and remains unpublished. This preparation updates documentation and freezes a candidate without changing personal installation or enable lists. The four wearable integrations built into 1.0.1 remain. The existing `Codex_SuQingWearableCompat_4221` ordinary adapter accepts only 1.0.0 and keeps its original refusal on 1.0.3. Its separate HavenFall large-backpack EX bridge independently checks EX `1.0.0-rc.2`, source definitions and wrapper ownership. Do not disable the entire patch merely because ordinary registrations are built in. This preparation does not change that bridge; complete gameplay-combination acceptance remains pending.

### Added in 1.0.1

- `CombatStims.InjectorCase`: injector case; retains the upstream injector filter and maximum item size **10**. Extra Adrenapen storage remains part of a separate compatibility patch.
- `CodexCBRT.SST02_ChestRig`: combat rig from the independent Chemical compatibility build. It requires that build; this mod does not distribute third-party equipment assets.
- `ESHF.Qwe_Backpack` and `ESHF.Qwe_BackpackFront`: HavenFall rear/front waist packs. Valid upgrade records and destination-slot protection are preserved during supported swaps.

Materials, skills, payment ledgers and restoration refunds are unchanged. Valid records previously written by the independent compatibility patch remain usable. HavenFall large-backpack EX upgrades remain a separate extension. These four integrations are optional and require their source mods.

## Five tiers and costs

Each row is the cost of that individual tier, not a cumulative total. Capacity and weight reduction are target minimums; higher existing values are preserved.

| Tier | Nominal base capacity | Weight reduction | Clean ripped sheets | Leather strips | Thread uses | Tailoring level |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| I | 12 | 90% | 4 | 0 | 2 | 0 |
| II | 20 | 93% | 6 | 2 | 4 | 1 |
| III | 30 | 95% | 10 | 4 | 6 | 2 |
| IV | 40 | 97% | 14 | 6 | 8 | 3 |
| V | Up to 49 | 99% | 20 | 10 | 10 | 4 |

The needle is retained. A full ordinary `Base.Thread` spool has **20 uses**: the table counts uses, not spools. Material IDs are `Base.RippedSheets`, `Base.LeatherStrips` and `Base.Thread`; needles use the native sewing-needle tag.

A tier is skipped when both capacity and weight reduction already meet it. Only the actual next tier is charged. A higher value in either attribute is never reduced.

Ordinary tier V reaches at most base capacity 49. Some heavy bags retain their actual weight and use the safety cap `floor(50 - item weight)`, so their final capacity can be **46, 47 or 48**. Character traits still affect effective capacity. Specified native 50/60-capacity bags receive weight reduction only; their physical capacity is unchanged. The two Raccoon City containers preserve larger sandbox base values. Consult the item list for exact policies.

## Installation and use

Choose **either Steam subscription or a manual Git download**. Both use Mod ID **`SuQingContainerUpgrade_4221`**; keep only one installation source for that ID. Before switching, fully exit the game, back up the save and old files, move duplicate local copies out of the mod directory, and disable old test versions.

### Steam subscription

1. Open the [Workshop page](https://steamcommunity.com/sharedfiles/filedetails/?id=3823988025) and select **Subscribe**.
2. Wait for Steam to finish downloading, then launch Build 42.21.
3. Enable SuQing's Container Upgrades in both the game mod list and the target single-player save's mod management.
4. Fully exit and restart the game so the new Lua and resources load, then enter the target save.

### Manual Git download

1. Select **Code → Download ZIP**. Extract it and copy the **`SuQingContainerUpgrade` folder** to `%UserProfile%\Zomboid\mods\`.
2. Check for `%UserProfile%\Zomboid\mods\SuQingContainerUpgrade\42\mod.info`, keeping sibling folders such as `common`. The repository root itself is not the mod folder.
3. Enable the mod in the game list and the target single-player save, then fully exit and restart. Manual installations require manually downloading future updates.

### Upgrading an item

Unequip the container, place it in the character's main inventory and remove all contents. Prepare the materials and select the current next tier in the **“蘇清”** crafting category. Vanilla containers do not require all optional source mods.

**Fluid containers such as hydration backpacks and rigs must have all liquid drained before upgrading or restoring.** Removing ordinary items is insufficient: even a little remaining water or other fluid blocks crafting. Only ordinary-item storage improves; fluid capacity and components are unchanged.

Old tiers may still appear selectable in the crafting panel. Cached candidates do not establish that the current item can perform that tier. Only its next tier is allowed; old tiers are rejected without payment. A queued native action may still take time. The end of an animation alone does not prove success.

Before swapping a front/back pack, unequip any other pack from the destination slot into the main inventory. An occupied slot is rejected normally; the other pack is not displaced or dropped.

## Restoration and refunds

Empty and unequip the container, then use the recipe to restore its first pre-upgrade specification. This is a full restoration, not a step-down recipe, and grants no experience.

A successful restoration refunds **50% of each material's cumulative actual payment in a valid ledger, rounded down separately**. Cloth and leather are returned as items; thread is returned in uses and can produce a partial spool. Actually paying all five tiers costs 54 cloth, 22 leather and 30 thread uses, yielding 27 cloth, 11 leather and 15 thread uses on restoration.

Only successfully consumed materials are recorded. Skipped tiers, free crafting and operations with no actual consumption create no refund entitlement. Older payments without a ledger are not reconstructed. Valid ledgers from 0.2.2 remain supported: for example, if only tier V was paid after an unrecorded old tier IV, only half of that tier-V payment is refunded. Successful restoration clears the ledger, preventing repeated collection. Crafting cancellation does not use this 50% refund rule.

Disabling the mod does not automatically restore saved physical attributes. Restore items as needed before removing it, and keep the mod that supplies the container.

## Preserved functions and restrictions

Upgrades change managed capacity, weight reduction and this mod's records on the original item instance. Original weight, name, appearance, condition, favorite state, clothing slots, attachment points and other ModData are retained.

- Reload tags, MFS automatic-loading checks and loading logic are unchanged. More storage does not increase rounds loaded per animation.
- Rig item-size limits, ammunition-belt filters and the shoulder holster's maximum of **2 pistol magazines** remain active.
- Only audited native swaps and size conversions preserve records. Other crafting recipes consuming an upgraded bag need not transfer them to the new product; restore it first.
- The six 踏行千山 containers and vanilla crude leather/tarp bags retain their own native upgrade chains instead of paid upgrades. 踏行千山五 is restore-only for valid old records.
- The 10 Legendary Backpack colors and Estate 39's Miku bag already meet ordinary targets and are excluded from paid upgrading. Unlisted non-wearable crates are outside the scope; the exact registered freshness lunchbox is a separate exception.

### Loaded containers on the ground cannot be picked up or worn

An unequipped container weighs its own weight **plus all its contents**. The usual main-inventory pickup capacity is **50**, separate from the character's comfortable carrying limit shown in the inventory panel. Picking up a container checks the character's current carried weight plus the container's full unequipped weight against that capacity.

Choosing **Wear** on a ground item first transfers it into the main inventory, then equips it. The pickup check therefore happens before the equipped weight reduction applies. Higher storage capacity and stronger weight reduction do not exempt an unequipped container from this check.

To recover the container, temporarily move some contents from it to the ground or another external container, or put other carried items into external storage. Once the pickup fits, pick up and wear the container, then return the contents. Simply moving contents from the ground bag into the character's main inventory usually leaves the combined weight unchanged and does not solve the pickup limit.

## Validation scope

The maintainer confirmed normal use of **v1.0.0 in their own Build 42.21 single-player environment**, covering representative items. v1.0.1 incorporated four ordinary integrations from an existing independent patch. Offline checks and gameplay acceptance for the additions are tracked separately. The support count of 173 **does not mean every item has been tested individually**, or that all reload, save/reload or mod-combination scenarios have passed.

This release is single-player only. Multiplayer and dedicated servers are unvalidated; the current preconditions do not allow upgrading or restoration in multiplayer. See [testing guidance](docs/TESTING.en.md).

## Maintaining the supported list

`SuQingContainerUpgrade/compatibility/registry.json` is the single registry source. From the repository root, use Python 3:

```sh
cd SuQingContainerUpgrade
python tools/build_compatibility.py
python tools/build_compatibility.py --check
```

The generator updates the runtime allowlist, six recipes and readable lists. `--check` only verifies that generated outputs match. Scope changes must also audit original capacity, restrictions, native upgrade chains and swap/size-conversion behavior. Python is not required while playing.

## Source and assets

The repository currently has no open-source license attached. Icons and cover artwork were made with AI assistance. The original game and supported mods belong to their authors. See [asset notes](docs/ASSETS.en.md).

See [CHANGELOG](CHANGELOG.md) for release history and the [Workshop guide](docs/WORKSHOP.en.md) for publishing and updates. `tools/prepare_workshop.py` prepares the upload folder recognized by the game.
