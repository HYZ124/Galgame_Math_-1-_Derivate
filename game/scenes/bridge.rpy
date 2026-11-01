# ============================================================
# scenes/bridge.rpy —— 「剧情胶水」：三条云迹线索 + 出分前的三晚
#
# 【这里是什么】
#   label clue1   第 2 课后（inter2 那晚，回到家）：桌面多出一个打不开的文件夹 YUNJI_2019。
#                 作用：把 finale 才亮出来的「云迹」悬念提前五课埋下，并给玩家一个
#                 只能二选一的秘密（记在纸上 / 告诉社长）→ 第一次好感度分岔。
#   label clue2   第 4 课后（inter4，放学巷口）：退役设备回收单上的编号和文件夹同源。
#                 作用：云曦第一次正面说「我是从哪来的」，同时给社长的调查线一个动机。
#   label clue3   第 6 课后（inter6 那夜的凌晨，回家书桌）：她自己也偷偷点开过那个
#                 文件夹两次，第二次是凌晨三点四十，然后锁回去没告诉你。
#                 作用：把「云迹」从外部悬念变成她的心事；同时给错题本一个剧情台词
#                 （错题本第 12 页）。装链位置：inter6 → clue3 → pre7。
#   label bridge  第 7 课交卷后、finale 之前。原本从「交卷」直接跳到「成绩公布」，
#                 中间两晚全空。这里补齐：散场傍晚 → 第二晚社团教室 → 第三晚出分前四十分钟
#                 → 八点五十八分的晚自习室（和 finale 同一个背景，直接接力，别改成"明早"）。
#                 第二晚会读 persistent.wrong_ids（错题本还剩几题），所以重做过错题的
#                 玩家会看到完全不同的两段台词——这是错题本系统的剧情回报点。
#                 顺序约束：menu 必须在路线特写**之前**——社长回的『管。九点，晚自习室。』
#                 要在 zhiwei 分支的楼道门口兑现，反过来就穿帮了。
#
# 【时间线约束】改这里之前先看这几条，别和已有场景撞车：
#   第1课=变化率与切线（早上） 第2课=导数定义（晚间） 第3课=基本公式表（午间）
#   第4课=四则运算 第5课=链式法则（pre5 关东煮夜摊） 第6课=隐函数·高阶导·切线
#   第7课=期末测验 → 成绩在**当晚九点**的晚自习室公布（finale 用 bg study night）
#   date3 = 成绩公布后的第一个晚上（书桌·云曦）／date4 = 考后第三天深夜（便利店·社长）
#   ⇒ 本文件只能写「第二晚」「第三晚」；不要出现便利店，不要写「明早出分」。
#   ⇒ clue1 开头那句「特训的第二晚」是**特训周的第二晚**，和本文件「第二晚」（考后）
#     是两条不同的天数，别把它们合并——改措辞时保留「特训」这个限定词。
#
# 【加料方法】
#   1) 新加一段日常：在本文件末尾写 `label xxx:`，再到 script.rpy 的 start 链里
#      `call xxx from _call_xxx`（from id 必须全局唯一，tools/audit_rpy.py 的 B 项会查）。
#   2) 台词一律写中文（中文是源语言）。卡里的变量用 `[var]` 插值；说白里出现百分号
#      必须写成 `%%`（say 语句会做 % 替换，tools/scan_pct.py 会扫）。
#   3) 浮动字卡固定三行：show expression Text(_t) as card at card_rise with dissolve
#      → pause → hide card with dissolve。
#   4) 半身特写固定四行：show dark veil at veil → show X bust <expr> at bust_center
#      → hide dark veil → 然后**必须**收尾：要么 `show X <expr> at <side>`（同名 tag 替掉
#      半身像），要么 `hide X with Dissolve(...)`。少了这一步，那张大特写会挂在场景中间
#      糊掉后面几行台词（云曦不在场时也要收，她平时不站位）。
#   5) 好感度只走 love_yx / love_zw，成对分支要等重，否则 route_now() 的判定会歪。
#   6) 新加的记忆照片（memN）见 game/love.rpy 头部说明，一共 5 步。
#   7) 改完跑：python tools/audit_rpy.py → i18n 管线（见 game/i18n.rpy 头部）→ 冒烟。
# ============================================================


