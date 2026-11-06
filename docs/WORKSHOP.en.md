# Steam Workshop publishing and updates

[中文](WORKSHOP.md) | English

当前源码与个人普通升级均为1.0.3，配套餐盒rc.5；已本地部署、尚未公开。本次只修订资料和冻结候选，不再改个人环境。 / Source and personal ordinary upgrades are 1.0.3 with lunchbox rc.5: installed locally, unpublished. This preparation updates copy and freezes a candidate without changing the personal setup.

Maintain the existing item: [SuQing Container Upgrade](https://steamcommunity.com/sharedfiles/filedetails/?id=3823988025). Its Workshop ID is fixed at `3823988025`; its Mod ID remains `SuQingContainerUpgrade_4221`. Update this item rather than creating a new ID.

**This mod greatly affects realism and game balance. Add it carefully. It is intended for players who enjoy collecting and stockpiling large quantities of items.** The capacity and weight-reduction increases substantially reduce the tradeoffs involved in carrying and transporting supplies.

For player installation, follow the [Steam subscription or manual download instructions in the README](../README.en.md); choose one source. The following instructions cover publishing preparation and later updates. Keep the existing Workshop ID when maintaining this item.

The Workshop portion of the current single-player setup is in [SuQing's personal mod collection](https://steamcommunity.com/sharedfiles/filedetails/?id=3823981387). See the [current single-player mod list](current-single-player-modlist.md) for the full enabled order, local patches and limits. The collection cannot supply unpublished local patches or replace the save's Mod ID order.

## Prepare and validate files

Run validation from the repository root with Python 3; no extra dependencies are required:

```sh
python tools/prepare_workshop.py --output release/1.0.3_20261106_ReleaseRepair/Workshop/SuQingContainerUpgrade --check
```

This candidate is staged separately at `release/1.0.3_20261106_ReleaseRepair/Workshop/SuQingContainerUpgrade`, retaining `id=3823988025`. Generated `release` files are excluded from Git. The old C-drive Workshop directory remains untouched and outdated; use the new candidate identified by its frozen manifest.

This check does not connect to Steam, upload files or modify local installations, saves or enable lists. Without `--check`, `prepare_workshop.py` creates only a nonexistent staging directory and writes the existing Workshop ID after checking the metadata. Use `--output release/<timestamp>/Workshop/SuQingContainerUpgrade` for a fresh directory, then check that same output path. It validates the combined bilingual description below 8000 UTF-8 bytes, the title, preview and source-file equality.

```text
SuQingContainerUpgrade/
├── workshop.txt
├── preview.png
├── changenote.txt
└── Contents/
    └── mods/
        └── SuQingContainerUpgrade/
            ├── common/
            └── 42/
                ├── mod.info
                ├── media/
                ├── icon.png
                └── poster.png
```

The title, description, tags and public visibility are prefilled. The preview is a 512×512 PNG derived from the selected cover, below the current uploader's 1,024,000-byte limit. The mod-details poster retains the larger version. The local Build 42.21 native validator accepts a 256- or 512-pixel square preview, although some translated UI text mentions only 256.

Verify that `workshop.txt` still contains `id=3823988025`. The Mod ID `SuQingContainerUpgrade_4221` and the numeric Workshop ID are different identifiers; retain both.

## Update the existing item in the game

The new candidate has not been copied into the game's scanned Workshop directory; the existing C-drive entry still contains the old package. Before using these steps, verify that the uploader actually points to the frozen new tree above. Do not upload directly from the old entry.

1. Keep Steam signed in. Start the game normally and open **Workshop** from the main menu.
2. Open **Create/update item**, select **SuQingContainerUpgrade**, then continue.
3. Review the prefilled title, description, cover, tags and **Public** visibility, then continue.
4. Confirm that the update targets existing Workshop ID **3823988025**. Do not select the option to create a new Workshop ID.
5. On the ready-to-publish page, edit the change notes using the upload directory's `changenote.txt`, then upload to Steam Workshop.
6. Wait for a success message, then open the existing item and verify its version, description, cover and update time. File validation does not establish a successful online update, and an upload does not establish in-game acceptance.

These steps were checked against the local Build 42.21 `WorkshopSubmitScreen.lua` and `SteamWorkshopItem` validation. v1.0.3 supports 173 exact item IDs. Offline checks and in-game acceptance for the four earlier items and this lunchbox are recorded separately. EX super upgrades for HavenFall's large backpacks are outside this package.

## Later updates

Preserve the upload directory's `workshop.txt` and existing numeric ID `3823988025`. Update the same item rather than creating another ID.

Copy the new mod files into the same `Contents/mods/SuQingContainerUpgrade`, update the cover or description as needed, and use the uploader with that directory. The preparation script refuses to overwrite existing directories by default, protecting the assigned ID from accidental removal.

Using vanilla containers does not require every third-party mod in the compatibility table. Do not mark every optional integration as a required Workshop dependency; the original mods still provide their own items.

The subscription and local versions use the same Mod ID. Uploading does not require migrating the personal save. If switching to the subscribed version later, fully exit the game, retain only one installed source for that Mod ID, then check the enabled-mod lists.
