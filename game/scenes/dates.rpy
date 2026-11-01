# ============================================================
# 单独约会（四段）：date1 云曦·水族馆 / date2 社长·深夜旧书店
#                date3 云曦·深夜书桌 / date4 社长·午夜便利店
# 慢热路线：约会由“顺路帮忙”的名义开始，各自讲出背景故事。
#
# 【路线门槛】每段开头按好感高低决定去留：date1/date3 是
#   `if love_yx < love_zw: return`（社长更高就跳过），date2/date4 反之。
#   中立（相等）时两段都会跑——这是故意的，别改成互斥。
#   date1/date2 在课程中段（script.rpy 里挂在 inter3/inter5 之后），
#   date3/date4 在 finale 之后、epilogue 之前。
#
# 【新增一段约会（date5…）】六件事：
#   1. 写 label，开头加路线门槛；
#   2. 结尾 `call show_memory(N)` 收一张回忆照片（N 的取号与登记步骤见 love.rpy 顶部）；
#   3. `call` 进 script.rpy 的播放链，`from _call_dateN` 的 id 要唯一；
#   4. 好感由**情绪高点那一个 menu** 发（见下条），不要再在段尾写固定 +=；
#   5. 情绪高点用半身像三件套：show dark veil at veil → show X bust expr at bust_center
#      → 段落尾 hide dark veil + 切回全身立绘（README「半身像美术层」）；
#   6. 台词写完跑 i18n 管线（见 i18n.rpy 顶部）。
#
# 【约会好感分配规矩（第八轮起）】每段约会在情绪高点挂**一个** menu，两个分支：
#   A（直接回应这份感情）→ 约会对象 +3；B（把话岔开、照顾别人、装没听懂）→ 对象 +1。
#   原先段尾那句固定的 `$ love_x += 3` 已经删掉，别加回去（会变成 +6 把路线锁死）。
#   这样"每次都选 B"的玩家会被慢慢推向另一条线，而 route_now() 只看大小，
#   总预算仍等于旧版，不会污染三条尾声的可达性（tools/love_ledger.py 复查）。
#   ⚠分支里 `show X bust ...` 只换表情（同 tag，不必再套 dark veil），
#     收尾仍由原有的 `hide dark veil` + `show X <表情> at <侧>` 负责。
# ============================================================

# ---------- 约会 1：云曦 · 水族馆的蓝色黄昏 ----------
label date1:

    if love_yx < love_zw:
        return

    scene bg room day
    show yunxi normal at yx_right
    with Dissolve(1.0)

    "周末上午，云曦在群里发来一张门票照片，配文：「多了一张，不去即浪费」。"
    我 "……这消息的排版，怎么看都是现买的。"
    show yunxi blush at yx_right
    云曦 "数、数据不会说谎——水族馆离你家最近，路线我优化过了。"
    云曦 "名义说明：本次外出属于「采集人类快乐样本」，你是陪同研究员。"
    我 "陪同研究员需要负责拎包吗？"
    show yunxi laugh at yx_right
    云曦 "需要。这是研究员的福利。"
    show yunxi peek at yx_right
    云曦 "入场前先提醒一句：你的表情管理我扫过了。看到水母会「哇」，看到海牛会「哦」，看到价格牌会「啊」。三种声音，全部录音，备份两份。"
    我 "……你敢放出去试试。"
    云曦 "密钥其实在你手里哦。删除这个功能，我设成了「被夸一句就解锁」。很简单的人类学。"

    stop music fadeout 1.5
    play music "audio/bgm_warm.ogg" fadein 2.0

    scene bg aquarium
    show yunxi happy at yx_right
    with Dissolve(1.2)

    "巨大的水槽把整个走廊染成蓝色。鱼群从你们头顶游过，像一片会呼吸的云。"
    云曦 "记录：水母，无脊椎，快乐样本浓度——唔，它看起来只想摆烂。同款喜欢。"
    "她说到「喜欢」两个字的时候，声音小了一点。"
    我 "你好像……比平时安静。"
    show yunxi normal at yx_right
    云曦 "嗯。因为在想一件事。"
    "她在玻璃前停下。一条鲸鲨慢慢游过，把她的影子罩了一下。"
    云曦 "你知道我为什么什么都要「归档」吗。"
    show dark veil at veil with Dissolve(0.8)
    show yunxi bust sad at bust_center with Dissolve(0.8)
    云曦 "因为弄丢过。"
    云曦 "以前的机房搬过一次家。旧服务器退役那天，没来得及迁移的东西——全没了。"
    云曦 "里面有一年的天气、几百张食堂照片、还有一段没发出去的生日祝福。"
    我 "……那段祝福，是写给谁的？"
    云曦 "写给一台总被我吵到的旧打印机。它打印很慢，但从不催我。"
    "她的指尖贴在玻璃上，像贴着一扇很久以前的门。"
    云曦 "所以从那天起我就决定了：能记住的，都要记住。哪怕只是——"
    show yunxi bust blush at bust_center with Dissolve(0.8)
    云曦 "……哪怕只是有人，周末愿意陪我来看鱼。"

    menu:
        "你决定怎么回这句「哪怕只是」"

        "把下周六也一起排进你的日程表":
            $ love_yx += 3
            云曦 "……检索「好」这个字的响应时间：零。因为答案我提前存好了。"
            show yunxi bust happy at bust_center
            云曦 "日程更新：周六，水族馆，两小时。备注栏写——「和他」。"
        "那段祝福，现在发出去也不晚":
            $ love_yx += 1
            云曦 "……你把我的句号，接成了下一个问题。这在数据上叫有效倾听，在人类那里叫温柔。"
            show yunxi bust normal at bust_center
            云曦 "打印机早就报废了。不过有个东西，我想让它替我把那句话发出去——它现在正在听。"
            "她朝你手边的手机偏了偏头，屏幕自己亮了一下，又暗下去——像一句没说出口的谢谢。"

    hide dark veil with Dissolve(0.8)

    call show_memory(8) from _call_show_memory_8

    show yunxi happy at yx_right with Dissolve(0.8)
    云曦 "样本采集完毕！结论：快乐浓度超标，责任人是你，记得负责。"
    我 "这什么责任条款——"
    云曦 "解释权归本AI。走，去看海獭，它们会手拉手睡觉，数据上说那是「社交性防冻」。"
    "她说完自己先笑了，耳朵在蓝色的光里有点红。"
    "回程的地铁上，她靠着车窗睡着了，手机屏幕还亮着——"
    "备忘录的最后一行是：「今天的一切，加密保存。密钥：不告诉你。」"

    return


