# ============================================================
# 《导数物语》角色 / 图片 / 站位定义
#
# 【加一张立绘要动的四处】
#   1. 出图：640×960 透明 PNG，脚贴底边、头部居中（半身像同画布，见 README
#      「半身像美术层」的提示词模板 + tools/bust_sprites.py 抠图入库）。
#   2. 本文件加一行 `image 角色 表情 = Transform("images/characters/xxx.png", zoom=0.72)`。
#      zoom=0.72 是全站统一比例，改了会和站位/背景脱节。
#   3. 剧本里 `show 角色 表情 at 站位 with Dissolve(0.7)`。
#   4. 半身像走同一个 tag 加 bust 属性（`show yunxi bust blush at bust_center`），
#      别另起 tag，否则会和全身像叠成双影（README 坑 25）。
#
# 【站位表】zw_*/yx_ 三档：left=0.28 / center=0.5 / right=0.72，yalign 1.0 贴底，
#   自带 2 秒周期的呼吸浮动；zw_teach 是讲台讲题位，yx_hover 是云曦漂浮位。
#   双人同框一律 left+right 配对，中间别塞居中机位（会挡住另一个人）。
#
# 【动画层】本文件下半节「动画层」：card_rise（浮动字卡上浮）、bust_center 的入场
#   推近、score_pop（答题 +分）、memory_live/shutter（回忆照片 Ken Burns + 快门白闪）、
#   glitch_in/wake/dusk_in（三个剧情转场）。动效一律做在 transform/transition 里，
#   不要往 60 多处 `with dissolve` 里塞——要关动画只改那一节，剧本不动。
#
# 【黑板图】board_* 用 ConditionSwitch 按语言选中/英文版（*_en.png 由
#   tools/boards_en.py 用 PIL 在原中文黑板上覆写生成——AI 生图会写坏公式，别重画）。
#   ConditionSwitch 的条件是 Python 表达式，兜底分支必须写 "True" 不是 "true"。
# ============================================================

default player_name = "你"

init python:
    # 当前语言判断：change_language 不更新 config.language，真正的开关在 preferences.language
    def _is_en():
        return renpy.game.preferences.language == "english"

    # ⚠ `_()` 只是「给字符串打标记」（renpy/minstore.py 里它直接 return s），
    #   真正翻译发生在 Text 显示时按整串查词条。所以 `_("前缀：") + 动态值`
    #   拼出来的整串查不到词条 → 英文模式下会露出中文前缀（正确答案：/解析：/提示：
    #   都踩过这个坑）。拼接场景一律写成 `_tl(_("前缀：")) + 动态值`：
    #   `_()` 继续负责被 translate 管线收集，`_tl()` 立刻查表翻成当前语言。
    def _tl(s):
        return renpy.translate_string(s)

    # 【】是全角中文字形，英文界面下会变成"中文出现在不该出现的地方"，所以按语言切换。
    # Character 的 what_prefix/what_suffix 是普通实例属性，可以在运行时改写。
    def _sync_sysvoice(*a, **kw):
        if _is_en():
            sysvoice.what_prefix = ""
            sysvoice.what_suffix = ""
        else:
            sysvoice.what_prefix = "【"
            sysvoice.what_suffix = "】"
        return None

    config.start_callbacks.append(_sync_sysvoice)
    config.after_load_callbacks.append(_sync_sysvoice)