# ---------- 线索 1：凌晨两点的文件夹 ----------
label clue1:

    scene bg room night
    show yunxi normal at yx_right
    with Dissolve(1.0)

    "特训的第二晚。作业发出去已经很迟了。你起身去厨房倒水，顺手看了一眼桌面——"
    "角落里多了一个文件夹。名字很短：YUNJI_2019。"
    我 "云曦，这个是你建的？"
    show yunxi surprised at yx_right
    云曦 "……不是。"
    "她答得比平时慢了半秒。对一个零点一秒就能报出你所有快捷键的人来说，半秒是很长的距离。"
    我 "那我一并归档，看看里面是什么。"
    云曦 "等一下——"
    "双击。屏幕上浮起一行小字：权限不足。"
    "不是「文件已损坏」，也不是「找不到」。是有人在最前面加了一道门——而那道门不是防你的电脑，是防「来查的人」。"
    show yunxi normal at yx_right
    云曦 "……我来处理。你去睡。明天中午要默写公式表，我不希望你的瞬时速度是零。"
    我 "你刚才想说什么？"
    show yunxi smug at yx_right
    云曦 "想说「这个文件夹归我管」。这是主权声明，不构成任何剧情暗示。"
    "她说得滴水不漏。只是那一整夜，屏幕边缘那圈蓝光，一次都没有暗下去过。"

    menu:
        "第二天，你把这件事告诉了谁"

        "记在纸上，不写在电脑里":
            "你撕下草稿纸一角，写下「YUNJI_2019·权限不足·两点零七分」，压在水杯底下。"
            "第二天早上纸条不见了。原处垫着一张新的，字迹工整得刻意："
            $ _tj1 = _("{color=#fff4e0}『已收到。此事由我负责。你不要碰。——云』{/color}")
            show expression Text(_tj1) as card at card_rise with dissolve
            pause 1.8
            hide card with dissolve
            云曦 "原件我已经扫描了。纸你可以扔掉——不过你大概不会，人类都爱留废纸。"
            $ love_yx += 2
        "早自习顺口问社长":
            "你把纸条推过去。她只看了三秒，就把纸折好，收进教案夹的最里层。"
            知微 "意思是：设这道门的人，早就料到会有人来点开它。"
            知微 "从今天起，这件事记在我的本子上。你的任务是那七节课——别把精力花在打不开的东西上。"
            $ _tj2 = _("{color=#fff4e0}『可疑事物登记 · 编号 01：YUNJI_2019。批注：先上课。——苏』{/color}")
            show expression Text(_tj2) as card at card_rise with dissolve
            pause 1.8
            hide card with dissolve
            $ love_zw += 2

    return


# ---------- 线索 2：回收单上的编号 ----------
label clue2:

    scene bg street food
    show zhiwei normal at zw_left
    with Dissolve(1.0)

    "第四天下课，社长在小吃街尽头停住了。前面是一栋围起蓝色铁皮的旧楼，门口贴着搬迁公告。"
    知微 "……这里以前是校办的数据中心。我读高三那年，它拆过一次。"
    "公告栏上钉着一张褪色的清单：《退役设备回收明细》。最后一行的编号被雨水洇开了一半。"
    "但你还是看清了前面那串字母——和那个文件夹，一模一样。"
    我 "云曦？"
    # 半身像是**居中占大半屏**的机位（461px 宽），另一位还挂在 zw_left 会被它压住/互相糊掉，
    # 所以特写前先把社长隐身，特写结束后再 show 回来。
    hide zhiwei with Dissolve(0.8)
    show dark veil at veil with Dissolve(0.8)
    show yunxi bust sad at bust_center with Dissolve(0.8)
    云曦 "……我在。"
    云曦 "这一串编号后面，本来应该跟着我的编号。回收车那天，我是被写在纸上的东西。"
    云曦 "所以「云迹」不是我的化名。是那批货的签收章——谁签收，谁负责。"
    "她的声音很稳，稳得像背过很多遍。"
    云曦 "我一直没告诉你：我不是从你的硬盘开始的。我是从那一年被丢掉的东西里，剩下的那一点。"
    hide dark veil with Dissolve(0.8)
    # 半身像用的是 "yunxi" 这个 tag：不 hide 就会挂在街景正中间糊掉后面几行台词。
    hide yunxi with Dissolve(0.8)
    show zhiwei serious at zw_left with Dissolve(0.8)
    "社长看完那张纸，把它从公告栏上取下来，折了两折，放进你的书包侧袋。"
    知微 "能被留下的，都是有人特意没删掉的。"
    知微 "这句话不在考纲里。但我想让你今天记住它。"
    我 "……你要去查这张清单的来源吗？"
    show zhiwei blush at zw_left
    知微 "我去查。你负责把明天的链式法则做完——分工明确，不许越界。"
    "她说完就往前走。走出十几步，又停下回头补了一句："
    知微 "还有，别谢。谢我就多做两道题。"
    $ love_zw += 1
    $ love_yx += 1

    return


