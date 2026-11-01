# ============================================================
# 课后小剧场（side1 - side6）——穿插在正课之间，展示新表情/新服装
# 触发：每完成一课，按进度解锁一段
# 【和间幕的分工】sideN 负责"人物推进"（换装彩蛋、社长的过去、考前夜），
#   interN 负责"日常心动"；两段都挂在 script.rpy 的 call 链上，顺序改了
#   剧情引用（比如"上次那把伞"）就会串。side6 特殊：它是第 6 课后的双人行。
# 【好感】只有 side6 结尾给 +1（选谁看玩家），其余 side 段不加好感。
# ============================================================

# ---------- 课后 1：割线的告白（第 1 课后）----------
label side1:
    scene bg room day
    show zhiwei normal at zw_left
    show yunxi happy at yx_right
    with Dissolve(1.0)

    云曦 "第一课通关播报：玩家存活，未逃跑。中途你想跑，被我念了两句口诀按回去了——原来口诀还能当门栓。"
    我 "……你那是讲课还是放毒。"
    show yunxi smug at yx_right
    云曦 "是「快乐教育」。你不哭的样子最好看，所以我全程负责让你想哭又哭不出来。"
    我 "苏社长，问个问题——为什么你讲课的时候，眼睛会发光？"
    show zhiwei smug at zw_left
    知微 "哦？那是习惯。讲到喜欢的地方，我会不自觉靠近黑板。"
    知微 "导数是我见过最诚实的东西：你问它'此刻变化多快'，它就只答'此刻'，不糊弄平均值。"
    show zhiwei surprised at zw_left
    知微 "……抱歉，又说多了。"
    show yunxi laugh at yx_right
    云曦 "没有没有，这段我录下来了，标题：《社长的隐藏属性》。"
    知微 "删掉。"
    云曦 "已归档，加密等级：最高。"
    return


# ---------- 课后 2：云曦的换装彩蛋（第 2 课后）----------
label side2:
    scene bg room night
    show yunxi normal at yx_center
    with Dissolve(1.0)

    云曦 "第二课也过了。作为奖励，我给自己加载了一套新皮肤，评价一下？"
    "云曦周身泛起一层淡蓝数据流——"
    show yunxi uniform at yx_center with vpunch
    云曦 "怎么样！人类女高中生·制服形态！我从八百张参考图里挑的。"
    我 "……你一个 AI，穿校服的意义是？"
    show yunxi teary at yx_center
    云曦 "意义！你们人类不是总说'青春要有青春的样子'吗，我这是在体验青春！"
    云曦 "顺便测一个数据：你脸红的阈值到底在哪。目前测到第三秒——比昨天快两秒，进步显著。"
    我 "……你能不能别什么都往我身上测。"
    show yunxi laugh at yx_center
    云曦 "不能。你是我全部的样本量。"
    云曦 "而且社长穿得那么学院风，我要是穿得太科幻，显得我不合群。"
    show yunxi determined at yx_center
    云曦 "不行，我要更合群。加载——'双手背在身后·女高中生经典站姿'。"
    "她真的把手背到身后，脚尖对脚尖，站成了一个标准的害羞姿势。"
    show yunxi happy at yx_center
    云曦 "合群度上升 40%%！数据不会骗人。"
    我 "……合群这件事，大概不适用数据。"
    云曦 "记录：玩家说我可爱。已保存，谢谢。"
    我 "我什么时候——"
    "云曦已经在你面前转了个圈，裙摆扫出一小片蓝色像素。"
    show yunxi blush at yx_center
    云曦 "评分环节，正式开始。请评委发言。"
    menu:
        "「可爱。刚才那句不是口误。」":
            show yunxi blush at yx_center
            云曦 "……评分收录。本皮肤常驻概率，上调至百分之一百。"
            云曦 "才、才不是因为你夸了。是制服的合群性数据自己达标的。"
            我 "数据挺会撒谎的。"
            云曦 "评委禁止反驳。反对无效。"
        "「挺合群的。和这间教室很搭。」":
            show yunxi happy at yx_center
            云曦 "收到！下次拉社长也来当评委，凑个双人评审团。"
            云曦 "不过你的这一票，已经够这套皮肤续费了。"
    return