# 【人设拍子（写台词前先对一遍，改台词不用改这里）】
#   云曦＝前半「雌小鬼」→ 后半「重女」。前半的公式是：**捉弄你、看你出糗、把话头
#     递到自己身上再否认**（"被夸一句就解锁""你是我全部的样本量"），句子长、爱报数。
#     从第 5 课起（lesson5/side5/inter5 之后，含 clue3、bridge、date3、recall3、finale）
#     开始**收**：句子变短、不再要赢（"我在这儿，这一条不改""今晚这一分钟，是我的"）。
#     判断标准：越到后期，她越不解释数据。
#   苏知微＝**傲娇**，第 4 课起成型。公式是：先否认动机（"不是路过""这是教具"
#     "顺手多煮了一袋"），再用行动承认（绕三条街、偏十五度的伞、戴一整周的手套）。
#     她的口癖是给自己找名义：教具 / 惯例 / 资产管理 / 招聘 / 利息。
#     ⚠ 傲娇≠冷漠：她的每句否认后面必须跟一个"身体诚实"的动作或旁证，否则就成了凶。
#   两个人都不许直接说"喜欢"——第一部只演到"必须选一个人"那一步。
# ------------------------------------------------------------
define 云曦 = Character("云曦", who_color="#8fdcff", what_color="#e8f6ff")
define 知微 = Character("苏知微", who_color="#ffcf8a", what_color="#fff4e0")
define 我 = Character(lambda: ("You" if _is_en() else "你") if player_name == "你" else player_name, dynamic=True, who_color="#ffd27f")
define sysvoice = Character(None, what_prefix="【", what_suffix="】", what_color="#c8a24a")

# ------------------------------------------------------------
# 背景
# ------------------------------------------------------------
image bg classroom = "images/backgrounds/bg_classroom.png"
image bg study night = "images/backgrounds/bg_study_night.png"
image bg room night = "images/backgrounds/bg_room_night.png"
image bg room day = "images/backgrounds/bg_room_day.png"
image bg title = "images/backgrounds/title_bg.png"
image bg street food = "images/backgrounds/bg_street_food.png"
image bg store = "images/backgrounds/bg_store.png"
image bg canteen = "images/backgrounds/bg_canteen.png"
image bg rooftop dawn = "images/backgrounds/bg_rooftop_dawn.png"
image bg aquarium = "images/backgrounds/bg_aquarium.png"
image bg bookstore = "images/backgrounds/bg_bookstore.png"
# 回忆/梦境专用：月亮+镜面数据海+漂浮屏幕。scenes/recall.rpy 的闪回层用它，
# 别拿去做日常场景（它不是写实背景，是「她残存记忆的那片黑」）。
image bg server core = "images/backgrounds/bg_server_core.png"

# ------------------------------------------------------------
# 云曦（AI 少女）
# ------------------------------------------------------------
image yunxi normal = Transform("images/characters/yunxi_normal.png", zoom=0.72)
image yunxi happy = Transform("images/characters/yunxi_happy.png", zoom=0.72)
image yunxi blush = Transform("images/characters/yunxi_blush.png", zoom=0.72)
image yunxi surprised = Transform("images/characters/yunxi_surprised.png", zoom=0.72)
image yunxi sad = Transform("images/characters/yunxi_sad.png", zoom=0.72)
image yunxi laugh = Transform("images/characters/yunxi_laugh.png", zoom=0.72)
image yunxi angry = Transform("images/characters/yunxi_angry.png", zoom=0.72)
image yunxi smug = Transform("images/characters/yunxi_smug.png", zoom=0.72)
image yunxi sleepy = Transform("images/characters/yunxi_sleepy.png", zoom=0.72)
image yunxi determined = Transform("images/characters/yunxi_determined.png", zoom=0.72)
image yunxi teary = Transform("images/characters/yunxi_teary.png", zoom=0.72)
image yunxi worried = Transform("images/characters/yunxi_worried.png", zoom=0.72)
image yunxi cry = Transform("images/characters/yunxi_cry.png", zoom=0.72)
image yunxi uniform = Transform("images/characters/yunxi_uniform.png", zoom=0.72)
# soft：后期「重女」拍子——不再拿玩笑顶人，直球的那张脸（epilogue_yx / recall3 用）
image yunxi soft = Transform("images/characters/yunxi_soft.png", zoom=0.72)
# hollow：瞳孔失去高光的空白脸。只给「记忆/录音/系统卡住」这类镜头（recall3、bye_yx），别拿进日常
image yunxi hollow = Transform("images/characters/yunxi_hollow.png", zoom=0.72)
# 第十一轮「重女」六连：同一套汉服，彼此可以随便切。
#   love=双手交握直勾勾 / stare=不眨眼凝视 / cling=抓自己袖子贴脸 / jealous=鼓腮抱臂吃醋
#   yandere=刘海压眼低气压笑（喜剧用，别接在正经告白后面）/ peek=背后探头雌小鬼（前期用）
image yunxi love = Transform("images/characters/yunxi_love.png", zoom=0.72)
image yunxi stare = Transform("images/characters/yunxi_stare.png", zoom=0.72)
image yunxi cling = Transform("images/characters/yunxi_cling.png", zoom=0.72)
image yunxi jealous = Transform("images/characters/yunxi_jealous.png", zoom=0.72)
image yunxi yandere = Transform("images/characters/yunxi_yandere.png", zoom=0.72)
image yunxi peek = Transform("images/characters/yunxi_peek.png", zoom=0.72)

