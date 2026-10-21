# 上传 Steam 创意工坊

当前仓库提供本地上传材料；存在这些材料不表示条目已经上传成功。

## 准备文件

在仓库根运行 Python 3，无需额外依赖：

```sh
python tools/prepare_workshop.py
python tools/prepare_workshop.py --check
```

默认创建 `%UserProfile%\Zomboid\Workshop\SuQingContainerUpgrade`。脚本不会连接 Steam，不会改本地已启用模组、存档或启用名单，也不会覆盖已有上传目录。

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

首次上传不填数字工坊 ID。Mod ID `SuQingContainerUpgrade_4221` 保持原样，与 Steam 分配的数字工坊 ID 是两件事。

## 游戏内操作

1. 保持 Steam 登录并正常启动游戏，进入主菜单 **创意工坊**。
2. 点 **创建/更新插件/项目**，选择 **SuQingContainerUpgrade**，点 **下一页**。
3. 核对已预填的标题、介绍、封面、标签，以及 **公开** 可见性，再点 **下一页**。
4. 首次上传选择 **这是一个新的 Steam 创意工坊插件/项目，创建一个新的 Steam 创意工坊 ID**。
5. 到“准备发布”页后，可点 **编辑更新说明**，粘贴上传目录的 `changenote.txt`；再点 **上传到 Steam 创意工坊!**。
6. 等待成功提示，打开条目页面核对名称和内容。如首次上传提示工坊协议，按 Steam 页面完成确认；未接受时条目可能仍被隐藏。

这一流程按 Build 42.21 本机 `WorkshopSubmitScreen.lua` 和 `SteamWorkshopItem` 校验核对。首次协议行为另见 [Steamworks 官方说明](https://partner.steamgames.com/doc/features/workshop/implementation#WorkshopLegalAgreement)。

## 后续更新

成功创建条目后，游戏会把数字 ID 写回上传目录的 `workshop.txt`。保留这份文件和 ID。以后更新同一条目，不再创建新 ID。

将新版模组文件更新到同一个 `Contents/mods/SuQingContainerUpgrade`，同步封面或介绍后，从同一目录进入上传器更新。脚本默认拒绝覆盖已有目录，避免误清已分配的 ID。

兼容原版容器不要求安装适配表中的全部第三方模组。不要把所有适配模组都设置为工坊必需依赖；原模组的物品仍由原作者提供。

发布后的订阅版与当前本地版使用同一 Mod ID。上传本身不需要迁移个人档；以后如改用订阅版，完全退出游戏后只保留一份该 ID 的安装来源，再核对启用名单。
