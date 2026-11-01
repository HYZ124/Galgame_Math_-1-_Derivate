# 导数物语 (DERIVATIVE STORY)

> **“在函数的极限处，遇见关于你的解。”**  
> 一款结合高中微积分（导数）学习与选择支恋爱的视觉小说（galgame），基于 **Ren'Py 8.5.3** 引擎制作。

---

## 📖 游戏简介

玩家将扮演一名面临高考/期末挑战的高中生，在上完 7 节“导数课”的过程中，与两位性格迥异的女主角展开故事：
- **云曦**：古风白发少女，神秘地“附身”在黑板与数学公式之间。
- **苏知微**：严谨的眼镜社长，冷静理智的数学学霸。

在解题、上课与课后约会中积累经验与好感度，你的选择与答题表现将决定走向 **云曦线**、**社长线** 或 **中立线**。

---

## 🚀 快速开始与运行指南

### 1. 安装 Ren'Py 引擎
本游戏基于 **Ren'Py 8.5.3** 开发。请根据你的操作系统下载并安装 SDK：

1. 前往 [Ren'Py 官方下载页面](https://www.renpy.org/latest.html)。
2. 下载适用于你系统（Windows / macOS / Linux）的 **Ren'Py SDK 8.x** 版本并解压安装。

### 2. 运行游戏
有以下两种运行方式：

#### 方式 A：通过 Ren'Py SDK 启动（推荐）
1. 打开 Ren'Py SDK 启动器。
2. 点击 **“Preferences” -> “Projects Directory”**，将本项目的根目录 `galgame-math/` 所在的文件夹添加进来。
3. 在左侧项目列表中选择 **`galgame-math`**，点击 **“Launch Project”（启动项目）** 即可。

#### 方式 B：直接启动可执行文件
如果你使用的是打包好的游戏版本，直接点击 `/game/` 同级目录下的项目启动程序（或点击 `/game/` 内部的主脚本入口）即可运行。

---

## 📂 项目目录结构

```text
galgame-math/
├── game/                          ← 游戏核心逻辑与全部资源
│   ├── script.rpy                 ← 主流程控制 (start -> prologue -> lesson1..7 -> finale -> epilogue)
│   ├── math_core.rpy              ★ 做题引擎：题库切片、判题逻辑、MC/IN 答题界面、practice()
│   ├── love.rpy                   ★ 恋爱系统：好感度管理 (love_yx/love_zw)、相册与 CG 回放
│   ├── prelude.rpy                ← 每课前置小剧情与题型讲解
│   ├── defines.rpy                ← 角色立绘定义、全局变量与好感度初始化
│   ├── options.rpy                ← 基础配置（分辨率、主菜单音乐、音量静音逻辑）
│   ├── screens.rpy                ← UI 界面定义（主菜单、设置、答题 UI、静音开关）
│   ├── title_fx.rpy               ← 主菜单 Visual 效果（鼠标视差、粒子浮尘等 ATL 变换）
│   ├── i18n.rpy                   ← 多语言国际化辅助
│   ├── gui.rpy / guisupport.rpy   ← Ren'Py 默认 GUI 框架支持文件
│   │
│   ├── lessons/                   ← 7 节课对应题库
│   │   ├── lN_xxx.rpy             ← 中文题目与解析 (Lesson 1 ~ 7)
│   │   └── lN_en.rpy              ← 英文题库支持
│   │
│   ├── scenes/                    ← 剧情文本拆分
│   │   ├── tutorial.rpy           ← 开局教学
│   │   ├── dates.rpy              ← 4 段角色约会剧情
│   │   ├── sides.rpy              ← 课后日常小插曲
│   │   ├── interlude.rpy          ← 6 段转场间幕
│   │   └── ending.rpy             ← 三线结局 + 第二部预告
│   │
│   ├── audio/                     ← 音效与 BGM（含 6 首 .ogg 主题音乐）
│   ├── images/                    ← 游戏美术资源
│   │   ├── characters/            ← 角色立绘
│   │   ├── backgrounds/           ← 场景背景
│   │   ├── blackboard/            ← 黑板板书与数学图表
│   │   ├── story/                 ← 剧情 CG (scg1 ~ scg9)
│   │   └── memories/              ← 回忆相册照片 (mem1 ~ mem11)
│   └── fonts/                     ← 游戏字体文件（包含中文黑体）
