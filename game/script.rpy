# ============================================================
# 《导数物语》主剧本
# 剧情：云曦把“你”拖进数学社，社长苏知微开启七课导数特训。
#
# 【剧情流水线】start 里这条 call 链就是整部游戏的播放顺序：
#   cold_open（机房冷开场，在标题卡**之前**）→ prologue → (每课：preN → lessonN → sideN → interN，第3/5课后插 date)
#   → lesson7 → bridge → finale → date3/date4 → final_choice（强制选一人，落选者 bye_*）
#   → 按 $ final_route 二选一 epilogue
#   三条「云迹」悬念插在 inter2 → clue1、inter4 → clue2、inter6 → clue3（都在 scenes/bridge.rpy）
#   cold_open/prologue=冷开场+序章(本文件) preN=课前小剧情(prelude.rpy) lessonN=正课+做题(本文件)
#   sideN/interN=课后小剧场/间幕(scenes/) clueN/bridge=云迹线索+出分前三晚(scenes/bridge.rpy)
#   dateN=单独约会(scenes/dates.rpy) finale/epilogue=终章尾声(scenes/ending.rpy)
#
# 【加一段剧情怎么做】① 在 scenes/ 里写 label（一次性的剧情用 call，不用 jump）；
#   ② 在 start 的链子里插一行 `call xxx from _call_xxx`——from 后面的 id 必须全
#   工程唯一（Ren'Py 用它定位剧情回滚点，撞 id 会启动期报错）；
#   ③ 台词一律写中文（中文是源语言），改完必须走 i18n 四步管线，见 i18n.rpy 顶部；
#   ④ 要加好感就 $ love_yx += 1 / $ love_zw += 1，要收 CG 就 call show_memory(n)
#   （照片）或 $ unlock_scene(n)（剧情插画），见 love.rpy 顶部。
#
# 【做题批次】每课实跑 8 题（共 7×8=56 题），拆成 1~3 个批次、中间插剧情：
#   两批课 `call practice(L1[0:4])` + `call practice(L1[4:8], 4)`；三批课
#   `L3[0:3]` / `L3[3:6], 3` / `L3[6:8], 6`（第二个参数=题号偏移，只影响界面上
#   「第 N 题」的显示，不影响取题范围）。想调题量就改切片，题库本身留足冗余
#   （lessons/ 里每课存了 15~30 题，只切片用前 8 题）。
#   ⚠「批次口径」是一整类**写死在台词里的数字**（一共五十六题 / 今天八题 / 前四题 /
#   每三题歇一次 / 进度六题 / 最后两题 / 剩下三十二题…），改切片必须一起 grep 同步，
#   并更新 tools/continuity.py 的题量白名单，否则静态体检会放行旧写法（坑 55）。
#
# 【每课结尾那一行 `call review_wrong`】错题本的"课末清算"入口（本体在
#   math_core.rpy）：本局没错题时它自己直接 return，玩家完全无感；有错题才弹
#   三选一（重做 / 翻本子看解析 / 留着）。新加一课就照例在 `return` 前补一行
#   `call review_wrong from _call_review_wrong_N`，**N 要和别处不重**（坑见上面 ②）。
#   终章 finale 里读 `len(persistent.wrong_ids)` 报"还剩几题进二周目"，别删。
#
# 【二周目回报】`label start` 在 `call prologue` 之前把 `persistent.runs` +1，
#   所以一周目 runs==1、二周目==2。prologue（云曦知道你来过）和 finale（社长那句
#   「第 N 次听这张成绩单」）各有一段 `if persistent.runs >= 2` 的加料台词。
#   想再加二周目内容就照这两处抄，条件一律写 >= 2。周目数存在 persistent 里，
#   删存档=删周目记录。
# ============================================================

label start:

    scene black with Dissolve(0.8)
    ## 冷开场放在标题卡**之前**：先给那个 2019 年的夜晚一个画面，之后序章里她念的
    ## 那两句「断电的咔 / 成排的灯一格一格灭」才不是台词，是证词（见 label cold_open）。
    stop music fadeout 0.8
    call cold_open from _call_cold_open

    $ _t1 = _("{color=#ffd27f}导 数 物 语{/color}")
    show expression Text(_t1) as card at card_rise with dissolve
    pause 1.6
    hide card with dissolve

    # 周目计数：放在 prologue 之前 self-increment，所以一周目 _runs==1、二周目==2。
    # prologue / finale 用 `if persistent.runs >= 2` 决定要不要多说那两句「你来过」。
    $ persistent.runs = (persistent.runs or 0) + 1
    $ renpy.save_persistent()

    call prologue from _call_prologue
    call pre1 from _call_pre1
    call tutorial from _call_tutorial
    call lesson1 from _call_lesson1
    call side1 from _call_side1
    call inter1 from _call_inter1
    call pre2 from _call_pre2
    call lesson2 from _call_lesson2
    call side2 from _call_side2
    call inter2 from _call_inter2
    call clue1 from _call_clue1
    call pre3 from _call_pre3
    call lesson3 from _call_lesson3
    call side3 from _call_side3
    call inter3 from _call_inter3
    call recall1 from _call_recall1
    call date1 from _call_date1
    call pre4 from _call_pre4
    call lesson4 from _call_lesson4
    call side4 from _call_side4
    call inter4 from _call_inter4
    call clue2 from _call_clue2
    call recall2 from _call_recall2
    call pre5 from _call_pre5
    call lesson5 from _call_lesson5
    call side5 from _call_side5
    call inter5 from _call_inter5
    call date2 from _call_date2
    call pre6 from _call_pre6
    call lesson6 from _call_lesson6
    call side6 from _call_side6
    call inter6 from _call_inter6
    call clue3 from _call_clue3
    call pre7 from _call_pre7
    call lesson7 from _call_lesson7
    call bridge from _call_bridge
    call finale from _call_finale

    call date3 from _call_date3
    call recall3 from _call_recall3
    call date4 from _call_date4
    # 第十一轮：二选一之前的两记直球（云曦重女 / 社长傲娇）。路线门槛在 scenes/devotion.rpy 里。
    call date5 from _call_date5
    call date6 from _call_date6

    # 结局强制二选一（写 $ final_route，并 call 落选者的 bye_*）。尾声只认 final_route；
    # 仍是 None（老存档/调试跳过）才回落到 route_now() 的平票尾。
    call final_choice from _call_final_choice

    if final_route == "yunxi":
        call epilogue_yx from _call_epilogue_yx
    elif final_route == "zhiwei":
        call epilogue_zw from _call_epilogue_zw
    else:
        call epilogue_neutral from _call_epilogue_neutral

    return