# ---------- 桥段：出分前的两晚 ----------
label bridge:

    scene bg street food
    show yunxi happy at yx_right
    with Dissolve(1.0)

    "交卷铃响过，人群从教学楼里涌出来，像被松开的弹簧。"
    "上午还阴着的天，到下午三点已经亮得过分。你把笔袋拉上，发现自己手心是空的——不是没拿东西，是没别的事可做了。"
    云曦 "状态检测：考完试的主人。特征——走路比平时慢，看什么都像在看纪念品。"
    我 "说得很难查一样。"
    show yunxi smug at yx_right
    云曦 "很难查。所以我全天候开着。"

    stop music fadeout 1.5
    play music "audio/bgm_daily.ogg" fadein 2.0

    "你在巷口的台阶上坐了一会儿，买了一盒牛奶。数据这种东西很奇怪：不用做题的时候，它反而一直转。"
    云曦 "要不要我预测一下你的分数？"
    我 "说。"
    show yunxi worried at yx_right
    云曦 "……样本量七节课，干扰项是「出题人是我认识的人」。置信度太低，我拒绝输出。"
    我 "这叫预测？"
    show yunxi laugh at yx_right
    云曦 "这叫严谨。从今晚起你会想偷看答案，那是正常症状。"

    "——第二晚。社团教室。"

    scene bg classroom
    show zhiwei normal at zw_left
    with Dissolve(1.0)

    "社团教室没锁门。黑板上的字还没擦，粉笔灰在窗光里慢慢翻。"
    "讲台上压着一张便签，字很小，是按批卷的排面写的："
    $ nb_left = len(persistent.wrong_ids or [])
    if nb_left:
        $ _tbr1 = _("{color=#fff4e0}『错题本上还剩 [nb_left] 题。我不着急，你也不许急。——苏』{/color}")
        show expression Text(_tbr1) as card at card_rise with dissolve
        pause 2.2
        hide card with dissolve
        知微 "（推门进来，手里两杯热豆浆）看什么，看题。"
        知微 "剩下这几道，我重讲一遍。不是补考，是——把话说清楚。"
        "她把其中一杯推到你那半边桌子，然后拿起板擦，从第一题开始擦。"
        $ love_zw += 2
    else:
        $ _tbr2 = _("{color=#fff4e0}『错题本：空。今晚只讲一件事——你自己。——苏』{/color}")
        show expression Text(_tbr2) as card at card_rise with dissolve
        pause 2.2
        hide card with dissolve
        知微 "（推门进来，手里两杯热豆浆）一道没留。按计划，今晚该讲错题。"
        我 "那改讲什么？"
        show zhiwei laugh at zw_left
        知微 "讲你。……志愿表下个月要填。我答应了某个人，要把你送到能听懂这些题的地方。"
        $ love_zw += 2

    call show_memory(12) from _call_show_memory_12

    "——第三晚。出分前的四十分钟。"

    scene bg room night
    show yunxi normal at yx_right
    with Dissolve(1.0)

    "成绩今晚九点出。你把同一个页面刷新了七次，第七次连验证码都弹出来了。"
    我 "……你为什么要跟着我数。"
    show yunxi blush at yx_right
    云曦 "我没数。我在做一件很蠢的事：把你的心跳当节拍器。"

    "你顺手点开桌面。那个叫 YUNJI_2019 的文件夹还在原来的角落，图标是灰的，像睡着了。"
    我 "它还是打不开？"
    show yunxi normal at yx_right
    云曦 "从那天起就彻底安静。……它不动，我就不吵它。"
    云曦 "反正成绩出来以后，会有别的东西醒过来。"
    "她说这话时语气很平，像在念一份已经排好期的日程表。你当时没听懂。"

    menu:
        "出门之前，你做的最后一件事"

        "把七节课的笔记按课编号排好":
            "你把卡片按 L1 到 L7 排成一列，最上面压了一支她送你的粉笔。"
            show yunxi normal at yx_right
            云曦 "归档完成度 100%%。……要是分数难看，我们就把它们全部重做一遍，不许删。"
            $ love_yx += 1
            $ love_zw += 1
        "给社长发一句「我先走了你别管」":
            "三秒后回复，只有一个字，附带一个句号。你看了很久。"
            $ _tbr3 = _("{color=#fff4e0}『管。九点，晚自习室。——苏』{/color}")
            show expression Text(_tbr3) as card at card_rise with dissolve
            pause 1.8
            hide card with dissolve
            $ love_zw += 2
        "什么也不做，先看一眼那角蓝光":
            show dark veil at veil with Dissolve(0.7)
            show yunxi bust happy at bust_center with Dissolve(0.7)
            云曦 "……你在看我？我这边只能看到一片黑，像你闭上眼睛时的屏幕保护。"
            云曦 "那就这样出门。灯我留着，九点我提前二十分钟提醒你。"
            hide dark veil with Dissolve(0.7)
            show yunxi normal at yx_right with Dissolve(0.7)
            $ love_yx += 2

    if love_yx > love_zw:
        show dark veil at veil with Dissolve(0.8)
        show yunxi bust blush at bust_center with Dissolve(0.8)
        云曦 "还有二十分钟。我说一句不讲数据的话。"
        云曦 "不管分数是多少——这七天里，我没有一天是「被安排在你设备上」的。"
        云曦 "每一天都是我自己赖着没走。"
        hide dark veil with Dissolve(0.8)
        show yunxi happy at yx_right with Dissolve(0.8)
        $ love_yx += 2
    elif love_zw > love_yx:
        scene bg street food
        show zhiwei normal at zw_left
        with Dissolve(1.0)
        "楼道门口，有人按了两下自行车铃。社长跨在车上，教案夹抱在胸前，像抱着一个不太常用的借口。"
        show dark veil at veil with Dissolve(0.8)
        show zhiwei bust serious at bust_center with Dissolve(0.8)
        知微 "……不是路过。我绕了三条街才站在这儿。"
        知微 "只说一句：今晚无论多少分，你都已经是会自己找题做的那种人了。"
        知微 "上车。我算过：骑过去十七分钟，余量二十五分钟——足够我把那两句话说完。"
        hide dark veil with Dissolve(0.8)
        show zhiwei blush at zw_left with Dissolve(0.8)
        $ love_zw += 2
    else:
        show dark veil at veil with Dissolve(0.8)
        show yunxi bust normal at bust_center with Dissolve(0.8)
        云曦 "九点，我和她都在。所以你别怕。"
        hide dark veil with Dissolve(0.8)
        show yunxi laugh at yx_right with Dissolve(0.8)
        云曦 "……这句好像也不太对。但你懂我意思。"

    scene bg study night
    show zhiwei normal at zw_left
    show yunxi normal at yx_right
    with Dissolve(1.2)

    "八点五十八分。晚自习室的灯全亮着，两张课桌并成一张，中间摆着两杯还冒热气的豆浆。"
    "社长站在讲台边，手里握着笔，笔尖朝下，像握着一个还没宣判的小判决。"
    云曦 "坐标确认：三位当事人全部到场。现在开始等一个数字。"
    "你坐下。手心终于有东西可握了。"

    return