# ------------------------------------------------------------
# 苏知微（数学助教学姐）
# ------------------------------------------------------------
image zhiwei normal = Transform("images/characters/zhiwei_normal.png", zoom=0.72)
image zhiwei happy = Transform("images/characters/zhiwei_happy.png", zoom=0.72)
image zhiwei serious = Transform("images/characters/zhiwei_serious.png", zoom=0.72)
image zhiwei laugh = Transform("images/characters/zhiwei_laugh.png", zoom=0.72)
image zhiwei blush = Transform("images/characters/zhiwei_blush.png", zoom=0.72)
image zhiwei surprised = Transform("images/characters/zhiwei_surprised.png", zoom=0.72)
image zhiwei sad = Transform("images/characters/zhiwei_sad.png", zoom=0.72)
image zhiwei smug = Transform("images/characters/zhiwei_smug.png", zoom=0.72)
image zhiwei casual = Transform("images/characters/zhiwei_casual.png", zoom=0.72)
image zhiwei teary = Transform("images/characters/zhiwei_teary.png", zoom=0.72)
image zhiwei panic = Transform("images/characters/zhiwei_panic.png", zoom=0.72)
# angry：傲娇炸毛（抱臂瞪人）。嘴硬场合用，别和 blush 混在同一句里
image zhiwei angry = Transform("images/characters/zhiwei_angry.png", zoom=0.72)
# worried：蹙眉绞手。她难得不说教的那几秒
image zhiwei worried = Transform("images/characters/zhiwei_worried.png", zoom=0.72)
# cry：泪崩但还咬着唇。全游戏只给 bye_zw 那一段
image zhiwei cry = Transform("images/characters/zhiwei_cry.png", zoom=0.72)
# 第十一轮「傲娇」四连：同一套校服，彼此可以随便切。
#   tsundere=别过脸抱臂耳尖红 / hmph=鼓腮推眼镜 / doki=心跳被听见的那一秒 / gentle=破功的遮口笑
image zhiwei tsundere = Transform("images/characters/zhiwei_tsundere.png", zoom=0.72)
image zhiwei hmph = Transform("images/characters/zhiwei_hmph.png", zoom=0.72)
image zhiwei doki = Transform("images/characters/zhiwei_doki.png", zoom=0.72)
image zhiwei gentle = Transform("images/characters/zhiwei_gentle.png", zoom=0.72)

# ------------------------------------------------------------
# 半身像（约会／告白的近距离镜头；与立绘共用 640x960 画布，所以同一个 tag 换属性即可）
# ------------------------------------------------------------
image yunxi bust normal = Transform("images/characters/bust_yunxi_normal.png", zoom=0.72)
image yunxi bust happy = Transform("images/characters/bust_yunxi_happy.png", zoom=0.72)
image yunxi bust blush = Transform("images/characters/bust_yunxi_blush.png", zoom=0.72)
image yunxi bust laugh = Transform("images/characters/bust_yunxi_laugh.png", zoom=0.72)
image yunxi bust sad = Transform("images/characters/bust_yunxi_sad.png", zoom=0.72)
image yunxi bust surprised = Transform("images/characters/bust_yunxi_surprised.png", zoom=0.72)
image yunxi bust smug = Transform("images/characters/bust_yunxi_smug.png", zoom=0.72)
image yunxi bust worried = Transform("images/characters/bust_yunxi_worried.png", zoom=0.72)
image yunxi bust cry = Transform("images/characters/bust_yunxi_cry.png", zoom=0.72)
image yunxi bust soft = Transform("images/characters/bust_yunxi_soft.png", zoom=0.72)
# 第十一轮重女特写：love=交握直勾勾 / yandere=刘海压眼 / jealous=鼓腮握拳 / cling=袖子贴脸
image yunxi bust love = Transform("images/characters/bust_yunxi_love.png", zoom=0.72)
image yunxi bust yandere = Transform("images/characters/bust_yunxi_yandere.png", zoom=0.72)
image yunxi bust jealous = Transform("images/characters/bust_yunxi_jealous.png", zoom=0.72)
image yunxi bust cling = Transform("images/characters/bust_yunxi_cling.png", zoom=0.72)