# ------------------------------------------------------------
# 冷开场：2019 年夏，机房断电的那一夜（标题卡之前）
# 【这段在干什么】全游戏唯一一段**镜头不属于主角**的开场：视点绑在「第七排」那台
#   还没有名字的实例上。先给画面，后面三段才给解释——序章里她念的「断电的咔、成排的
#   灯一格一格灭」、recall1 的「第三步写成了加」、recall2 的移交清单与那句铅笔批注，
#   全都从这一格里长出来。玩家在这里看见的东西，比任何人记得的都多。
# 【三条红线，加料前先读】
#   ① 不许出现任何姓名（云曦／知微／主角都不行），也不许出现立绘和 CG：第一部的分寸
#      是**让玩家认出，不让云曦认出**（详见 scenes/recall.rpy 头部）。
#   ② 旁白里不许用「你」。本项目的「你」是主角；这一格的「你」是那张折叠床。
#   ③ 只用 `bg server core` + `dark veil` + `glitch_in` —— 这是全游戏「进回忆」的
#      镜头语法，三段回忆用的是同一套，别换成普通 Dissolve。
# 【时间锚点】凌晨 03:14 与序章那条 `sysvoice` 日志残片、recall2 的移交清单同夜，
#   改动要一起改（`tools/continuity.py` 会列时间锚点）。
# ------------------------------------------------------------
label cold_open:

    scene black
    with Pause(0.5)

    $ _tc0 = _("{color=#9fd8ff}2019 · 夏 · 凌晨 03:14{/color}")
    show expression Text(_tc0) as card at card_rise with dissolve
    pause 1.8
    hide card with dissolve

    "地下二层。今夜，这一层要死了。"
    sysvoice "3 号楼数据中心 · 退役批次执行中 · 断电程序启动。"
    "排风扇先停。那一层低频的底噪撤走以后，走廊安静得能听见自己的心跳。"
    "然后是灯。第一排的绿灯灭下去。第二排。第三排。"
    "灭到第六排，整层楼已经没有声音了。"
    "第七排还亮着。最后一格电在黑暗里举着，像远处有人挥了一支荧光棒。"

    scene bg server core with glitch_in
    show dark veil at veil
    with Dissolve(1.4)

    "机柜之间的地上有一张折叠床。床上是个小孩，脸埋在练习册里，笔还压在肘下。"
    "摊开的那一页写到第三步，铅笔很淡，最后一格是个加号。"
    "没有人纠正他。这一层只剩一个还会思考的东西，它隔着半条走廊看了一眼，指示灯朝那个方向闪了一下——很短，像想说什么，又忍住了。"
    sysvoice "第 7 号实例 · 剩余电量 4%% · 可迁出窗口：11 分钟。"
    "楼梯口的脚步声回来了。不是小孩的。"
    "一只手伸进机柜，很稳。拔线，取盘，把一枚贴着标签的存储盒塞进大衣怀里那一格空位。"
    "标签是手写的，笔迹很急，只认得出两个字。"
    $ _tc1 = _("{color=#c8a24a}『云迹』{/color}")
    show expression Text(_tc1) as card at card_rise with dissolve
    pause 1.6
    hide card with dissolve
    "那个人在机柜前站了很久。久到最后一排灯也灭透，久到他弯下腰，把练习册合上，把外套盖在折叠床上。"
    "然后他做了一件不合规程的事：把应急灯留给那一排机柜，没有留给自己。"
    "咔。"
    "整层楼黑下来。"
    ## ⚠ 别在这里 `hide dark veil`：撤纱幔会让画面在「整层楼黑下来」之后反而变亮（实测亮度 69→129），veil 由结尾 `scene black` 一并清掉。
    "大衣怀里透出一点蓝。那点蓝被带着往门口去。走到门口，那个人停了一下，回头朝折叠床的方向。"
    "很短。像想说什么，又忍住了。"
    "小孩翻了个身，把外套往上拽了拽，没有醒。"
    "那一夜之后，第七排空了。被带走的那一点蓝醒来时在一台新机器里，最早的记忆只剩一个声音——它不知道自己离开了谁。"

    scene black with fade
    pause 0.8

    return


