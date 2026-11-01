# ============================================================
# options.rpy —— 工程级配置（官方模板 + 手工改动清单）
# ============================================================
# 这里只放「整局生效、和剧情无关」的东西。改之前先确认该不该写在别的文件：
#   - 角色/立绘/站位/黑板图 → defines.rpy
#   - 音乐文件名在各场景里用 play music 现写，不在这里
#   - 语言与翻译相关 → i18n.rpy
#
# 我们动过的几处（Ren'Py 升级后重建模板时要搬回来）：
#   1) config.name（第 17 行附近）：标题栏与主页显示的游戏名，带 _() 要走翻译管线。
#   2) config.version："1.1"（第八·九轮后从 1.0 提上来），改了会显示在主菜单右下角。
#      这条**不带 _()**，不用走翻译管线。
#   3) config.main_menu_music = "audio/bgm_title.ogg"：主页 BGM，会一直延续进
#      游戏，直到剧情里 stop music / play music 换掉。
#   4) 紧随其后的两段 init：「关闭音乐」开关的实现，见 music_mute_apply 上方注释。
#   5) config.save_directory = "gui-7"：**别随便改**，改了老玩家的存档和
#      persistent（好感度、相册解锁、音乐开关）就找不到了。
#   6) gui.about 目前是空的，主页「关于游戏」只显示引擎默认内容。
#   7) config.has_voice = False + 文件里的 init 999 键表清空块：**完整删除 TTS 朗读**
#      （玩家 2026-10-23 要求）。has_sound/has_music 保持 True，BGM 和音效不受影响。
#      恢复朗读必须同时改三处，见那个块上方的注释。
# ============================================================

## This file contains options that can be changed to customize your
## game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't
## uncomment them. Lines beginning with a single '#' mark are
## commented-out code, and you may want to uncomment them when
## appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default
## window title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("导数物语 DERIVATIVE STORY")


## Determines if the title given above is shown on the main menu
## screen. Set this to False to hide the title.

define gui.show_name = True


## The version of the game.
## 第八·九轮（回忆三段 + 强制二选一 + 动画层）之后从 "1.0" 提到 "1.1"。

define config.version = "1.1"


## Text that is placed on the game's about screen. Place the text between
## the triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
""")


## A short name for the game used for executables and directories in the
## built distribution. This must be ASCII-only, and must not contain
## spaces, colons, or semicolons.

define build.name = "gui"


## Sounds and music ############################################################

## These three variables control, among other things, which mixers are
## shown to the player by default. Setting one of these to False will
## hide the appropriate mixer.

define config.has_sound = True
define config.has_music = True
# 本作没有任何配音（voice 通道从来没放过东西），而玩家 2026-10-23 明确说「声音不需要的」，
# 所以关掉 voice 混音：设置页那条「语音音量」滑条会随之消失（screens.rpy 的 if config.has_voice）。
define config.has_voice = False


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played
## while the player is at the main menu. This file will continue playing
## into the game, until it is stopped or another file is played.

define config.main_menu_music = "audio/bgm_title.ogg"

# 「关闭音乐」开关（设置页那个按钮改的是 persistent.music_off）。
# renpy.music.set_mute 在 8.5 不存在，只能用 preferences.set_mute(通道, bool)；
# 偏好是每档存档各自记的，所以要在 start / after_load 两个回调里重新应用，
# 否则读档后开关看着开着、音乐却照放。init 999 负责给老档补默认值。
init python:

    def music_mute_apply():
        off = bool(getattr(persistent, "music_off", False))
        preferences.set_mute("music", off)
        preferences.set_mute("main", off)

    config.start_callbacks.append(music_mute_apply)
    config.after_load_callbacks.append(music_mute_apply)

init 999 python:
    if persistent.music_off is None:
        persistent.music_off = False
    music_mute_apply()

## 彻底删掉 self-voicing（TTS 朗读）############################################################
##
## 玩家 2026-10-23 说「这个 self voice 可以完整删除了，声音不需要的」。本作没有任何配音，
## 朗读功能只会用系统 TTS 把对白念出来，属于噪音。删干净要动三处，缺一不可：
## 1) config.has_voice = False（上面）——设置页那条「语音音量」滑条消失。
## 2) 下面的 keymap 清空——否则 Alt+V / V / Shift+A / ? 还能把朗读或无障碍菜单叫出来，
##    而偏好一经翻转就会写进存档，读档后照样念。
##    ⚠ 键表本身在 common/00keymap.rpy 的 **init -1600 / -1100** 里填好，所以 init 999
##    一定改得到；但同文件 **init 1100** 在有 RENPY_DEFAULT_KEYMAP 环境变量时会把
##    config.keymap 整个重新赋值成 config.default_keymap（common/00keymap.rpy:471）。
##    解法不是把优先级顶到 1200（lint 会报「init priority 不在 -999~999」），
##    而是**两张表一起清**：keymap + default_keymap 都清空后，它爱怎么重新赋值都行。
##    （`config.emulated_keymap` 是旧引擎的东西，8.5 没有这个键，别照抄网上的写法。）
##    引擎的 Keymap.event 每次都走 renpy.map_event → 现读 config.keymap[name]，
##    清空列表 = 这个键永远匹配不上，不需要动 init -1100 挂的 _default_keymap 那个 underlay。
## 3) 下面的 self_voicing_off 回调——兜住「带着旧存档进来的玩家」：偏好是每档存档各自记的，
##    以前开过朗读的存档读进来仍然是开的，所以 start/after_load 都强制关一次。
## 顺带：renpy/display/tts.py 的 speak() 在 `not preferences.self_voicing` 时直接 return，
## 所以只要偏好为 False，即使有人用控制台打开也不会真的出声。
## related: screens.rpy 的帮助页里那两行（V self-voicing / Shift+A accessibility）已删；
##          tl/english/screens.rpy 的对应块靠 tools/drop_orphans.py 清孤儿。
init 999 python:

    for _km in (config.keymap, config.default_keymap):
        for _k in ("self_voicing", "clipboard_voicing", "debug_voicing", "extra_voicing",
                   "accessibility"):
            _km[_k] = []

    def self_voicing_off():
        ## self_voicing 可以是 True/False/"clipboard"/"debug"，一律压成 False。
        preferences.self_voicing = False

    config.start_callbacks.append(self_voicing_off)
    config.after_load_callbacks.append(self_voicing_off)
    ## init 里也立刻压一次：主菜单阶段的偏好是从 persistent 恢复的，老玩家如果以前误按过
    ## V，self_voicing=True 会跟着主菜单一起进来（start_callbacks 那时还没跑）。
    self_voicing_off()


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that
## no transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = None


## A variable to set the transition used when the game starts
## does not exist. Instead, use a with statement after showing
## the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again
## once dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any
## other number is the number of characters per second to type out.

default preferences.text_cps = 0


## The default auto-forward delay. Larger numbers lead to longer waits,
## with 0 to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save
## files for this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "gui-7"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution
## files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base
    ## directory, with and without a leading /. If multiple patterns match,
    ## the first is used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/**.ogg"
    ## matches ogg files in the game directory or any of its subdirectories, and
    ## "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app
    ## build, so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')


## A Google Play license key is required to perform in-app purchases.
## It can be found in the Google Play developer console,
## under "Monetize" > "Monetization Setup" > "Licensing".

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project,
## separated by a slash.

# define build.itch_project = "renpytom/test-project"
