# Steam Workshop publishing and updates

[中文](WORKSHOP.md) | English

Maintain the existing item: [SuQing Container Upgrade v1.0.1](https://steamcommunity.com/sharedfiles/filedetails/?id=3823988025). Its Workshop ID is fixed at `3823988025`; its Mod ID remains `SuQingContainerUpgrade_4221`. Update this item rather than creating a new ID.

**This mod greatly affects realism and game balance. Add it carefully. It is intended for players who enjoy collecting and stockpiling large quantities of items.** The capacity and weight-reduction increases substantially reduce the tradeoffs involved in carrying and transporting supplies.

For player installation, follow the [Steam subscription or manual download instructions in the README](../README.en.md); choose one source. The following instructions cover publishing preparation and later updates. Keep the existing Workshop ID when maintaining this item.

The Workshop portion of the current single-player setup is in [SuQing's personal mod collection](https://steamcommunity.com/sharedfiles/filedetails/?id=3823981387). See the [current single-player mod list](current-single-player-modlist.md) for the full enabled order, local patches and limits. The collection cannot supply unpublished local patches or replace the save's Mod ID order.

## Prepare and validate files

Run validation from the repository root with Python 3; no extra dependencies are required:

```sh
python tools/prepare_workshop.py --check
```

The upload directory is `%UserProfile%\Zomboid\Workshop\SuQingContainerUpgrade`. Preserve its existing `workshop.txt` and `id=3823988025`. Copy the release's mod files into the same directory's `Contents/mods/SuQingContainerUpgrade`, and update the description and change notes.

This check does not connect to Steam, upload files or modify enabled local mods, saves or enabled-mod lists. Without `--check`, `prepare_workshop.py` only creates a directory that does not already exist and refuses to overwrite an existing one. Do not use that mode to recreate this already-published item. If a separate staging directory is needed, retain the existing Workshop ID above.

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

1. Keep Steam signed in. Start the game normally and open **Workshop** from the main menu.
2. Open **Create/update item**, select **SuQingContainerUpgrade**, then continue.
3. Review the prefilled title, description, cover, tags and **Public** visibility, then continue.
4. Confirm that the update targets existing Workshop ID **3823988025**. Do not select the option to create a new Workshop ID.
5. On the ready-to-publish page, edit the change notes using the upload directory's `changenote.txt`, then upload to Steam Workshop.
6. Wait for a success message, then open the existing item and verify its version, description, cover and update time. File validation does not establish a successful online update, and an upload does not establish in-game acceptance.

These steps were checked against the local Build 42.21 `WorkshopSubmitScreen.lua` and `SteamWorkshopItem` validation. v1.0.1 supports 172 exact item IDs. Offline checks and in-game acceptance for the four additions are recorded separately. EX super upgrades for HavenFall's large backpacks are outside this package.

## Later updates

Preserve the upload directory's `workshop.txt` and existing numeric ID `3823988025`. Update the same item rather than creating another ID.

Copy the new mod files into the same `Contents/mods/SuQingContainerUpgrade`, update the cover or description as needed, and use the uploader with that directory. The preparation script refuses to overwrite existing directories by default, protecting the assigned ID from accidental removal.

Using vanilla containers does not require every third-party mod in the compatibility table. Do not mark every optional integration as a required Workshop dependency; the original mods still provide their own items.

The subscription and local versions use the same Mod ID. Uploading does not require migrating the personal save. If switching to the subscribed version later, fully exit the game, retain only one installed source for that Mod ID, then check the enabled-mod lists.