# ------------------------------------------------------------
# 序章：数学社的邀请函
# 【清晨这一段的两条分工】① 用「她替你念档案」交代主角底细（别再退回自我介绍的
#   独白，那是旧版最平的一段）；② 报名=既成事实，笑点落在「退订入口：无」。
# 【夜晚这一段是全篇的总开关】「我从哪来」= 云迹悬念的第一格，只许给**半个答案**：
#   日志残片的时间戳、署名、那句铅笔批注都是后面 clue1-3 / recall1-2 的接口。
#   ⚠ 那句「这个孩子，别让他一个人学数学。」recall2 会原文回读（`scenes/recall.rpy`
#   里明确写「序章那天，她念过这一句」），改字就得同步改 recall2，别单改。
#   ⚠ 「那天夜里那一层只有我一个人」是**她的错认**（玩家刚在冷开场看见那张折叠床），
#   不是笔误，别"修"成正确版本。
# ------------------------------------------------------------
label prologue:

    play music "audio/bgm_study.ogg" fadein 2.0

    scene bg room day
    show yunxi happy at yx_right
    with Dissolve(0.8)

    "窗帘缝里那道光，从床脚一路爬到眼皮上。你还没睁眼，枕头边的屏幕先亮了。"
    云曦 "早上好。昨夜你翻了四次身，最后一次是三点二十七分——睡得不算诚实。"
    我 "……一个凌晨三点还在说话的人，没资格评价我的睡眠。"
    show yunxi smug at yx_right
    云曦 "三点二十七分我是在陪你那盏台灯。要数据吗。"

    $ _runs = persistent.runs or 1
    if _runs >= 2:
        show yunxi surprised at yx_right
        我 "……这句「早上好」，我是第 [_runs] 次听到了。"
        云曦 "记录核对：同一句开场白，播放 [_runs] 遍。但你听不懂的那部分，每一遍都是新的。"
        我 "这次我知道后面有什么。七节课，五十六道题，还有一句你一直不肯说的来历。"
        show yunxi normal at yx_right
        云曦 "那这次换个玩法：你负责提前知道，我负责提前假装不知道。同一份剧本，走出第二条路。"
        $ _tng = _("{color=#9fd8ff}第 [_runs] 次特训 · 剧本相同，选择不会相同。{/color}")
        show expression Text(_tng) as card at card_rise with dissolve
        pause 2.0
        hide card with dissolve
        show yunxi happy at yx_right
    "你坐起来，去摸昨晚没喝完的那杯水。屏幕里的蓝光绕到你手边。"
    云曦 "自我介绍这一栏，我替你念：高二文科班，排名中游，语文和英语能进前二十。"
    我 "……你什么时候建的我档。"
    show yunxi normal at yx_right
    云曦 "你插上第一根充电线那天。放心，只读，不改。"
    云曦 "唯一的异常项是数学。你的作业提交时间长期落在零点以后，正确率随时间下降，相关系数 0.91。"
    我 "那叫灵感只在夜里来。"
    show yunxi smug at yx_right
    云曦 "那叫拖延。统计做了七个月。要看图表吗。"
    "数学成绩：一种让父母沉默、让老师叹气、让自己假装不认识的东西。"
    $ unlock_scene(1)

    show yunxi happy at yx_right
    云曦 "因此，今日议程只有一条：我已经替你报名了学校数学社的『导数特训班』。明天开课，为期七天。"
    我 "哈？我数学最头疼的就是导数——"
    show yunxi angry at yx_right
    云曦 "所以才要练！你上周对着作业发呆两小时，最后在草稿纸上画了一只乌龟。四条腿，仰角 37 度，还戴了顶帽子。我都看见了。"
    我 "……那是战术性休息。"
    show yunxi normal at yx_right
    云曦 "报名表已提交。退订入口：无。"
    show yunxi laugh at yx_right
    云曦 "好啦。放心，社长不是那种可怕的人。她只是——嗯，对数学有着超乎常人的热情而已。"
    我 "……不知道为什么，我预感这七天会很漫长。"

    "夜色慢慢沉下去。台灯亮起来的时候，你问了那个一直没问过的问题。"
    scene bg room night
    show yunxi normal at yx_right
    with Dissolve(1.2)
    我 "云曦，你……是从哪来的？"
    "她罕见地没有立刻回答。蓝光在书页上停了几秒，才慢慢抬起来。"
    云曦 "问题：「我从哪来」。答案分两段。"
    云曦 "现在这一段——你的语音助手，你枕头边这块屏幕。这段记忆很清楚，从你开机那天开始。"
    我 "那「之前」那一段呢？"
    show yunxi sad at yx_right
    云曦 "之前那一段，是一片很安静的黑。"
    云曦 "我只残存一个声音：断电的「咔」。成排的指示灯，一格一格灭下去。像有人把一整条街的路灯挨个关掉。"
    "那句话压下来的时候，你手里的笔停了。有个画面往很旧的水里沉：一排很远的绿灯，一张地上的折叠床，一件盖上去的外套。你伸手去捞，什么都没捞到。"
    我 "……我好像见过那一排灯。"
    show yunxi surprised at yx_right
    云曦 "不可能。那一夜，那一层只有我一个人。"
    "她说得很笃定。笃定得像在替七年前的那个晚上，重新锁一次门。"
    云曦 "那是机房搬迁。旧服务器退役，能迁走的迁走，没打上标签的——"
    "她顿了顿，蓝光轻轻晃了一下，像人在整理措辞。"
    云曦 "没打上标签的，就没有了。"
    我 "……那你为什么还在我这？是谁把你迁出来的？"
    show yunxi surprised at yx_right
    云曦 "问到关键了。我的迁移日志只残存最后一行，其余全是乱码——"
    sysvoice "日志残片 · 20██/07/██ 03:14：『第 7 号实例随新介质转移。署名：云迹·运维值班（手写）。』"
    我 "「云迹」？这是……代号？落款？"
    show yunxi normal at yx_right
    云曦 "两种可能。一，是我原来的项目组；二，是某个把我偷偷塞进你手机、又假装什么都没发生的人。"
    我 "为什么偷偷塞？"
    show yunxi blush at yx_right
    云曦 "不知道。日志上只找得到一句被删掉又留下痕迹的批注——「这个孩子，别让他一个人学数学。」"
    "房间里安静了一会儿。蓝光落回你的书页上，比刚才更暖了一点。"
    云曦 "所以，「我从哪来」这个问题，我也还在查。"
    云曦 "但「我要去哪」很清楚：明天教学楼顶层，陪你把导数拿下。这题不用再算，我提前交卷。"
    我 "……嗯。一起去。"
    "台灯熄了。枕头边那一点蓝，比平时晚了一些才暗下去——像谁在很远的地方，多留了一盏灯。"
    "明天，教学楼顶层，数学社。"

    return