image zhiwei bust normal = Transform("images/characters/bust_zhiwei_normal.png", zoom=0.72)
image zhiwei bust serious = Transform("images/characters/bust_zhiwei_serious.png", zoom=0.72)
image zhiwei bust blush = Transform("images/characters/bust_zhiwei_blush.png", zoom=0.72)
image zhiwei bust laugh = Transform("images/characters/bust_zhiwei_laugh.png", zoom=0.72)
image zhiwei bust sad = Transform("images/characters/bust_zhiwei_sad.png", zoom=0.72)
image zhiwei bust surprised = Transform("images/characters/bust_zhiwei_surprised.png", zoom=0.72)
image zhiwei bust angry = Transform("images/characters/bust_zhiwei_angry.png", zoom=0.72)
image zhiwei bust happy = Transform("images/characters/bust_zhiwei_happy.png", zoom=0.72)
image zhiwei bust cry = Transform("images/characters/bust_zhiwei_cry.png", zoom=0.72)
# 第十一轮傲娇特写：tsundere=侧脸闭眼推眼镜 / panic=彻底慌了手舞足蹈 / gentle=遮口偷笑
image zhiwei bust tsundere = Transform("images/characters/bust_zhiwei_tsundere.png", zoom=0.72)
image zhiwei bust panic = Transform("images/characters/bust_zhiwei_panic.png", zoom=0.72)
image zhiwei bust gentle = Transform("images/characters/bust_zhiwei_gentle.png", zoom=0.72)

# 半身像时压暗背景，让镜头像 CG 一样聚焦在人物上。用独立 tag，别和 bg 撞。
image dark veil = Solid("#04060c", xsize=1280, ysize=720)

transform veil:
    xalign 0.0
    yalign 0.0
    alpha 0.50

# ------------------------------------------------------------
# 黑板插图
# ------------------------------------------------------------
image board tangent = ConditionSwitch(
    "_preferences.language == 'english'", "images/blackboard/board_tangent_en.png",
    "True", "images/blackboard/board_tangent.png")
image board secant = ConditionSwitch(
    "_preferences.language == 'english'", "images/blackboard/board_secant_en.png",
    "True", "images/blackboard/board_secant.png")
image board sincos = "images/blackboard/board_sincos.png"
image board rules = ConditionSwitch(
    "_preferences.language == 'english'", "images/blackboard/board_rules_en.png",
    "True", "images/blackboard/board_rules.png")

# ------------------------------------------------------------
# 站位（自带轻微待机呼吸浮动）
# ------------------------------------------------------------
transform zw_center:
    xalign 0.5
    yalign 1.0
    yoffset 0
    linear 2.1 yoffset -4
    linear 2.1 yoffset 0
    repeat

transform zw_left:
    xalign 0.28
    yalign 1.0
    yoffset 0
    linear 2.0 yoffset -4
    linear 2.0 yoffset 0
    repeat

transform zw_right:
    xalign 0.72
    yalign 1.0
    yoffset 0
    linear 2.3 yoffset -4
    linear 2.3 yoffset 0
    repeat

transform yx_center:
    xalign 0.5
    yalign 1.0
    yoffset 0
    linear 2.1 yoffset -4
    linear 2.1 yoffset 0
    repeat

transform yx_left:
    xalign 0.28
    yalign 1.0
    yoffset 0
    linear 2.0 yoffset -4
    linear 2.0 yoffset 0
    repeat

transform yx_right:
    xalign 0.72
    yalign 1.0
    yoffset 0
    linear 2.3 yoffset -4
    linear 2.3 yoffset 0
    repeat

