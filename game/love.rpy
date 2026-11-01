# ============================================================
# 恋爱度 / 路线判定 / 回忆图鉴（记忆 CG + 主菜单相册）
# 慢热设计：前期好感增益小、台词淡；随课程推进逐渐升温。
#
# 【好感怎么流动】love_yx（云曦）/ love_zw（社长）由 prelude 选项、课堂尾声
#   分支、side/inter/clue/bridge/date 各处 += 累加；route_now() 只比大小，相等即 neutral。
#   课堂台词按 route_now() 分支；结局不再自动判定——final_choice 强制玩家当面选一个，
#   写进 final_route，尾声只认 final_route（没选才回落 route_now()）。想调路线难度就改各处加值。
#
# 【加一张「回忆照片」memN】五步，少一步相册里就是空的或崩：
#   1. 出图 1280×720 → game/images/memories/memN.png；
#   2. 本文件 `image memory N = "images/memories/memN.png"`；
#   3. mem_title() 表里加 N: _("标题")；
#   4. memory_gallery 里 mem 页的 range(1, 16) 上界 +1（16 表示现有 1~15），
#      并按 README「回忆相册版面参数」确认列数×行数还塞得进 720 高；
#   5. 剧情里在情绪最高点 `call show_memory(N)`（会解锁 + 播 CG + 提示入册）。
#      例外：mem13（童年机房）里拍照的人不是云曦，scenes/recall.rpy 自己
#      unlock_memory + `show expression Image(…) as memory` 播，别套用
#      「云曦举起手机」那句台词。
#
# 【加一张「剧情插画」scgN】同理四步：图片 → scg_title() → gallery 的
#   range(1, 10) 上界 → 剧情里 `$ unlock_scene(N)`（它只登记进册，不播 CG；
#   要当场展示就自己 renpy.show + Dissolve）。
#
# 【两条 close-up 规矩】show_memory 的入场是 shutter（快门白闪）+ memory_live
#   （Ken Burns 慢推），两个都在 defines.rpy 动画层；因为要带 `at`，所以用
#   `show expression Image(…) as memory` 语句而不是 renpy.show()（后者没有 at 参数，
#   而且 transition 只能走 with_statement，README 坑 9）。memory_view 的关闭必须是
#   Hide 不是 Return（README 坑 26）。
# ============================================================

default love_yx = 0
default love_zw = 0
# 结局强制二选一的结果（"yunxi"/"zhiwei"），由 scenes/ending.rpy 的 final_choice 写。
# 必须是 default（不是 define）：读档/回滚时它才能回到未选状态。留 None 时
# script.rpy 的尾声分发回落到 route_now()（平票尾 epilogue_neutral 因此不是死代码）。
default final_route = None