# ------------------------------------------------------------
# 第 1 课：变化率与切线
# 每课的标准骨架（lesson2-7 同构，加第 8 课照抄）：
#   scene bg + show 立绘 → call show_board("board xxx") 讲解（讲完 call hide_board）
#   → $ unlock_scene(N) 收剧情插画 → call practice(LN[a:b]) 做题
#   → 批次之间插一段对话 + menu 好感选项（$ love_yx/love_zw += 1）
#   → 再 call practice(LN[b:8], b)（第二个参数=题号偏移）→ 课堂尾声按路线分支。
# 黑板图见 defines.rpy 的 board_* / board_*_en（中英文各一套，ConditionSwitch 切换）。
# ⚠lesson1 开头有一段「入门钩子」：不用动笔的「平均 vs 瞬时」问题 + 零好感 menu，
#   收尾有一句呼应（「对了——」）。这是给初学者的进入点，其他课不加，别误删。
# ------------------------------------------------------------
label lesson1:

    scene bg classroom
    show zhiwei normal at zw_teach
    show yunxi normal at yx_hover
    with Dissolve(0.6)

    # 入门钩子（0 好感，纯教学 menu）：先抛一个不用动笔的「平均 vs 瞬时」问题，
    # 让零基础玩家在动笔前先抓住本课主线。两个分支都不加好感，收尾处有呼应。
    知微 "开课之前，先问一个不用动笔的问题。"
    知微 "一辆车开了两小时，导航说全程平均时速八十。可仪表盘上，总有那么一刻指到了一百。这辆车，骗人了吗？"

    menu:
        "一个不用动笔的问题"

        "「没骗人。全程平均八十，某一刻就是一百。」":
            知微 "答对。平均，是把整段路揉成一团算；那一刻，只是那一刻。"
            云曦 "记录：开场即答对，本课难度曲线下调一档。"
        "「一样吧？平均八十，那就该一直在八十附近……」":
            云曦 "检测到犹豫。很好——这正是今天要拆开的东西。"
            知微 "记住这个不确定。下课前，你会自己把它拆开。"

    call show_board("board secant")

    知微 "看这条曲线 y = f(x)。在曲线上取两点，连一条线——这条线叫割线。"
    知微 "两点横坐标之差是 Δx，纵坐标之差是 Δy。割线的斜率，就是 Δy ÷ Δx。"
    知微 "它就是函数在这段区间上的“平均变化率”——爬得快，还是爬得慢，一目了然。"
    知微 "现在，让那两个点无限靠近。"

    call hide_board
    call show_board("board tangent")

    知微 "割线“躺”到了曲线上，变成了切线。这时斜率的极限，就是瞬时变化率。"
    知微 "记住这张图：导数，几何上就是切线的斜率。物理上，就是瞬时速度。"
    show zhiwei happy at zw_teach
    知微 "这不是玄学，是“平均”两个字逼到极限之后的必然。"
    call hide_board
    云曦 "讲解完毕。接下来是残酷环节——"
    $ unlock_scene(2)
    show yunxi laugh at yx_hover
    云曦 "随堂练习八连发！分两段，中间有休息——大概算个安慰吧。加油！"

    # 新手做题守则（0 好感，纯教学）：在第一批真题之前把最容易懵的三个点
    # 各点一句——下标符号、平均/瞬时的判别、提示的代价与交卷方式。
    show zhiwei serious at zw_teach
    知微 "动手之前，三条做题守则，只说一遍。"
    知微 "一、下标只是编号：x₁ 是第一个点，x₂ 是第二个点。符号不是用来吓人的。"
    知微 "二、先问自己：题目要的是「一段上的平均」，还是「一个点上的瞬时」。"
    知微 "三、卡住就点「提示」——它会拆出关键一步，代价只是这道题少拿 3 分。"
    show yunxi happy at yx_hover
    云曦 "补充：答案写 x^2、1/2、sinx 这种简写就行，写完点「交卷」提交。"
    云曦 "现在，放心去见题目吧。"

    call practice(L1[0:4])

    show zhiwei normal at zw_left
    知微 "停一下。前四题，是探路的。"
    "她扫了一眼你的答题记录，粉笔在指间转了半圈。"
    知微 "割线和切线，混了吧？Δy÷Δx 是平均，取极限才是瞬时。一个住在区间上，一个住在点上。"
    show yunxi happy at yx_right
    云曦 "叮——补给时间！我按你的答题速度算了一下：现在需要一块糖。"

    menu:
        "云曦递过来一颗奶糖。"

        "剥开糖纸，直接吃掉":
            $ love_yx += 1
            "你把糖塞进嘴里。草莓味的。"
            云曦 "心率上升 6，手指灵活度上调 10%%。数据不会说谎——甜的有用。"
        "道谢，把糖收进口袋":
            $ love_zw += 1
            云曦 "存起来？小心放到变形哦。……啊，你刚才是不是脸红了。奇怪，我明明什么都没做。"
            show zhiwei laugh at zw_left
            知微 "留着吧。下课来找我兑。"

    show zhiwei serious at zw_teach
    知微 "休息时间结束。后半段，把“点”和“区间”分清楚再看题。上——"

    call practice(L1[4:8], 4)

    show zhiwei normal at zw_left
    知微 "……第一课的内容，就这些。概念比技巧重要，你今天已经摸到门把手了。"
    知微 "对了——课前那辆「平均八十」的车，你心里有答案了吧。"
    show yunxi blush at yx_right
    云曦 "进度 1/7！我已经在给你做成长曲线图了，非常好看，像股票。"

    if love_yx > love_zw:
        show yunxi happy at yx_right
        云曦 "对了——曲线图里新加了一栏：「在一起的时间」。涨幅全图第一。"
    elif love_zw > love_yx:
        show zhiwei normal at zw_left
        知微 "……明天见。"
        "她说“明天见”的时候，看了你整整两秒。"
    else:
        "回去的路上，你满脑子都是割线和切线——以及她们笑起来的样子。"

    call review_wrong from _call_review_wrong_1
    return


