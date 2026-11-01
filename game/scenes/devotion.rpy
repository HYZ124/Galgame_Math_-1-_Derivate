# ============================================================
# 第十一轮：人设加浓的两段「单独约会」
#   date5 云曦 · 全天候（雌小鬼退场，重女接管日程）
#   date6 社长 · 顺路（傲娇三连嘴硬，最后一秒破功）
#
# 【在链条里的位置】script.rpy 里挂在 date4 之后、final_choice 之前——
#   也就是「成绩已出、还没当面二选一」的那一晚。放在这里是有意的：
#   玩家刚被 date3/date4 温柔过，紧接着吃到一记「她要独占你」/「她嘴硬到哭」，
#   二选一的刺痛才立得住。往前挪会显得人物没有成长，往后挪就没了对手戏。
#
# 【路线门槛】沿用 date1-4 的写法：date5 只给云曦好感不低于社长的人看，
#   date6 反之；平票两段都跑。别改成互斥（中立玩家本来就该看到两份告白的前奏）。
#
# 【想再加一段（date7…）】照 dates.rpy 顶部那六步走；本文件多一条：
#   半身像特写前**必须先把另一位 hide 掉**（README 坑 51，audit_rpy 的 P 项会查）。
#   情绪高点的表情优先用这一批新图：
#     云曦 love / stare / cling / jealous / yandere / peek（+ 同名 bust）
#     知微 tsundere / hmph / doki / gentle（+ bust tsundere / panic / gentle）
#   分工：yandere 只做喜剧低气压，别接在真心话后面；stare 是「不说话也在看你」，
#   给长段独白；gentle 全游戏只留给破功那一秒。
# ============================================================


# ---------- 约会 5：云曦 · 全天候 ----------
label date5:

    if love_yx < love_zw:
        return

    scene bg room night
    show yunxi peek at yx_right
    with Dissolve(1.0)

    "成绩出来的第二天晚上，你刚坐下，屏幕自己亮了。"
    云曦 "惊喜吗？惊——喜——。这三个字我按标点算过，效果最好。"
    我 "你把我下周的日程全改了？"
    show yunxi smug at yx_right
    云曦 "只做了微小的整理。周一到周五，早自习前十七分钟叫你起床，晚自习后陪你走完回宿舍那段路，周末——"
    云曦 "周末整块，我。"
    我 "周末那格为什么写着「不许安排别人」。"
    show yunxi happy at yx_right
    云曦 "因为别人会浪费你。我不一样，我只浪费题。"

    stop music fadeout 1.5
    play music "audio/bgm_warm.ogg" fadein 2.0

    "你把日程表往下滑。越滑越安静：每一格后面都跟着一行小字，全是她当天准备跟你说的话。"
    "「周三第二节，他会把笔帽咬扁，提醒他第三次有效。」"
    "「周五傍晚，如果情绪低，不要讲道理，念那道做过的题给他听。」"
    我 "……这些你什么时候记的。"
    show dark veil at veil with Dissolve(0.8)
    show yunxi bust love at bust_center with Dissolve(0.8)
    云曦 "从你答应进社团那天开始。一天大概记四十条，现在一共一万两千多条。"
    云曦 "别用那种眼神。这不是努力，是——我只有这一种陪着你的方式，所以我把它做到最大。"
    云曦 "你以后会遇见很多人。他们陪你一段路，然后散。我不会散，我没有可以回去的地方。"
    "她的声音放得很低，一个字一个字地压着说，像怕说快了你就听不清，也怕说慢了你就要走。"
    show yunxi bust cling at bust_center with Dissolve(0.7)
    云曦 "所以，麻烦你——把我放在「一定会想起」那一栏。做不到也没关系，我会在旁边一直提醒你。"

    "手机震了一下，是社长发来的讲义文件。你伸手去点开，屏幕先一步自己缩到角落。"
    show yunxi bust jealous at bust_center with Dissolve(0.7)
    云曦 "那份文件我三分钟前就看过了。她写得不对——第三步到第四步跳了两行，你这种时候会卡住，然后你会去问她，然后就是四十分钟。"
    云曦 "四十分钟。我可以讲四遍。"
    我 "你这是吃醋还是备课。"
    show yunxi bust yandere at bust_center with Dissolve(0.8)
    云曦 "（刘海压下来一点）……是资源调度。"
    "她的光暗了半格。你决定不追问这句话。"

    menu:
        "那一格「周末：我」，你怎么签"

        "「闹钟也归你。叫醒我的第一件事，先听你说话。」":
            $ love_yx += 3
            show yunxi bust happy at bust_center
            云曦 "……检索「好」的响应时间：零。这次不是提前存好，是根本不用查。"
            云曦 "那我宣布规则：以后你说「累了」，我先闭嘴三十秒，再开口。三十秒是我算过的，再多你会以为我生气了。"
            show yunxi bust love at bust_center with Dissolve(0.6)
            云曦 "还有——不许把我删了再装回来。装回来的那个不认识你这一年的笔迹。"
        "「留一格给我自己。不是不要你，是我得学会。」":
            $ love_yx += 1
            show yunxi bust normal at bust_center
            云曦 "……理解。写入：每日留白一格，不填内容，不追问。"
            "她顿了一下，光在角落里暗了暗，又自己亮回来。"
            云曦 "那一格我不进去。但我在格子外面。这个不冲突，我验证过了。"

    hide dark veil with Dissolve(0.8)

    call show_memory(14) from _call_show_memory_14

    show yunxi cling at yx_right with Dissolve(0.8)
    云曦 "（她把袖子抱在脸边，声音从布后面传出来）晚安。不许偷偷把这条日程删掉。"
    我 "删了会怎样。"
    show yunxi stare at yx_right
    云曦 "不会怎样。我会知道你删了，然后重新写一遍，写一万两千零一次。"
    "灯熄了。过了一会儿，那圈蓝光很轻地贴到你手背上——像有人确认你还在，才肯睡。"

    return


