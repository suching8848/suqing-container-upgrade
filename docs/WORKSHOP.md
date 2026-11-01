# Steam 创意工坊发布与更新

中文 | [English](WORKSHOP.en.md)

维护既有条目：[蘇清的容器升级 v1.0.1](https://steamcommunity.com/sharedfiles/filedetails/?id=3823988025)。工坊 ID 固定为 `3823988025`；Mod ID 保持 `SuQingContainerUpgrade_4221`。后续更新使用这个条目，不创建新 ID。

**本模组会极大影响游戏真实性与平衡性，请谨慎添加。适合喜欢大量收集、囤积物资的囤囤鼠玩家。** 容量和减重提升会明显削弱负重管理与搬运取舍的压力。

玩家安装请按 [README 中的 Steam 订阅或手动下载步骤](../README.md#安装与使用) 操作，两种来源选择一种即可。下面保留发布材料准备和后续更新流程；维护现有条目时应使用上述工坊 ID，不要再次创建新条目。

当前单人档的工坊部分见 [蘇清的自用模组合集](https://steamcommunity.com/sharedfiles/filedetails/?id=3823981387)；完整启用顺序、本地补丁与限制见 [当前单人档模组清单](current-single-player-modlist.md)。合集不能单独提供未发布本地补丁，也不能代替存档中的 Mod ID 启用顺序。

## 准备文件

在仓库根运行 Python 3，无需额外依赖：

```sh
python tools/prepare_workshop.py --check
```

上传目录为 `%UserProfile%\Zomboid\Workshop\SuQingContainerUpgrade`。更新前保留其中已有的 `workshop.txt` 及其 `id=3823988025`，将本次模组文件同步到同一目录下的 `Contents/mods/SuQingContainerUpgrade`，并同步介绍和更新说明。

上述检查不连接 Steam，也不上传、不改本地已启用模组、存档或启用名单。`prepare_workshop.py` 不带 `--check` 的模式仅用于创建尚不存在的上传目录，会拒绝覆盖既有目录；不应把它用于重建当前已分配 ID 的条目。若另建暂存目录，也须保留上述已有工坊 ID。

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

标题、介绍、标签和公开可见性会预填。512×512 PNG 预览图沿用选定封面，大小低于当前上传器的 1,024,000 字节限制；模组详情海报保留较大的版本。当前原生校验实际接受256或512正方形预览，界面的部分翻译仍只写256。

核对 `workshop.txt` 中仍为 `id=3823988025`。Mod ID `SuQingContainerUpgrade_4221` 与数字工坊 ID 是两件事，两者均保持原样。

## 游戏内操作

1. 保持 Steam 登录并正常启动游戏，进入主菜单 **创意工坊**。
2. 点 **创建/更新插件/项目**，选择 **SuQingContainerUpgrade**，点 **下一页**。
3. 核对已预填的标题、介绍、封面、标签，以及 **公开** 可见性，再点 **下一页**。
4. 确认更新既有工坊 ID **3823988025**，不选择创建新工坊 ID。
5. 到“准备发布”页后，可点 **编辑更新说明**，粘贴上传目录的 `changenote.txt`；再点 **上传到 Steam 创意工坊!**。
6. 等待成功提示，打开既有条目页面核对版本、介绍、封面和更新时间。文件校验通过不等于线上更新成功，上传成功也不等于游戏内验收完成。

这一流程按 Build 42.21 本机 `WorkshopSubmitScreen.lua` 和 `SteamWorkshopItem` 校验核对。v1.0.1 支持 172 个精确物品 ID；新增四项的离线验证与游戏内验收分开记录。HavenFall 大背包 EX 超级升级未纳入此包。

## 后续更新

保留上传目录的 `workshop.txt` 和已有数字 ID `3823988025`。更新同一条目，不再创建新 ID。

将新版模组文件更新到同一个 `Contents/mods/SuQingContainerUpgrade`，同步封面或介绍后，从同一目录进入上传器更新。脚本默认拒绝覆盖已有目录，避免误清已分配的 ID。

兼容原版容器不要求安装适配表中的全部第三方模组。不要把所有适配模组都设置为工坊必需依赖；原模组的物品仍由原作者提供。

发布后的订阅版与当前本地版使用同一 Mod ID。上传本身不需要迁移个人档；以后如改用订阅版，完全退出游戏后只保留一份该 ID 的安装来源，再核对启用名单。