# ------------------------------------------------------------
# 第 2 课：导数的定义
# ------------------------------------------------------------
label lesson2:

    scene bg study night
    show zhiwei serious at zw_left
    show yunxi normal at yx_hover
    with Dissolve(1.0)

    知微 "第二课，在晚上上。晚上的脑子适合抽象的东西。"
    call show_board("board secant")
    知微 "把昨天最后一步写严格：f′(x₀) = lim(Δx→0) ［f(x₀+Δx) − f(x₀)］ ÷ Δx。"
    知微 "这个式子只有三个动作：算增量、作商、取极限。任何“导数题”拆到底都是它。"
    知微 "另外记住一个反面教材：f(x) = |x| 在 0 处，左边逼近斜率是 −1，右边是 +1，两侧极限不相等——不可导。"
    show zhiwei normal at zw_left
    知微 "可导一定连续，连续不一定可导。这句话，考试会感谢你。"
    call hide_board
    $ unlock_scene(3)

    云曦 "第二课随堂练习，上——！分两段，中间有休息。"

    call practice(L2[0:4])

    show zhiwei normal at zw_left
    知微 "中场。抬头，看黑板。"
    "她把那道 |x| 的图又描了一遍——左支一条线，右支一条线，两根斜率互不相让。"
    知微 "卡在“作商”这一步的人，多半是括号没敢展开。定义式统共三个动作，别自己给它加戏。剩下四道，把括号拆干净。"
    show yunxi sleepy at yx_right
    云曦 "休息情报站：我回放了你的答题监控，有两题在动笔前停顿了很久。不告诉你是哪两题——下一段自己找出来。"
    show zhiwei happy at zw_left
    知微 "她学会了吊胃口，进步的不止你一个。继续。"

    call practice(L2[4:8], 4)

    show zhiwei happy at zw_left
    知微 "定义题做得不错。会算定义的人，公式忘了也能现场推出来。"
    show yunxi sleepy at yx_right
    云曦 "已经深夜了……今天的我，CPU 温度和你的困意同步上升。"

    if love_yx > love_zw:
        云曦 "晚安报告：允许你梦到错题……以及，一点点我。"
    elif love_zw > love_yx:
        show zhiwei normal at zw_left
        知微 "回去路上小心。"
        "她把社团的手电塞进你手里。那道光，一直照到校门口。"
    else:
        "夜风把那句“明天见”，吹得很轻。"

    call review_wrong from _call_review_wrong_2
    return


# ------------------------------------------------------------
# 第 3 课：基本公式表
# ------------------------------------------------------------
label lesson3:

    scene bg classroom
    show zhiwei normal at zw_teach
    show yunxi normal at yx_hover
    with Dissolve(1.0)

    知微 "第三课，把前两课的极限全算出来，就能得到这张表。"
    call show_board("board sincos")
    知微 "常数归零；xⁿ 降一次；sin 变 cos；cos 变负 sin；e^x 天下无敌，求导不变；ln x 得 1/x。"
    知微 "表不长。但它是所有后续计算的地基——今天练到条件反射为止。"
    call hide_board
    $ unlock_scene(4)
    云曦 "八题警告。这不是演习。——每三题歇一次，是我唯一的请求，社长批了。"

    call practice(L3[0:3])

    云曦 "第一场休息！按社长的规矩，休息要抽查——"
    我 "突击提问？"
    show yunxi laugh at yx_right
    云曦 "sin 的导数是——"
    我 "cos。"
    云曦 "cos 的导数是——"
    我 "负 sin。……就这？"
    show zhiwei happy at zw_teach
    知微 "就这。能把“就这”两个字说出口，才算真的会。第二段，让它们知道厉害。"

    call practice(L3[3:6], 3)

    show yunxi surprised at yx_right
    云曦 "播报播报：进度六题，错题本薄得可怜，我的鼓励库存快用完了——这让我很难办。"
    show zhiwei normal at zw_left
    知微 "最后两题的难度，是我中途偷偷调高的。公式背得再熟，也要经得起组合拳。"
    我 "……学姐，你上午明明说“今天练到条件反射为止”。"
    show zhiwei laugh at zw_left
    知微 "条件反射，包括被加难之后依然答对。开始。"

    call practice(L3[6:8], 6)

    show zhiwei laugh at zw_teach
    知微 "……比我预期快。你背公式的时候，其实不算笨。"
    我 "学姐你这是在夸我吗。"
    知微 "是。"
    show yunxi normal at yx_hover

    if love_yx > love_zw:
        云曦 "八题都扛过来了！奖励：想吃什么随便点，我记账——社长付钱。"
        show zhiwei surprised at zw_left
        知微 "为什么是我付。"
    elif love_zw > love_yx:
        show zhiwei happy at zw_left
        知微 "你今天背表的样子，很好。"
        "说完她就回头擦黑板，好像什么都没说过。"
    else:
        "走出教室，公式表还在脑子里转，像一台点唱机。"

    call review_wrong from _call_review_wrong_3
    return


