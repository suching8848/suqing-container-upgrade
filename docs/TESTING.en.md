# Testing scope and verification

[中文](TESTING.md) | English

## Known validation limits

- The target is Project Zomboid Build 42.21 single-player. The maintainer previously confirmed that v1.0.0 worked in their own single-player setup.
- In-game checks covered representative containers, successive upgrade tiers, restoration refunds and capacity displays. v1.0.3 supports 173 exact IDs; this does not mean every item, reload behavior, position combination or save-and-reload scenario has been tested in the game.
- Development also used the installed game JAR's script parser and Kahlua runtime for offline regression checks covering the whitelist, material transactions, old records, position changes, size conversions, dynamic capacity and refund failure paths. Offline fixtures do not establish successful game startup, persistence in a real save or correct visuals.
- Multiplayer and dedicated servers have not been validated. The current upgrade and restoration prechecks reject client or server environments; this release does not claim multiplayer support.

## Freshness lunchbox candidate acceptance in 1.0.3

The current companion is freshness lunchbox **0.1.0-rc.5**, with ordinary Container Upgrades **1.0.3**. Both are installed in the author's local single-player setup and remain unpublished. This update changes neither the exact supported ID nor upgrade rules. The rc.5 outline, five-tier/restoration behavior and full EX combination retain separate acceptance limits.

Offline checks cover the generated whitelist and six native recipes, an absent lunchbox provider, retention of all 172 prior IDs, five upgrades/restoration and payment ledgers. No world is created; parser or simulated-object results are not gameplay acceptance. The user checks empty/unhanded boxes through 12/20/30/40/49 and 90/93/95/97/99, actual 50% refunds, exact restoration of capacity 4 or the initialized sandbox baseline, freshness switches/progress and save/reload. Without the optional provider, existing vanilla containers must remain usable. Check the old WearableCompat ordinary-version gate separately from its EX bridge; the full EX gameplay combination remains unaccepted.

Generated consistency entry: `python SuQingContainerUpgrade/tools/build_compatibility.py --check`. This round's combined offline regression lives in the independent freshness-lunchbox project's `tools/integration_validate.py`; corresponding results are frozen in the test package. Candidate installation is not required.

## Acceptance limits for the v1.0.1 additions

Four ordinary-container integrations were moved from the existing independent compatibility patch into this release. Offline checks cover generated lists, recipe coverage, existing `mod_container` records, the injector case's size limit and front/back waist-bag conversion. This release was prepared without starting the game or opening the personal save. Injector filtering, actual material payments, upgrading and restoration, occupied destination slots and saving/reloading still need acceptance checks in an isolated single-player test save. EX upgrades for HavenFall's large backpacks are outside this release.

## Suggested in-game checks

Use a backed-up single-player test world with only one installed copy of this mod. Record original specifications, the resulting item state and actual material differences for each case.

1. **Ordinary light bags:** unequip, empty and place the bag in the main inventory. Check skill requirements, actual material consumption, capacity and weight reduction for tiers I–V. Test insufficient materials, selecting an old tier, cancelling the action and refusal at the maximum tier.
2. **Heavy bags and restricted containers:** check heavy bags whose safe maximum is 46–48, chest-rig item-size limits, ammunition-strap filters and the shoulder holster's two-pistol-magazine limit. Test existing reload and automatic-loading behavior separately according to the source mod's requirements.
3. **Bags with fluid storage:** a small amount of remaining fluid must block both upgrading and restoration. Empty all fluid before trying again. After refilling, fluid volume and fluid behavior must retain their original values.
4. **Native position and size changes:** use listed actions and check upgrade records, contents, favorite status, custom names and worn state. A front/back conversion must refuse an occupied destination slot without displacing or dropping the other bag.
5. **Dynamic and high native capacities:** check that Raccoon City sandbox capacity and character traits are applied once, and that the specified high-capacity bags retain their native physical capacity. Bags already meeting the ordinary tier-V targets must not be charged again.
6. **Restoration and payment ledger:** check a refund of half the newly recorded actual payments, rounded down separately. Thread is returned by uses and may produce a partial spool. Older payments without a ledger are not reconstructed. Repeating restoration after success must not duplicate a refund.
7. **Saving/reloading and old records:** record item specifications and material quantities before saving, then compare them after reloading. Check old records with backed-up test items rather than modifying the personal world to run acceptance tests.

Use Debug only to prepare items, skill levels and other test conditions. **Disable free crafting and unlimited materials when checking payments and the payment ledger.** Use the normal crafting panel and let actual material consumption finish. Free crafting cannot establish correct charging or refunds.

If the native recipe-debug icon panel raises a `setPlaceholderText` null-reference error, avoid that debug entry point. Prepare items with the item-list spawner, then use the normal crafting panel. That debug-UI error is not evidence of a successful or failed upgrade.

## Reporting problems

Provide the game build, mod version, full item ID, specifications before and after the action, Tailoring level, actual material differences and minimal reproduction steps. When another mod is involved, include its version and load order. Include only relevant log excerpts and remove private machine paths, account details and save information before submitting them.

An old tier remaining selectable, an action animation playing or a console command completing is not enough to establish success. Check the target instance's final properties, record and material changes.