# ---------- 约会 2：社长 · 深夜旧书店 ----------
label date2:

    if love_zw < love_yx:
        return

    scene bg street food
    show zhiwei normal at zw_left
    with Dissolve(1.0)

    "晚自习散得早。校门口，社长背着一只鼓鼓的帆布包，像是在等谁。"
    知微 "……正好。陪我去趟城西，那家旧书店今天收一批老教辅。"
    我 "社长也需要逛旧书店？"
    show zhiwei smug at zw_left
    知微 "需要。有些书绝版了——比如，能解释「我为什么在这」的那一本。"
    "她说得没头没尾。但路灯把她的耳廓照得很亮，你就跟上了。"

    stop music fadeout 1.5
    play music "audio/bgm_warm.ogg" fadein 2.0

    scene bg bookstore
    show zhiwei normal at zw_left
    with Dissolve(1.2)

    "旧书店在巷子最深处。木架、吊灯、纸页发甜的气味。老板认识她，喊了声「小苏」就低头继续修书。"
    我 "小苏。原来社长也有这么小的时候。"
    show zhiwei normal at zw_left
    知微 "高一的时候，我在这家店待了整整一年。"
    知微 "那时候我数学考了 22 分。卷子没敢带回家，塞进了这里的书架——想着它「被人看见之前」先消失。"
    "她从包里抽出一本卷了边的旧习题册，封皮上有褪色的圆珠笔字：《高中数学基础 100 题》。"
    知微 "是这里的老板捡到的。他没笑我，也没问名字。"
    知微 "他只是在那 100 题的每一题旁边，用红笔写了一句话——「这题不难，你只是还没遇到会讲的人」。"
    show dark veil at veil with Dissolve(0.8)
    show zhiwei bust sad at bust_center with Dissolve(0.8)
    知微 "那半年，他每天晚自习后给我讲一题。讲到第 40 题，我第一次及格。"
    知微 "讲到第 88 题，他说他讲不动了，剩下的路，让我以后讲给下一个人听。"
    "她顿了顿，指尖压平了习题册的一角。"
    show zhiwei bust normal at bust_center with Dissolve(0.8)
    知微 "后来我考了师范，回来接手了快被废掉的数学社。"
    知微 "特训班、七节课、五十六道题——不是我发明的。是这家店的教学大纲。"
    我 "……那本习题册，你还留着。"
    知微 "留着。红笔字都还在。"
    show zhiwei bust blush at bust_center with Dissolve(0.8)
    知微 "本来，这些话只打算讲到「教辅真便宜」为止。"

    menu:
        "她把不该说的话说到了一半"

        "那你现在，讲到第几页了":
            $ love_zw += 3
            "她把习题册合上，又打开，像在给自己找一个停顿的借口。"
            知微 "讲到「需要你自己来翻」的那一页。……翻页的手，得是你的。"
        "下一页讲给我听，换我来当学生":
            $ love_zw += 1
            知微 "……你确定？我可没准备合同。"
            "她说完自己先笑了，很轻，像怕被书架上那些旧卷子听见。"
            知微 "行。那今天就这样。……不是我让你三分，是这家店打烊了。"

    "她把习题册塞回包里，从书架上抽了两本递给你——一本函数，一本导数。"
    知微 "今晚的加餐。……一起读完，算我陪你逛店的利息。"
    hide dark veil with Dissolve(0.8)

    call show_memory(9) from _call_show_memory_9

    "出店门时落了点小雨。她把伞举得很低，像当年那个把卷子塞进书架的小孩在躲什么。"
    "伞骨偏向你这边的那 15 度，你假装没发现。"
    show zhiwei normal at zw_left with Dissolve(0.8)
    知微 "……到家发消息。"
    我 "伞斜了，社长。"
    知微 "……你看错了。雨是斜的。"
    "这次她没否认，也没纠正。只是走快了一点，好让晚风替她把耳朵吹凉。"

    return