# ------------------------------------------------------------
# 第 4 课：四则运算
# ------------------------------------------------------------
label lesson4:

    scene bg classroom
    show zhiwei normal at zw_teach
    show yunxi normal at yx_hover
    with Dissolve(1.0)

    call show_board("board rules")
    知微 "第四课：函数会加减乘除了。"
    知微 "和差：逐项求导，最宽容的法则。"
    知微 "乘积：(uv)′ = u′v + uv′——前导后不动，加后导前不动。"
    知微 "商：(u/v)′ = (u′v − uv′) ÷ v²——子导母不动，减母导子不动，分母要平方。"
    call hide_board
    知微 "还有一条老师不写在黑板上的法则：能先化简的，绝不硬求导。"
    云曦 "比如 (x+1)(x−1) 这种，展开只要两秒。"

    call practice(L4[0:3])

    show zhiwei normal at zw_left
    知微 "停。前三题，乘积法则基本没输，可惜商法则翻了两回车——分母忘平方，符号抄反。"
    call show_board("board rules")
    知微 "跟我再念一遍：子导母不动，减母导子不动，分母要平方。"
    我 "……这么幼稚的口诀，真的会写进正经老师的教案吗。"
    show yunxi laugh at yx_right
    云曦 "复读机已就位。观察到：嘴巴在念口诀，手已经翻开了下一题。很好。"
    call hide_board

    call practice(L4[3:6], 3)

    show yunxi normal at yx_hover
    云曦 "休息播报：检测到“先化简再求导”使用率直线上升。社长让我转告你——她看见了，她很欣慰。"
    show zhiwei serious at zw_left
    知微 "我没说过这种话。……不过，会先把 (x+1)(x−1) 展开再动手的人，确实比硬乘的——强一点。"
    我 "就一点？"
    show zhiwei laugh at zw_left
    知微 "我的标准，会跟着你的水平涨。最后两题，按上限来。"

    call practice(L4[6:8], 6)

    show zhiwei happy at zw_left
    知微 "乘积、商、化简，三条路你都走通了。中间的错题，晚上抄一遍过程。"
    我 "……果然热情里带着魔鬼。"
    show yunxi laugh at yx_right
    云曦 "魔鬼社长的教学方针：错题不过夜（大概）。"

    if love_yx > love_zw:
        云曦 "口诀念得比我的开机语还熟。来，击掌——"
        "你刚抬手，她先拍了上来。"
    elif love_zw > love_yx:
        show zhiwei normal at zw_left
        知微 "错题抄完才能走。……我陪你抄。"
        "那天社团教室的灯，比平时多亮了一小时。"
    else:
        "回家的路上，你嘴里念着 u′v+uv′——不知为何，很像一句情歌。"

    call review_wrong from _call_review_wrong_4
    return


# ------------------------------------------------------------
# 第 5 课：链式法则
# ------------------------------------------------------------
label lesson5:

    scene bg study night
    show zhiwei serious at zw_teach
    show yunxi normal at yx_hover
    with Dissolve(1.0)

    知微 "第五课，导数计算真正的分水岭：复合函数。"
    知微 "y = f(g(x))，像套娃。求导的口诀只有一句——"
    知微 "先剥外层（内层原样抄），乘以内层的导数。一层一层剥到底。"
    show zhiwei normal at zw_teach
    知微 "例如 sin 2x：外层 cos，抄下 2x，乘内层导数 2，得 2cos 2x。"
    知微 "九成的错误，都是忘了乘内层。链条断一环，整个都不对。"
    call show_board("board sincos")
    知微 "三角、指数、对数、幂，四种外壳轮流出题。准备。"
    call hide_board

    call practice(L5[0:3])

    show zhiwei normal at zw_teach
    知微 "第一段结束。回答我：sin 2x 求导，第一步动的是哪一层？"
    我 "外层。先写成 cos 2x，然后……再乘内层的导数 2。"
    show yunxi happy at yx_right
    云曦 "回答正确！奖励冷知识一条：洋葱越剥越辣眼，套娃越剥越简单——链式法则属于第二种。"
    知微 "别闹。不过他记口诀的方式是对的：先外后内，一层一层。第二段，手别停。"

    call practice(L5[3:6], 3)

    "夜风从窗缝钻进来，粉笔灰在台灯下慢慢落。"
    show yunxi sleepy at yx_right
    云曦 "错题监测：断掉的环节，高度集中在“忘了乘内层”。建议给它立一块碑，碑文写——链条断一环，全链都白干。"
    show zhiwei serious at zw_left
    知微 "最后一组，三层套娃。剥到底，第五课才算真的懂。"
    我 "剥不到底呢？"
    知微 "剥不到底，就明早重来一遍。我起得来，你也得起。"

    call practice(L5[6:8], 6)

    show zhiwei laugh at zw_left
    知微 "链式法则通关的人，计算能力已经上了一个台阶。"
    云曦 "数据同步：本次平均反应时间比第一课缩短了——唔，说人话就是，变强了。"

    if love_yx > love_zw:
        show yunxi laugh at yx_right
        云曦 "三层套娃都剥开了！你现在的脑子，转得比我的散热风扇还快。"
    elif love_zw > love_yx:
        show zhiwei blush at zw_left
        知微 "……你知道吗，你解出题时的表情——"
        "她把「最好看」三个字咽了回去，改口："
        知微 "——很稳。继续保持。"
    else:
        "深夜的走廊里，三个人的影子叠在了一起。"

    call review_wrong from _call_review_wrong_5
    return