init python:

    def route_now():
        if love_yx > love_zw:
            return "yunxi"
        if love_zw > love_yx:
            return "zhiwei"
        return "neutral"

    def unlock_memory(n):
        seen = set(persistent.mem_seen or [])
        if n not in seen:
            seen.add(n)
            persistent.mem_seen = seen

    def mem_seen_set():
        return set(persistent.mem_seen or [])

    def unlock_scene(n):
        seen = set(persistent.scg_seen or [])
        if n not in seen:
            seen.add(n)
            persistent.scg_seen = seen

    def scg_seen_set():
        return set(persistent.scg_seen or [])

    # 剧情插画（scg）图鉴标题。取号现状与解锁点：
    #   1 序章 / 2-5 第1~4课 / 7 第6课 / 9 终章 —— 都在 script.rpy
    #   6 考前夜（scenes/sides.rpy 的 side6）
    #   8 三条尾声共用（scenes/ending.rpy，epilogue_yx/zw/neutral 各调一次）
    def scg_title(n):
        # `_()` 只打标记不翻译（见 defines.rpy 的 _tl 注释），返回值会直接进
        # 相册/横幅文本，必须 _tl() 立刻查表，否则 EN 模式露出中文标题。
        return _tl({
            1: _("清晨书桌，邀请的开始"),
            2: _("割线，第一次靠近切线"),
            3: _("深夜，定义的三个动作"),
            4: _("口诀背得像一首歌"),
            5: _("黑板上那颗心形线"),
            6: _("错题本前夜，一支粉笔"),
            7: _("考试的寂静，交卷时刻"),
            8: _("明天的曲线"),
            9: _("屏幕上浮现的陌生签名"),
        }[n])

    # 回忆照片（mem）图鉴标题。取号现状与解锁点：
    #   1-7 = 七次课前小剧情（prelude.rpy，每 preN 结尾 call show_memory(N)）
    #   8-11 = 四段单独约会（scenes/dates.rpy 的 date1~date4）
    #   12 = 出分前第二晚的社团教室（scenes/bridge.rpy 的 bridge，重讲错题那一段）
    #   13 = 童年机房（scenes/recall.rpy 的 recall1，拍照的不是云曦）
    #   14 = 全天候那晚的书桌（scenes/devotion.rpy 的 date5，她看你而不是看题）
    #   15 = 夜里社团教室的两盒牛奶（scenes/devotion.rpy 的 date6，拍照的是你）
    def mem_title(n):
        # 同 scg_title：必须 _tl() 立刻查表，否则 EN 模式的横幅和相册露出中文标题
        # （2026-10-27 探针在 EN 模式抓到 "Memory unlocked: 旧书店里的那本红笔习题册"）。
        return _tl({
            1: _("校门口，第一杯热豆浆"),
            2: _("便利店的牛奶与热可可"),
            3: _("食堂窗边，被偷走的最后一口饭"),
            4: _("天台的包子与晨读口诀"),
            5: _("夜摊的关东煮与鹌鹑蛋"),
            6: _("一人一半的便当"),
            7: _("考试早晨的豆浆之碰杯"),
            8: _("水族馆的蓝色黄昏"),
            9: _("旧书店里的那本红笔习题册"),
            10: _("深夜书桌，只照你一角的蓝光"),
            11: _("午夜便利店的第二支红笔"),
            12: _("两杯热豆浆，一块没擦的黑板"),
            13: _("旧机房地上，有人在写作业"),
            14: _("整张书桌被她排满，只留你坐的那一格"),
            15: _("夜里空教室，两盒牛奶和一盒创可贴"),
        }[n])

# ------------------------------------------------------------
# 记忆 CG
# ------------------------------------------------------------
image memory 1 = "images/memories/mem1.png"
image memory 2 = "images/memories/mem2.png"
image memory 3 = "images/memories/mem3.png"
image memory 4 = "images/memories/mem4.png"
image memory 5 = "images/memories/mem5.png"
image memory 6 = "images/memories/mem6.png"
image memory 7 = "images/memories/mem7.png"
image memory 8 = "images/memories/mem8.png"
image memory 9 = "images/memories/mem9.png"
image memory 10 = "images/memories/mem10.png"
image memory 11 = "images/memories/mem11.png"
image memory 12 = "images/memories/mem12.png"
image memory 13 = "images/memories/mem13.png"
image memory 14 = "images/memories/mem14.png"
image memory 15 = "images/memories/mem15.png"

# ------------------------------------------------------------
# 解锁演出：在约会场景的最高点插入，展示 CG 并提示入册
# ------------------------------------------------------------
label show_memory(n):

    $ unlock_memory(n)
    "云曦不知什么时候举起了手机——“咔嚓”，这一刻被她存进了数据库。"
    # 快门白闪 → 照片带 Ken Burns 慢推入场（transform/transition 都在 defines.rpy
    # 的动画层）。这里用 show 语句而不是 renpy.show()，因为 renpy.show 没有 at 参数。
    # ⚠`Image()` 的参数是**文件路径**，不是 image 名：写成 Image("memory 13") 不报错，
    #   只会在屏幕顶上画一行 "Couldn't find file 'memory 13'."（2026-10-22 探针抓到）。
    #   路径规则与主菜单相册 memory_view 保持一致。
    $ renpy.with_statement(shutter)
    show expression Image("images/memories/mem%d.png" % n) as memory at memory_live
    pause 1.3
    $ mt = mem_title(n)
    sysvoice "获得回忆图：[mt]"
    "（想再看的话，它会安静地等在主菜单的「回忆相册」里。）"
    hide memory with Dissolve(0.8)

    return


# ------------------------------------------------------------
# 主菜单：回忆相册（剧情插画 / 回忆照片 两分页）
# ------------------------------------------------------------
transform memory_pop:
    alpha 0.0
    zoom 0.94
    easeout 0.35 alpha 1.0 zoom 1.0

