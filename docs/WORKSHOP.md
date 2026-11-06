# Steam 创意工坊发布与更新

中文 | [English](WORKSHOP.en.md)

当前源码与个人普通升级均为1.0.3，配套餐盒rc.5；已本地部署、尚未公开。本次只修订资料和冻结候选，不再改个人环境。 / Source and personal ordinary upgrades are 1.0.3 with lunchbox rc.5: installed locally, unpublished. This preparation updates copy and freezes a candidate without changing the personal setup.

维护既有条目：[蘇清的容器升级](https://steamcommunity.com/sharedfiles/filedetails/?id=3823988025)。工坊 ID 固定为 `3823988025`；Mod ID 保持 `SuQingContainerUpgrade_4221`。后续更新使用这个条目，不创建新 ID。

**本模组会极大影响游戏真实性与平衡性，请谨慎添加。适合喜欢大量收集、囤积物资的囤囤鼠玩家。** 容量和减重提升会明显削弱负重管理与搬运取舍的压力。

玩家安装请按 [README 中的 Steam 订阅或手动下载步骤](../README.md#安装与使用) 操作，两种来源选择一种即可。下面保留发布材料准备和后续更新流程；维护现有条目时应使用上述工坊 ID，不要再次创建新条目。

当前单人档的工坊部分见 [蘇清的自用模组合集](https://steamcommunity.com/sharedfiles/filedetails/?id=3823981387)；完整启用顺序、本地补丁与限制见 [当前单人档模组清单](current-single-player-modlist.md)。合集不能单独提供未发布本地补丁，也不能代替存档中的 Mod ID 启用顺序。

## 准备文件

在仓库根运行 Python 3，无需额外依赖：

```sh
python tools/prepare_workshop.py --output release/1.0.3_20261106_ReleaseRepair/Workshop/SuQingContainerUpgrade --check
```

本次新候选单独保存在仓库 `release/1.0.3_20261106_ReleaseRepair/Workshop/SuQingContainerUpgrade`，包含既有 `id=3823988025`。`release`是本地生成目录，不纳入Git。C盘旧Workshop入口仍为历史版本，没有覆盖；应以冻结清单标出的新候选为准，不直接上传旧树。

上述检查不连接 Steam，也不上传、不改本地已启用模组、存档或启用名单。`prepare_workshop.py` 不带 `--check` 时只创建尚不存在的目录，拒绝覆盖，且从元数据校验并写入既有工坊ID。可用 `--output release/<日期时间>/Workshop/SuQingContainerUpgrade` 准备新暂存目录，再用相同路径加 `--check` 复核。脚本同时检查中英合并介绍小于8000个UTF-8字节、标题、预览图及逐文件一致性。

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

本轮尚未将新候选接入游戏扫描的Workshop目录；当前C盘同名入口仍是旧包。后续发布须先核对上传器实际使用的是上述冻结新树，再执行下列步骤，不能直接从旧入口上传。

1. 保持 Steam 登录并正常启动游戏，进入主菜单 **创意工坊**。
2. 点 **创建/更新插件/项目**，选择 **SuQingContainerUpgrade**，点 **下一页**。
3. 核对已预填的标题、介绍、封面、标签，以及 **公开** 可见性，再点 **下一页**。
4. 确认更新既有工坊 ID **3823988025**，不选择创建新工坊 ID。
5. 到“准备发布”页后，可点 **编辑更新说明**，粘贴上传目录的 `changenote.txt`；再点 **上传到 Steam 创意工坊!**。
6. 等待成功提示，打开既有条目页面核对版本、介绍、封面和更新时间。文件校验通过不等于线上更新成功，上传成功也不等于游戏内验收完成。

这一流程按 Build 42.21 本机 `WorkshopSubmitScreen.lua` 和 `SteamWorkshopItem` 校验核对。v1.0.3 支持 173 个精确物品 ID；此前四项与本次返鲜餐盒的离线验证、游戏内验收分开记录。HavenFall 大背包 EX 超级升级未纳入此包。

## 后续更新

保留上传目录的 `workshop.txt` 和已有数字 ID `3823988025`。更新同一条目，不再创建新 ID。

将新版模组文件更新到同一个 `Contents/mods/SuQingContainerUpgrade`，同步封面或介绍后，从同一目录进入上传器更新。脚本默认拒绝覆盖已有目录，避免误清已分配的 ID。

兼容原版容器不要求安装适配表中的全部第三方模组。不要把所有适配模组都设置为工坊必需依赖；原模组的物品仍由原作者提供。

发布后的订阅版与当前本地版使用同一 Mod ID。上传本身不需要迁移个人档；以后如改用订阅版，完全退出游戏后只保留一份该 ID 的安装来源，再核对启用名单。