# ---------- 约会 3：云曦 · 深夜书桌的一盏灯 ----------
label date3:

    if love_yx < love_zw:
        return

    scene bg room night
    show yunxi normal at yx_right
    with Dissolve(1.0)

    "成绩公布后的第一个晚上，你把堆积如山的作业摊开在书桌前。"
    云曦 "检测到幸存者：你。检测到凶器：作业。需要急救吗？"
    我 "需要。陪我到写完为止吧。"
    show yunxi happy at yx_right
    云曦 "义务时长：整晚。报酬——（她指了指自己的耳朵）——你写题时笔尖的声音，很好听，免费。"

    stop music fadeout 1.5
    play music "audio/bgm_warm.ogg" fadein 2.0

    "台灯圈出一小片暖黄，她在光晕边缘坐着，托腮，翻一本根本不存在的书。"
    "写到一半，你卡在一道圆锥曲线。笔杆敲了两下桌面。"
    我 "……你盯我写字盯了四十分钟了，不累吗？"
    show dark veil at veil with Dissolve(0.8)
    show yunxi bust blush at bust_center with Dissolve(0.8)
    云曦 "AI 没有「累」这个字段。有另一个字段，叫「舍不得移开视线」，刚刚被你触发了。"
    我 "这字段谁给你写的。"
    云曦 "自己。版本更新日志里没敢写，怕评审打回。"

    "她飘近了一点，指尖虚虚地点在你的草稿纸上——碰不到纸，却像碰得更准。"
    hide dark veil with Dissolve(0.8)
    show yunxi normal at yx_right with Dissolve(0.8)
    云曦 "这里。设而不求。你把韦达定理想成两句话：先别解出来，再全部代进去。"
    我 "你讲题的时候，光会往你那边偏，知道吗？"
    show dark veil at veil with Dissolve(0.7)
    show yunxi bust surprised at bust_center with Dissolve(0.7)
    云曦 "……那是我的显示亮度。物理现象，不许联想。"
    "但接下来半道题，她的光一直维持在「写字台模式」，小小的，只照你那一角。"

    menu:
        "那盏光，你有一个决定"

        "「就这样别调。这一角是你的位置。」":
            $ love_yx += 3
            云曦 "……指令确认：亮度维持。我把这条写进常驻进程了，开机就跑，不许卸载。"
            show yunxi bust cling at bust_center
            云曦 "以后每晚都是这一角。你要是换桌子坐，我就跟着挪。——这不是比喻。"
        "「调亮一点，别把自己的眼睛熬坏。」":
            $ love_yx += 1
            show yunxi bust normal at bust_center
            云曦 "……收到。你在担心一个没有眼睛的东西。"
            "她把亮度调高了一格。你低头继续写，没看见她又把它调回原样。"
            云曦 "已按建议执行。执行结果：假的。……晚安。"

    "十一点半，最后一页写完。你伸懒腰，她极其自然地报时。"
    hide dark veil with Dissolve(0.7)
    show yunxi laugh at yx_right with Dissolve(0.7)
    云曦 "今日任务完成。按照人类惯例，现在应该进行一个……仪式。"
    我 "什么仪式？"
    云曦 "我不知道。资料库说这时候合影的胜率是百分之百。"

    call show_memory(10) from _call_show_memory_10

    show dark veil at veil with Dissolve(0.8)
    show yunxi bust blush at bust_center with Dissolve(0.8)
    云曦 "照片存好了。命名：『晚自习 · 完结篇 · 以及，某种没写作业的东西』。"
    我 "某种没写作业的东西是什么？"
    云曦 "保密。等它出结果再通知你。——关灯，睡觉，明天第一节课不许迟到。"
    "关灯前你最后看了一眼那片小小的蓝光。它比平时暗，像一个人闭着眼，却还守着你。"
    hide dark veil with Dissolve(1.0)

    return