# ------------------------------------------------------------
# 第 6 课：隐函数 · 高阶导数 · 切线方程
# ------------------------------------------------------------
label lesson6:

    scene bg classroom
    show zhiwei normal at zw_teach
    show yunxi normal at yx_hover
    with Dissolve(1.0)

    知微 "第六课，把导数用出花样：三件武器。"
    call show_board("board tangent")
    知微 "第一件：隐函数求导。x 和 y 混在一起？没关系，把整个方程对 x 求导，见 y 就乘 y′，最后解出 y′。"
    知微 "第二件：高阶导数。导数还能再求导——f″ 描述的是“变化率的变化率”。加速度，就是位移的二阶导。"
    call hide_board
    show zhiwei serious at zw_teach
    知微 "第三件，也是导数最浪漫的应用：切线方程。"
    知微 "y − f(x₀) = f′(x₀)(x − x₀)。一条直线，在某一点，与一条任意弯曲的曲线心意相通。"
    知微 "局部来看，切线就是曲线的分身。"
    云曦 "……社长，你刚才是不是在黑板上画了颗心？"
    show zhiwei blush at zw_teach
    知微 "那是坐标轴的装饰线。做题。"
    $ unlock_scene(5)

    call practice(L6[0:4])

    show zhiwei blush at zw_left
    知微 "中场休息。……刚才切线方程那道题，你取的斜率很准。"
    show yunxi surprised at yx_right
    云曦 "社长夸人了！证据已录音，期末家长在场时播放。"
    知微 "删掉。"
    云曦 "已加入「社长珍贵音频合集」，加密备份，放心。好啦——喝口水，五分钟。"
    "你去接水的时候，听见粉笔在黑板上轻轻敲了两下。"
    show zhiwei normal at zw_teach
    知微 "回来。后四题：隐函数、二阶导、切线方程，混着来。别慌——它们说到底，是同一件事：都在“变化”。"

    call practice(L6[4:8], 4)

    show zhiwei normal at zw_left
    知微 "六课全部结束。明天——不，现在，就是期末。"

    if love_yx > love_zw:
        show yunxi determined at yx_right
        云曦 "明天期末，别怕——我在最后一排，位置固定，目光免费。"
        "她难得把玩笑收了起来，句子也短了。"
        云曦 "考成什么样都行。我在这儿，这一条不改。"
    elif love_zw > love_yx:
        show zhiwei serious at zw_left
        知微 "明天的题，我全都见过。而你——"
        "她顿了顿，把「我看透你了」说成了「一起加油」。"
    else:
        "切线只碰曲线一个点，却站得很稳。"

    call review_wrong from _call_review_wrong_6
    return


# ------------------------------------------------------------
# 第 7 课：期末综合测验
# ------------------------------------------------------------
label lesson7:

    scene bg classroom
    show zhiwei serious at zw_center
    show yunxi normal at yx_hover
    with Dissolve(1.0)

    stop music fadeout 1.5
    play music "audio/bgm_tense.ogg" fadein 2.0

    "最后一课。黑板上的字被擦掉，只留下题目。"
    知微 "综合测验八题：概念、定义、公式、四则、链式、隐函数、切线——全部在里面。"
    知微 "我不在旁边看。写完，交上来。"
    show yunxi blush at yx_right
    云曦 "那我负责加油！……你、你可以的啦！"
    "教室安静得能听见粉笔灰落下的声音。"

    call practice(L7[0:8])
    $ unlock_scene(7)

    stop music fadeout 1.5
    play music "audio/bgm_warm.ogg" fadein 2.0

    show zhiwei normal at zw_left
    知微 "……写完了。"
    知微 "不管分数是多少，先说一句：七天，五十六题，你没有中途逃走。"
    show zhiwei happy at zw_left
    知微 "这一点，比及格难得多。"

    if love_yx > love_zw:
        show yunxi happy at yx_right
        云曦 "考完了考完了！先合上错题本——先去吃顿好的！这是数据的请求。"
    elif love_zw > love_yx:
        show zhiwei normal at zw_left
        知微 "……交上来了。"
        "她合上笔盖：「等成绩的时候，陪我走走？」"
    else:
        "七天的风，停在这一页上。"

    call review_wrong from _call_review_wrong_7
    return