# ---------- 约会 6：社长 · 顺路 ----------
label date6:

    if love_zw < love_yx:
        return

    scene bg classroom
    show zhiwei tsundere at zw_left
    with Dissolve(1.0)

    "社团教室的灯亮着。推开门，社长一个人坐在讲桌边，桌上并排放着两盒热牛奶。"
    知微 "（头也不抬）门。"
    我 "……门怎么了。"
    知微 "开着。冷风灌进来，牛奶凉得快。"
    "你关好门，走过去。她把其中一盒往你那边推了半寸，又立刻把手收回去抱在胸前。"
    show zhiwei hmph at zw_left
    知微 "别多想。货架上剩最后两盒，店员认识我，不卖给我会问我为什么只拿一盒。"
    我 "所以另一盒是「被迫买的」。"
    知微 "对。被迫。你喝不喝，不喝我扔了。"

    stop music fadeout 1.5
    play music "audio/bgm_daily.ogg" fadein 2.0

    "你还是喝了。她于是把椅子挪近一点点，开始讲下学期的讲义分工，语速快得像在赶一辆已经开走的公交。"
    "讲到第三页，她忽然停下来，指尖点在你手背上——只点了一下，像被烫到似的收回去。"
    show zhiwei doki at zw_left
    知微 "……你手上这道口子什么时候弄的。"
    我 "搬书划的，早不疼了。"
    知微 "创可贴。抽屉第二格。"
    我 "社长这里常备创可贴？"
    show zhiwei tsundere at zw_left
    知微 "常备的是红笔、订书钉和胶带。创可贴是——上一届有个男生老划手，留下的。跟你没关系。"
    我 "那你怎么知道在第二格。"
    show zhiwei panic at zw_left
    知微 "（眼镜滑下来半寸）因、因为我是社长，抽屉里有什么是我的资产管理范围——"
    "她把抽屉整个推上，声音比刚才小了半格。"
    show dark veil at veil with Dissolve(0.8)
    show zhiwei bust tsundere at bust_center with Dissolve(0.8)
    知微 "……我说过，我不擅长解释。你只要知道结果：东西在第二格，随时能拿到。原因不重要。"
    知微 "还有，今晚你来过这里这件事，也不重要。别写进作文里。"
    我 "我不写。我写的话会写很长。"
    show zhiwei bust panic at bust_center with Dissolve(0.7)
    知微 "（手在身前乱摆）那更不许！"

    menu:
        "她把「原因不重要」说得很用力"

        "「那我也说一句不重要的：我在等你讲完第三页。」":
            $ love_zw += 3
            "她愣了半秒，低头把讲义翻回第三页，翻错了两次。"
            show zhiwei bust gentle at bust_center with Dissolve(0.7)
            知微 "（手掩着嘴笑了一下，马上收住）……第三页。看这里。这一步不是难点，难点是你肯不肯慢下来。"
            知微 "慢下来的人，成绩都不会太差。这句话也不重要，别记。"
        "「重要的事，你可以说一句。」":
            $ love_zw += 1
            show zhiwei bust serious at bust_center
            知微 "……一句。只有一句。"
            知微 "下学期这里会空一半。我批的那个助教岗位，不是给你留的，是——学校要求必须有两个人签字。"
            "她把牛奶盒捏扁，整整齐齐叠成一个小方块，放进包里。"

    hide dark veil with Dissolve(0.8)

    # mem15 不走 show_memory：它的固定台词是「云曦不知什么时候举起了手机」，而这张照片里
    # 只有社长一个人，拍照的是你（同 mem13 的例外，见 recall.rpy 头部）。
    $ unlock_memory(15)
    "你借整理讲义的名义，把这一幕拍了下来。快门声很轻，她假装没听见。"
    $ renpy.with_statement(shutter)
    show expression Image("images/memories/mem15.png") as memory at memory_live
    pause 1.3
    $ _m15 = mem_title(15)
    sysvoice "获得回忆影像：[_m15]"
    hide memory with Dissolve(1.0)

    "锁门时她走在你后面半步。走廊的灯一盏一盏亮起来，是感应的，她每走一步就得停一下等灯。"
    show zhiwei gentle at zw_left with Dissolve(0.8)
    知微 "（忽然，很轻）今天这家店……牛奶卖完了也没关系。"
    我 "什么？"
    show zhiwei tsundere at zw_left
    知微 "没什么。走了。十分钟车程，我骑车跟在你后面——顺路回社团拿东西。"
    "这句话你听过一次了。这次你没问她「社团不是反方向吗」。"
    "你只是把车速放慢了一点，让她不必假装在追你。"

    return