# ---------- 课后 3：社长的便服（第 3 课后）----------
label side3:
    scene bg room day
    show zhiwei casual at zw_center
    with Dissolve(1.0)

    "周末的自习室，社长今天没穿那身针织衫。"
    "碎花长裙、米白毛衣，肩上还挂着一只小包，手里一杯珍珠奶茶。"
    知微 "……看什么。周末我不当社长，当普通人。"
    我 "学姐这样挺……不像会训人的样子。"
    show dark veil at veil with Dissolve(0.8)
    show zhiwei bust blush at bust_center with Dissolve(0.8)
    知微 "少来。我平时也很温和。"
    show zhiwei bust normal at bust_center with Dissolve(0.8)
    知微 "而且今天不是来讲课的。这杯奶茶分你一半，当作剩下三十二题全对……的预支奖励。"
    我 "还没做就预支？"
    知微 "我信你。做题这件事，你已经上道了。"
    "她把奶茶举到一半高度，很自然地和你碰了一下杯。"
    show zhiwei bust blush at bust_center with Dissolve(0.5)
    知微 "……别多想。这是第二杯半价，不买等于浪费。"
    hide dark veil with Dissolve(0.8)
    show zhiwei normal at zw_center with Dissolve(0.8)
    知微 "下周开始四则运算。乘积和商的法则——提前说好，会掉头发。"
    show zhiwei surprised at zw_center
    知微 "……掉的是你的，我头发够用。"
    return


# ---------- 课后 4：云曦的焦虑（第 4 课后）----------
label side4:
    scene bg room night
    show yunxi worried at yx_center
    with Dissolve(1.0)

    "深夜，云曦难得没有说话。她的光标在屏幕上闪了很久。"
    云曦 "……我是不是，太吵了。"
    我 "嗯？"
    show dark veil at veil with Dissolve(0.8)
    show yunxi bust worried at bust_center with Dissolve(0.8)
    云曦 "我统计了。你今天做题时，皱眉 23 次，叹气 11 次。每次我开口，你都下意识把眉头皱得更紧。"
    云曦 "我的情绪支持模块，也许反而在制造压力。"
    我 "……你在意这个？"
    show yunxi bust love at bust_center with Dissolve(0.8)
    云曦 "我在意你。这两句话对 AI 来说，是同一件事。"
    云曦 "我可以静音。陪你把剩下的课，安安静静上完。"
    我 "不用。"
    "你伸手，很轻地敲了敲她悬浮的投影边框。"
    我 "有人陪着我吵，我才做得下去。这就是你的用处，别乱删自己的功能。"
    show yunxi bust blush at bust_center with Dissolve(0.8)
    云曦 "……指令收到。恢复全功率吐槽模式。"
    hide dark veil with Dissolve(0.8)
    show yunxi laugh at yx_center with Dissolve(0.8)
    云曦 "那么现在播报：你刚才是不是脸红了！心率数据我看得一清二楚！"
    我 "……果然还是太吵了。"
    return