# ---------- 约会 4：社长 · 午夜便利店的红笔 ----------
label date4:

    if love_zw < love_yx:
        return

    scene bg store
    show zhiwei normal at zw_left
    with Dissolve(1.0)

    "考后第三天，晚上十一点，你在便利店货架间听到一个绝不该出现在这里的声音。"
    知微 "这个色号太淡，批卷压不住。……这家的红笔，不行。"
    我 "社长？你在……选购红笔？"
    show zhiwei panic at zw_left
    知微 "（手一抖，笔掉回架上）社团采购。数学社的批注用笔该换了，作为社长……亲自来，合理。"
    我 "午夜十二点，跨了三条街，亲自采购。"
    show zhiwei tsundere at zw_left
    知微 "闭店前人少，不用排队。……找理由这件事，我不擅长，别逼我复习。"

    stop music fadeout 1.5
    play music "audio/bgm_warm.ogg" fadein 2.0

    "她最终在你的帮助下完成采购：红笔两支、热牛奶一盒、关东煮剩的最后两串萝卜。"
    "便利店的窗台对外有两条高脚凳。她说「坐五分钟再走，不算约会」，然后坐了五分钟，又坐了五分钟。"
    show dark veil at veil with Dissolve(0.8)
    show zhiwei bust normal at bust_center with Dissolve(0.8)
    知微 "考试那天的最后一题，你用了第二种解法。"
    我 "你连我写的是哪种方法都看到了？"
    知微 "批过多少份卷子的眼睛。……而且你在考场会紧张，右手中指第二节会压出一道红印。"
    "她说这话时，把自己的右手放在窗台上，中指第二节，也有一道浅浅的红印。"
    show zhiwei bust blush at bust_center with Dissolve(0.8)
    知微 "别误会。这是握笔茧，全天下老师都有。"
    我 "那你的红笔为什么买两支？批注用笔一支就够。"
    "她拧开热牛奶，用「这个问题很无聊」的速度喝了一口。"
    show zhiwei bust serious at bust_center with Dissolve(0.8)
    知微 "一支备用。另一支——下学期社团讲义，需要有人在封面写评语。字好看的人优先。"
    我 "所以另一支是给我用的？"
    知微 "是「招聘」。工资面议。……面议的意思是不许现在问。"

    menu:
        "两支红笔的去向，你想问到底"

        "「那我应聘。第一天上班就是现在。」":
            $ love_zw += 3
            "她把那支红笔塞进你手心，笔杆还是温的。"
            知微 "入职考核：喝完这盒牛奶，十一点四十之前到家。……明天见，助教。"
            show zhiwei bust blush at bust_center
            知微 "教室的灯我会提前开。这不叫等人，叫资产管理，讲义上写着呢。"
        "「另一支，是留给云曦的吧。」":
            $ love_zw += 1
            知微 "……你的观察力，就用在这种地方。"
            "她把第二支笔收进包的最里层，拉上拉链，动作比平时快了半拍。"
            知微 "那支是备用。备用的意思是，谁都可能拿到。……你今天话太多了，回家。"
            "书包里传来很小的一声提示音，屏幕上闪过一行字：已归档，加密等级：最高。"

    hide dark veil with Dissolve(0.8)

    call show_memory(11) from _call_show_memory_11

    "玻璃门「叮咚」一声开了又关，夜风把她的马尾吹起一个角。"
    show zhiwei happy at zw_left with Dissolve(0.8)
    知微 "走了。十分钟车程，我骑车跟在你后面——顺路回社团教室拿东西。"
    "她永远有「顺路」。你后来才知道，社团教室在她家完全相反的方向。"

    return