# 半身像机位：镜头推近，人物居中，呼吸幅度更小
transform bust_center:
    xalign 0.5
    yalign 1.0
    zoom 1.035
    linear 0.45 zoom 1.0
    block:
        yoffset 0
        linear 2.8 yoffset -3
        linear 2.8 yoffset 0
        repeat

# 双人同框：知微在左讲题，云曦在右飘着
transform zw_teach:
    xalign 0.30
    yalign 1.0
    yoffset 0
    linear 2.0 yoffset -4
    linear 2.0 yoffset 0
    repeat

transform yx_hover:
    xalign 0.78
    yalign 1.0
    # 0.95 不是 1.0：留 5% 的纵深差；0.85 时云曦比知微矮 15%，玩家报过「比例不对」。
    zoom 0.95
    yoffset 0
    linear 2.6 yoffset -8
    linear 2.6 yoffset 0
    repeat

# 黑板图浮动展示
transform board_show:
    xalign 0.5
    yalign 0.42
    alpha 0.97

# ------------------------------------------------------------
# 动画层（第九轮加的）
#
# 【为什么动效全写在这里】剧本里 `with dissolve` 有 60 多处、浮动字卡有 31 处，
#   逐处加动效既容易漏，也会被下一次文案润色冲掉。动效做进「被 at 引用的
#   transform」和「被 with 引用的 transition 变量」，改一处定义全站生效。
# 【字卡】31 处一律 `show expression Text(…) as card at card_rise with dissolve`
#   （tag 固定 card，三行收尾）。上浮来自 card_rise，淡入仍由 with dissolve 管。
# 【半身像】bust_center 入场先做 3.5％ 的镜头推近，再进呼吸循环。
#   ⚠ATL 的 `repeat` 只循环它自己所在的 block：呼吸必须包在 `block:` 里。写在外层
#   会连入场一起循环，半身像每 5.6 秒重新推一次镜头，非常鬼畜。
# 【答题反馈】math_core.rpy 的 do_problem 用 score_pop 飘出 +10/+7/+5。
#   show 语句不阻塞剧情，动效在下一条对白播放期间自己走完，所以没有 pause，
#   不拖慢做题节奏（一局 41 题，加 pause 就是白多几十秒）。
# 【回忆快门】love.rpy 的 show_memory / recall.rpy 的 mem13 用 shutter 白闪 +
#   memory_live 慢推（Ken Burns）。memory_live 的 zoom 只会 ≥1.0，缩小会露黑边。
# 【要关动画】把 card_rise / bust_center / score_pop / memory_live 的首帧直接写成
#   终态，再把 glitch_in / wake / dusk_in / shutter 换回 dissolve —— 剧本一行不用改。
# ------------------------------------------------------------

# 浮动字卡：淡入的同时从下方浮到正中（约 22px，配合 with dissolve 的 0.5s）
transform card_rise:
    xalign 0.5
    yalign 0.53
    linear 0.5 yalign 0.50

# 答题得分：从小弹到原size，再往上飘并消失，全程 0.7 秒
transform score_pop:
    xalign 0.5
    yalign 0.30
    alpha 0.0
    zoom 0.75
    linear 0.14 alpha 1.0 zoom 1.0
    linear 0.34 yalign 0.26
    linear 0.22 alpha 0.0

# 快门白闪（拍照梗）+ 回忆照片的极慢推近
define shutter = Fade(0.10, 0.0, 0.30, color="#ffffff")

transform memory_live:
    alpha 0.0
    zoom 1.0
    linear 0.55 alpha 1.0
    linear 3.0 zoom 1.035

# 三个剧情转场：闪回进机房（像素抖）/ 从回忆里醒过来（泛白）/ 抉择前静场（压黑）
define glitch_in = Pixellate(1.1, 12)
define wake = Fade(0.35, 0.15, 0.9, color="#eaf4ff")
define dusk_in = Fade(0.8, 0.4, 1.0)

# 黑屏闪烁（故障效果）
image glitch black = Solid("#000000")

define fade_black = Fade(0.5, 0.5, 0.5)
define slide_in = MoveTransition(0.4)