screen memory_gallery():

    tag menu
    default gal_tab = "scg"
    $ seen = mem_seen_set()
    $ sseen = scg_seen_set()

    add Solid("#0b1712")

    # 用 yalign 而不是 yfill：Ren'Py 对超屏内容既不报错也不滚动，yfill 会把
    # 「返回」按钮顶出 720 之外。格子尺寸按 720 反推，见 README「回忆相册版面参数」。
    vbox:
        xfill True
        spacing 8
        xalign 0.5
        yalign 0.5

        null height 6
        text _("回忆相册") size 36 color "#ffd27f" xalign 0.5
        text _("和她们一起走过的日子。") size 20 color "#8aa596" xalign 0.5

        hbox:
            spacing 18 xalign 0.5
            vbox:
                spacing 2
                textbutton _("剧情插画") action SetScreenVariable("gal_tab", "scg") xalign 0.5
                if gal_tab == "scg":
                    add Solid("#ffd27f", xsize=140, ysize=3) xalign 0.5
                else:
                    null height 3
            vbox:
                spacing 2
                textbutton _("回忆照片") action SetScreenVariable("gal_tab", "mem") xalign 0.5
                if gal_tab == "mem":
                    add Solid("#ffd27f", xsize=140, ysize=3) xalign 0.5
                else:
                    null height 3

        null height 2

        if gal_tab == "scg":
            $ unlocked = [n for n in range(1, 10) if n in sseen]
            if not unlocked:
                text _("还没有解锁的插画——继续上课、间幕和约会，它们会一张张亮起来。") size 22 color "#8aa596" xalign 0.5
            else:
                $ _cols = 3
                $ _rows = (len(unlocked) + _cols - 1) // _cols
                grid _cols _rows spacing 14 xalign 0.5:
                    for n in unlocked + [0] * (_cols * _rows - len(unlocked)):
                        if n:
                            button:
                                xsize 236
                                ysize 133
                                padding (0, 0)
                                add Transform(Image("images/story/scg%d.png" % n), xsize=236, ysize=133)
                                action Show("memory_view", n=n, kind="scg")
                        else:
                            null:
                                xsize 236
                                ysize 133
        else:
            $ munlocked = [n for n in range(1, 16) if n in seen]
            if not munlocked:
                text _("还没有拍到照片——和她们多走走，云曦的快门会自己按下去。") size 22 color "#8aa596" xalign 0.5
            else:
                # 5 列而不是 4 列：13 张时 4 列要排 4 行（482 高）会把「返回」顶到屏外，
                # 5 列 3 行（358 高）永远塞得进 720。格子尺寸见 README「回忆相册版面参数」。
                $ _cols = 5
                $ _rows = (len(munlocked) + _cols - 1) // _cols
                grid _cols _rows spacing 14 xalign 0.5:
                    for n in munlocked + [0] * (_cols * _rows - len(munlocked)):
                        if n:
                            button:
                                xsize 196
                                ysize 110
                                padding (0, 0)
                                add Transform(Image("images/memories/mem%d.png" % n), xsize=196, ysize=110)
                                action Show("memory_view", n=n, kind="mem")
                        else:
                            null:
                                xsize 196
                                ysize 110

        null height 2
        textbutton _("返回") action Return() xalign 0.5

    # 贴在屏幕右下角，不进 vbox：相册版面是按 720 高反推的，往 vbox 里再加一行会把
    # 「返回」顶出屏幕（见 README「回忆相册版面参数」）。
    text _("桌面壁纸：游戏目录下的 wallpapers 文件夹，喜欢就拷走。") xalign 0.99 yalign 0.99 size 16 color "#5f7a6c"


screen memory_view(n, kind="mem"):

    modal True
    zorder 50

    $ gpath = ("images/story/scg%d.png" if kind == "scg" else "images/memories/mem%d.png") % n
    $ gtitle = (scg_title if kind == "scg" else mem_title)(n)

    add Solid("#000000")
    add Image(gpath) at memory_pop

    add Text(gtitle, size=30, color="#ffd27f", outlines=[(2, "#000000aa", 0, 0)]):
        xalign 0.5
        yalign 0.93

    text _("点击任意处关闭") xalign 0.97 yalign 0.05 size 18 color "#c8d6cc"

    # 关闭必须用 Hide，不能用 Return：本屏是相册里 Show() 叠上来的一层，
    # 而菜单上下文里 Return() 的语义是「退出整个菜单」，点一下会被踢回主菜单。
    button:
        xfill True
        yfill True
        action Hide("memory_view")

    key "game_menu" action Hide("memory_view")