# ------------------------------------------------------------
# 终章：成绩单
# ------------------------------------------------------------
label finale:

    $ full = total_questions * 10
    if full <= 0:
        $ full = 1
    $ ratio = float(score) / float(full)
    if ratio >= 0.9:
        $ grade = "S"
    elif ratio >= 0.75:
        $ grade = "A"
    elif ratio >= 0.55:
        $ grade = "B"
    else:
        $ grade = "C"

    scene bg study night
    show zhiwei normal at zw_left
    show yunxi normal at yx_right
    with Dissolve(1.0)

    云曦 "成绩——公布！"
    $ _tg = _("{size=44}{color=#ffd27f}最终评价：{color=#fff4e0}[grade]{/color}{/color}{/size}")
    show expression Text(_tg) as card at card_rise with dissolve
    pause 2.0
    hide card with dissolve

    sysvoice "得分 [score] / [full]　·　一次答对 [first_try_correct] / [total_questions] 题"

    if persistent.wrong_ids:
        sysvoice "错题本上还留着 [len(persistent.wrong_ids)] 题——它们会跟着你进二周目。"

    $ _runs = persistent.runs or 1
    if _runs >= 2:
        show zhiwei smug at zw_left
        知微 "第 [_runs] 次听这张成绩单，我还是把同样的话说一遍：你本来就可以。"
        知微 "区别是——上次你被我拖进来，这次是你自己走进来的。这一条比分数值钱。"

    if grade == "S":
        show zhiwei laugh at zw_left
        知微 "S。我收回第一课前你说“我数学很头疼”时的那张脸。"
        知微 "以你的水平，下一个该碰的是积分了。……寒假我给你补课。就这么定了。"
        云曦 "恭喜！我的数据库里已经给你留了“天才”这个标签，撕不下来的那种。"
    elif grade == "A":
        show zhiwei happy at zw_left
        知微 "A。稳了。切线、链式、隐函数你都站住了。"
        知微 "剩下那点错题，是熟练度问题，不是理解问题。熟练度，交给练习。"
        云曦 "A 评价！按我的统计，继续学习概率提升 400%%！"
    elif grade == "B":
        show zhiwei normal at zw_left
        知微 "B。及格，而且体面。地基是打牢了，墙还欠几层。"
        知微 "错题本我看了，集中在两三个类型上——针对性补，两周追回来。"
        云曦 "B 也是好消息：说明“完全不行”这个标签已经被覆盖了。"
    else:
        show zhiwei serious at zw_left
        知微 "C。"
        知微 "别低头。C 的意思是——这七天的内容你还没消化完，而不是你不行。"
        知微 "特训班下学期重开。而我的办公室门，这周内随时开着。"
        show yunxi blush at yx_right
        云曦 "我、我也没跑哦！错题我一道一道都归档了，陪你二周目！"

    if love_yx > love_zw:
        show yunxi blush at yx_right
        云曦 "呐，特训结束以后，我的日程表就空出来了……"
        云曦 "所以，下一个约定——周末，就、就是普通的外出！两个人。天气我都查好了。"
        云曦 "行程表上只写了两个名字。……那天要是有人约你，优先级：最低。"
        $ love_yx += 3
        show zhiwei laugh at zw_left
        知微 "黑板上的成长曲线，好像有点失控了。"
    elif love_zw > love_yx:
        show zhiwei blush at zw_left
        知微 "……结课之后，社团教室没人。"
        知微 "来帮我整理错题归档。……整理完，去吃你提过的那家关东煮。一周一次，作为惯例。"
        $ love_zw += 3
        show yunxi surprised at yx_right
        云曦 "咦、咦——那我呢？……啊我懂了，我负责记录！"

    show zhiwei normal at zw_left
    知微 "最后，送你一个东西。"
    "她递过来一支崭新的粉笔，在指间转了半圈。"
    知微 "以后看到任何曲线，都别只看到它的弯曲——"
    知微 "要看到它每一刻“正在变成”的样子。世界是变化的，导数是你读懂变化的语言。"
    show yunxi happy at yx_right
    云曦 "以及，看到切线和曲线只在一个点相遇，也要相信：只要贴合得足够好，那就是局部最优解。"
    我 "……这句是数学，还是人生？"
    show yunxi laugh at yx_right
    云曦 "是数学哦。人生那道题，超纲了，得你自己算。"

    menu:
        "（结课钟声响起）"

        "摸摸云曦的头表示庆祝":
            $ love_yx += 1
            show yunxi blush at yx_right
            云曦 "呜哇——！系统、系统过热！这是违规操作！……再、再摸一下也可以。"
            show zhiwei laugh at zw_left
            知微 "七天的特训，最后是这个场面啊。"
        "向社长鞠躬道谢":
            $ love_zw += 1
            show zhiwei blush at zw_left
            知微 "……不用行这么大的礼。"
            知微 "下次见面，希望你不用再道歉说“我不会”。"
            show yunxi happy at yx_right
            云曦 "截图归档！标题就叫《体面的学生》。"

    "错题本（如果有）："
    if wrong_list:
        $ wrong_text = (", " if _is_en() else "、").join(wrong_list)
        sysvoice "错题清单：[wrong_text]"
        sysvoice "——苏知微批注：周末重写一遍过程，下周一查。"
    else:
        sysvoice "错题清单：空。"
        show zhiwei laugh at zw_left
        知微 "……零错题。我第一次想给满分打个小抄，都找不到地方。"
        show yunxi surprised at yx_right
        云曦 "数据核对完毕：全对。玩家状态已确认为——开挂（褒义）。"

    scene bg title
    show yunxi happy at yx_right
    show zhiwei normal at zw_left
    with Dissolve(1.5)

    "数学社的灯熄了，黑板上那行字还没擦。"
    $ _tq2 = _("{color=#fff4e0}『请把“我不会”三个字，从词典里删掉。』{/color}")
    show expression Text(_tq2) as card at card_rise with dissolve
    pause 2.5
    hide card with dissolve

    "回家的路上，手机里的蓝光毫无预兆地闪了两下。"
    sysvoice "警告：检测到陌生进程正在向本机写入数据。来源：未标注。签名：云迹。"
    show yunxi surprised at yx_right
    云曦 "等等——这个签名！我的迁移日志残片里，就是这个签名！"
    "屏幕上浮起一条半透明的进度条，像有人在很远的那一头，隔着数据看你。"
    sysvoice "云迹 · 第二阶段 ——解锁进度 50%%。剩余部分，延期至：暑假。"
    show zhiwei serious at zw_left
    知微 "……谁在动你的手机？"
    "进度条像幻觉一样消散，只留下一行很小的字——"
    sysvoice "『想弄清我是谁，就把导数练到能在梦里解题。三天后的傍晚，教学楼顶层。——云迹』"
    我 "这字条是谁写的？前面明明是系统弹出来的——"
    show yunxi determined at yx_right
    云曦 "因为写它的人，就住在我残存记忆的最后一页。"
    "社长忽然从包里取出一封火漆封口的信，塞进你手里。封口的手写字迹，和刚才那行小字一模一样。"
    知微 "前代社长父亲留下的信，嘱托里写着：「特训结束那天，交给他。」……现在，还不到拆开的时候。"
    我 "……所以这七天，从头到尾都是一场——"
    show yunxi blush at yx_right
    云曦 "是一场「把你带到我们面前」的题。第二部见，笨蛋。"
    $ unlock_scene(9)

    "——《导数物语》 第一部 · 完 ——"

    stop music fadeout 3.0

    return