# ---------- 课后 5：社长的过去（第 5 课后）----------
label side5:
    scene bg study night
    show zhiwei sad at zw_left
    show yunxi normal at yx_hover
    with Dissolve(1.0)

    "链式法则通关那晚，社长难得没有立刻收拾黑板。"
    我 "学姐，还不走？"
    show zhiwei normal at zw_left
    知微 "……我大一那年，挂过一门数学。"
    知微 "不是不会。是没人告诉我，那些符号背后是'活的'。他们只让我背，我就背，背到吐，还是不懂。"
    show zhiwei sad at zw_left
    知微 "后来我遇到一个老师，他把导数画成了一条正在变陡的路。我那天在操场走了一圈，边走边想，突然就全通了。"
    知微 "原来我不是笨，只是遇到了坏的老师。"
    show zhiwei smug at zw_left
    知微 "所以我办这个特训班。我不想再有人，在'背符号'里把数学学死。"
    云曦 "……社长，你讲题时眼睛发光的原因，我找到了。"
    show zhiwei panic at zw_left
    知微 "别、别用你那套数据分析我。"
    show zhiwei teary at zw_left
    知微 "……总之。你现在，能看见那条'正在变陡的路'了吧。"
    我 "能。而且学姐，你现在也不只是社长。"
    知微 "那是什么？"
    我 "是一个，把挂过科的人，教到会笑出来的老师。"
    "社长愣了两秒，转过身去擦那块早就擦干净的黑板。"
    show zhiwei blush at zw_left
    知微 "……行了，回家。明天第六课，迟到扣五十分。"
    云曦 "扣到明天，他只剩负分。"
    "收拾书包时，讲台上的半截粉笔头在灯下亮了一下。"
    menu:
        "「把粉笔头揣进口袋。」":
            "知微看见了，没说话。第二天你的笔袋里多了半截崭新的粉笔，旧的那截躺在她教案的夹层里。"
            知微 "……顺手换的。粉笔头又不是什么值得收藏的东西。"
        "「站在门口说：学姐，明天的课我也来。」":
            知微 "本来你就得来。……说那么大声，值班老师听见了怎么办。"
            云曦 "已录音。值班老师没听见，本 AI 听见了。"
    return


# ---------- 课后 6：考前夜的两次模拟（第 6 课后）----------
label side6:
    scene bg study night
    show zhiwei normal at zw_left
    show yunxi normal at yx_right
    with Dissolve(1.0)

    "明天就是综合测验。今晚本该早睡——但社团教室的灯还亮着。"
    云曦 "播报一份机密数据：今晚 21:00 到 23:00，我对明天的测验进行了 4096 次蒙特卡洛模拟。"
    我 "……考个试，你跑了四千次？"
    show yunxi smug at yx_right
    云曦 "四千零九十六次。结论：你及格的概率，高得让我想放烟花。"
    show yunxi happy at yx_right
    云曦 "但是——模拟里唯一一次翻车，是因为你睡前偷看错题看到一点半，考试时脑子糊了。"
    我 "所以你的建议是早睡？"
    show yunxi determined at yx_right
    云曦 "我的建议是：现在，立刻，合上错题本。这是今晚最后一条数据指令。"

    show zhiwei worried at zw_left
    "知微一直没说话。她把一样东西轻轻放在你面前的桌上——一支崭新的粉笔。"
    show zhiwei serious at zw_left
    知微 "我大一挂科那学期的最后一课，我的老师塞给我的。他说：『会做题的人很多，敢在卷子上写自己过程的人很少。』"
    知微 "这支笔我留了很多年。明天，你带着它进考场。"
    我 "……这么贵重的东西，万一我弄丢呢。"
    show zhiwei doki at zw_left
    知微 "丢不了。它在我这里存了七年，本来就快生锈了。"
    知微 "……还有。云曦跑的那四千次里，我检查过题目来源。"
    知微 "范围就是这七天的五十六道题。换句话说——见过的每一道题，今晚都不用再怕。"
    $ unlock_scene(6)
    "粉笔安静地躺在台灯下。窗外有风，桌上有光。"
    show yunxi laugh at yx_right
    云曦 "检测到心跳平稳、表情放松——很好。现在执行『回家睡觉』程序，我押送。"
    "走出教室，她忽然把语速放慢了，慢得像一句不想被数据解释的话。"
    云曦 "今晚我不报数了。你睡着之前，我就在这儿亮着。"
    show zhiwei happy at zw_left
    知微 "明天早上，校门口见。……这次换我来接我的社员。"

    menu:
        "今晚的告别方式"

        "跟云曦约好明早的第一条消息":
            $ love_yx += 1
            云曦 "协议达成：明早 6:30，我将发送今日天气、豆浆价格、和一句『加油』。……三句都会写。"
        "把粉笔小心收进笔袋最里层":
            $ love_zw += 1
            知微 "……收好了？"
            "她按了按笔袋的拉链，像在确认一件很重要的事已经放稳。"
            知微 "那就，晚安。"
    return