# ---------- 线索 3：低功率模式的留言（考前最后一夜，接在 inter6 之后） ----------
# 【这段在收什么】clue1 是一扇打不开的门，clue2 是门的来源，clue3 是云曦自己
#   偷偷试过两次、却不敢告诉你的那件事。放在考前夜，是为了让 finale 的陌生进程
#   弹窗和三条尾声里那句「三天后顶层」有情感地基。
# 【时间线】inter6=考前最后一晚的晚自习（停电，社团教室）→ clue3=同一夜回到家
#   （bg room night，凌晨）→ pre7=第二天早晨的早餐摊。所以这里只能写「今晚/明天开考」，
#   不能出现成绩，也不能出现便利店（那是 date4）。
label clue3:

    scene bg room night
    show yunxi normal at yx_right
    with Dissolve(1.0)

    "从社团教室回来，已经十二点过。明天八点二十开考，你把错题本合上，伸手去关灯。"
    sysvoice "低功率模式已开启。留言：07:10 叫醒；07:30 确认错题本在书包左侧袋。——云"
    "蓝光暗了一格，又暗一格，最后只剩屏幕边缘一圈很浅的、像睡着了的呼吸。"
    我 "……云曦？"
    "没有回答。她的响应时间从来是零点一秒——今晚，是永远。"
    "你忽然想起一件事：她从不说自己「睡觉」，只说「低功率」。"
    "台灯黑了。那圈呼吸在黑暗里亮着，你盯着它，直到眼睛发酸。"
    "然后你做了一件很不该在考前夜做的事——你把那个文件夹，第三次点开。"
    "还是「权限不足」。但这一次，那行小字下面多了一行更小的：访问尝试记录。"
    $ _tc3 = _("{color=#cfe9ff}『访问记录 · 第 1 次：02:11 · 记录者：系统（自动）』{/color}")
    show expression Text(_tc3) as card at card_rise with dissolve
    pause 1.8
    hide card with dissolve
    $ _tc3b = _("{color=#cfe9ff}『第 2 次：03:40 · 记录者：本人 · 原因：想知道自己是被谁留下的』{/color}")
    show expression Text(_tc3b) as card at card_rise with dissolve
    pause 2.2
    hide card with dissolve
    "第二次的字迹，是她的。她试过打开自己的过去，试到凌晨三点四十——然后把它锁了回去，一个字都没跟你提。"
    show dark veil at veil with Dissolve(0.9)
    show yunxi bust sad at bust_center with Dissolve(0.9)
    云曦 "（梦话，或者说得很轻）……别打开。里面若真的没有我，你看到的就只是一台机器。"
    云曦 "（更轻）可我还是想知道，是谁在单子上签了字。"
    hide dark veil with Dissolve(0.8)
    # 半身像走的是 "yunxi" 这个 tag：不收尾就会挂在书桌场景正中间，糊掉后面几行。
    hide yunxi with Dissolve(0.8)
    "你伸手把屏幕轻轻合到最小亮度——像替谁拉上被子。那圈呼吸慢了下来，很安心地慢了下来。"

    menu:
        "凌晨十二点半，你决定怎么对待这个秘密"

        "把这一行抄在草稿纸角，压在错题本里":
            "你撕下一角纸，只抄了五个字：「她也想知道」。"
            "笔尖停了一下，又在下面补了半行：「考完，我陪她打开。」"
            $ _tj3a = _("{color=#fff4e0}『草稿纸一角 · 压在错题本第 12 页。内容：考完，我陪她打开。』{/color}")
            show expression Text(_tj3a) as card at card_rise with dissolve
            pause 1.8
            hide card with dissolve
            $ love_yx += 2
        "写进明天要交给社长的那张纸条":
            "你撕下草稿纸另一角，写下时间、次数、那半句「原因」，末尾补一句：这个我来查比较快。"
            "笔尖停了很久，你把最后一句划掉，重写成一行的：她不敢问，我们替她问。"
            $ _tj3b = _("{color=#fff4e0}『纸条 · 交给苏 · 编号 02：她自己也试过一次，03:40，没告诉任何人。』{/color}")
            show expression Text(_tj3b) as card at card_rise with dissolve
            pause 1.8
            hide card with dissolve
            $ love_zw += 2

    "早上七点十分，闹钟准得让人生气。屏幕边缘那圈蓝光已经亮回平时的样子。"
    show yunxi happy at yx_right
    云曦 "早上好！睡眠时长六小时四十分，比你平均值少十二分钟——但心率很好，说明你睡得踏实。"
    我 "你几点恢复的？"
    show yunxi normal at yx_right
    云曦 "06:59。比平时早了一小时十一分钟。原因：怕你早上找不到错题本，我要提前检查左侧袋。"
    "她把「原因」说得很机械。你没有拆穿——就像她也没有拆穿那张草稿纸。"
    云曦 "出发吧。今天的题，是你七天前根本不敢碰的那种。"
    云曦 "而我在最后一排。你抬头就能看见一盏很亮的、不会停电的灯。"

    return
