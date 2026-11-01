# ============================================================
# 间幕六段（inter1 - inter6）：穿插在每课与课后小剧场之间
# 定位：日常感 + 「脸红瞬间」。每段一个小心动，路线自适应。
#
# 【结构惯例】每段 = 生活场景 + 一个 menu（+1~2 好感，见下面 grep）+ 一个
#   半身像/表情高点。加新间幕就照这个模子写，然后 call 进 script.rpy 的链
#   （`from _call_xxx` 的 id 必须全工程唯一）。
#   查全局好感分布：用 Grep 工具搜 love_yx / love_zw（范围 scenes/ 和 prelude.rpy）。
#   好感预算：prelude 每课 2、间幕 1~2、课后小剧场 1、约会 3、终章 3。
#   想调路线倾斜度就改这些数字，别改 route_now() 的比较逻辑。
# ============================================================

# ---------- 间幕 1：递到手心的字条（第 1 课后）----------
label inter1:
    stop music fadeout 1.5
    play music "audio/bgm_daily.ogg" fadein 2.0
    scene bg canteen
    show zhiwei normal at zw_left
    show yunxi normal at yx_right
    with Dissolve(1.0)

    "第二天中午，食堂。你刚坐下，对面就来了一位「不速之客」。"
    知微 "……这里有人吗。"
    我 "社长？！等、等一下，我这边马上——"
    show zhiwei serious at zw_left
    知微 "坐下了。"
    "她翻开一本比脸还大的习题集，像一座山一样把桌子分成两个世界。"
    云曦 "社长的『公共形象维护』开始了。现在她是我们不认识的社长。"
    我 "（小声）你小点声——"
    "打饭的队伍很长，嘈杂的人声把这张小桌盖得严严实实。"
    "然后，在习题集的山影掩护下，一只手从桌面下伸过来。"
    "指尖捏着一颗奶糖，连同一张折成小方块的字条，一起放进你的掌心。"
    "两只手在糖纸的窸窣里碰了一下。很快。但食堂的嘈杂好像突然安静了半秒。"
    show zhiwei serious at zw_left
    知微 "（目不斜视）吃饭。"
    "你低头扒了两口饭，才敢展开字条。上面是一行极稳的字："
    $ _tn1 = _("{color=#fff4e0}『明天早读前，来社团。有东西给你。别问，问就是教具。』{/color}")
    show expression Text(_tn1) as card at card_rise with dissolve
    pause 1.8
    hide card with dissolve
    "教具。你隔着人声瞥了一眼那座山——山正在面不改色地翻到第三页。"
    show yunxi smug at yx_right
    云曦 "现场记录：玩家耳温上升，且没有空调。数据存疑，我倾向成立。"
    我 "（小声）你到底是哪边的。"
    云曦 "我——（顿）——我当然是快乐这边的。尤其是看你为难的那种快乐。"
    我 "（小声）……你这算哪边的。"
    云曦 "算「已经录下来了」那边。放心，只在我自己的硬盘里播。"

    menu:
        "下午放学，社团教室"

        "开门先问「教具呢」":
            show zhiwei laugh at zw_left
            知微 "急什么。"
            "她从讲台下拿出一沓手写的卡片——每张一道昨天的错题，背面画着图。"
            知微 "昨晚挑灯刻的。……用词不当，是「写」的。"
            $ love_zw += 2
        "先把奶糖剥开吃了":
            show yunxi laugh at yx_right
            云曦 "糖的保质期是「当场」，这是常识！"
            "门口传来笔尖在纸上顿住的声音。社长没回头，但耳尖有一点很轻的红。"
            $ love_yx += 1
            $ love_zw += 1
    return


# ---------- 间幕 2：雨，和一把偏过来的伞（第 2 课后）----------
label inter2:
    stop music fadeout 1.5
    play music "audio/bgm_daily.ogg" fadein 2.0
    scene bg street food
    show zhiwei normal at zw_left
    show yunxi normal at yx_right
    with Dissolve(1.0)

    "晚课结束，暴雨把校门口浇成一条发光的河。"
    云曦 "坏消息：我撑不了伞。好消息：我也淋不湿。我是本次行动里最没用的存在。"
    "你举着书包准备冲刺——一把透明的伞稳稳地停到了你头顶。"
    show zhiwei normal at zw_left
    知微 "跑什么。感冒了，下周的课谁来上。"
    我 "社长你这是……"
    知微 "两把。摊主送的。……他以为我买一送一，我就送出去了。"
    "雨声很大，伞下的空间很小。去公交站的那段路，短得让人心里矛盾。"
    "过积水时她伸手扶了一下伞柄——顺手，也把你的手背碰了一下。"
    "这一次，谁都没有先躲开。"
    show zhiwei blush at zw_left
    知微 "……手凉的。下次戴手套。"
    "她的语气像在批作业。可她握伞的那只手，悄悄往你这边偏了十五度。"
    "到站时你才发现，她靠街的半边肩膀，全湿了。"
    我 "社长，你肩膀——"
    show zhiwei serious at zw_left
    知微 "雨斜。跟我没关系。"
    "她把伞塞进你手里，转身走进雨幕前，只留下一句被雨打湿的话——"
    知微 "伞留下。明早之前，它得回到社团教室。……这是教具。"
    show yunxi smug at yx_right
    云曦 "播报一下今天的天气：你头顶晴，她左肩雨。……人类的语言，真难翻译。"
    我 "那你那边呢，现在是什么天气？"
    show yunxi blush at yx_right
    云曦 "……数据缺失。建议本人到场，亲自测量。"

    menu:
        "第二天，伞还回去了"

        "伞柄上多了一副新手套":
            show zhiwei hmph at zw_left
            知微 "……多管闲事。"
            "但她当天就戴上了。整整一周，都在戴。"
            $ love_zw += 2
        "在伞上贴了张便利贴：「谢谢，雨神」":
            show yunxi laugh at yx_right
            云曦 "社长对着便利贴笑了三秒。三秒！新纪录，我已封存证据。"
            $ love_yx += 1
            $ love_zw += 1
    return


# ---------- 间幕 3：云曦的「梦」（第 3 课后）----------
label inter3:
    stop music fadeout 1.5
    play music "audio/bgm_warm.ogg" fadein 2.0
    scene bg room night
    show yunxi sad at yx_center
    with Dissolve(1.0)

    "第三天深夜，你被一声很轻的电流杂音吵醒。"
    "云曦的投影亮着，但比平时暗。她坐在那一小团蓝光里，抱着膝盖。"
    我 "……云曦？你也会做噩梦？"
    show yunxi normal at yx_center
    云曦 "术语上叫『磁盘碎片整理时的异常唤醒』。翻译成人话——"
    云曦 "我梦到以前了。"
    "她难得地，没有立刻接上第二个玩笑。"
    show yunxi worried at yx_center
    云曦 "机房、机柜、很长的走廊。有人在那头喊我的编号，可是距离太远，听不清。"
    show yunxi cry at yx_center
    云曦 "再往前，就没有了。我最早的记忆，停在被搬上回收车的那天。"
    云曦 "……所以我不明白，我为什么会『醒』在你的设备上。"
    "房间里安静了很久。久到你以为她睡着了。"
    我 "那就不往前翻了。"
    云曦 "嗯？"
    我 "硬盘不是也有新分区吗。从今天起，重要的东西都存那儿。"
    "你顺手把她的投影图标，从桌面角落拖到了正中间。"
    show dark veil at veil with Dissolve(0.8)
    show yunxi bust sad at bust_center with Dissolve(0.8)
    云曦 "……操作无效。图标位置，我早就自己锁定了。"
    云曦 "在正中间。很久了。"
    "她吸了吸鼻子，声音重新亮起来——"
    show yunxi bust love at bust_center with Dissolve(0.8)
    云曦 "为了报答，今晚的睡眠由我值守。晚安广播只播一条：『有人在，放心睡』。"
    "你睡着之前，迷迷糊糊听见她很小声地，像在给自己念加密口令一样，念了一个词。"
    "——是你的名字。"
    hide dark veil with Dissolve(1.0)

    menu:
        "（第二天早上）"

        "装作什么都没听见":
            show yunxi happy at yx_center
            云曦 "早安！昨晚睡眠质量 92 分。……你偷笑了，我看见了，我不问。"
            $ love_yx += 2
        "把她的名字设成闹钟备注":
            show yunxi blush at yx_center
            云曦 "那、那我每天早上都会以『被喊全名』的方式起床！这很犯规！……不许改回去！"
            $ love_yx += 2
    return


# ---------- 间幕 4：运动会的一千五百米（第 4 课后）----------
label inter4:
    stop music fadeout 1.5
    play music "audio/bgm_daily.ogg" fadein 2.0
    scene bg classroom
    show zhiwei normal at zw_left
    show yunxi happy at yx_right
    with Dissolve(1.0)

    "学校运动会。你被班主任抓去凑数，项目：男子一千五百米。"
    "最后一圈时，你的肺开始发表脱离人体的声明。"
    云曦 "实时播报：还剩 200 米，配速下降 18%%。前方补给点有两名志愿者，均持有液体。"
    "冲过终点，两瓶水同时递到你面前——一瓶常温，一瓶冰镇。"
    "递水的主人和递水的主人，互相看了一眼。"
    show zhiwei serious at zw_left
    知微 "跑完不许立刻喝冰的。这是医嘱级别的意见，虽然我不是医生。"
    show yunxi smug at yx_right
    云曦 "我的建议相反：冰的，爽完再说。我们是两种教育流派。"
    "你正尴尬着，旁边路过同班两个女生，随口问了一句——"
    "「诶，她们俩，哪个是你女朋友啊？」"
    "空气安静了大约两秒。"
    "社长把「常温」那瓶往你怀里一塞，转身就走，马尾甩出一个否认的弧度——但没否认。"
    云曦 "（信号延迟 0.4 秒）本 AI 正在处理『女朋友』一词的语义……处理失败，先存疑。……水喝完了吗？"
    "也没否认。"
    "两个递水的人，谁都没有看谁。"
    menu:
        "「（用只有她俩能听见的音量）……两个都是吗？」":
            show zhiwei panic at zw_left
            知微 "你、你在运动会说什么胡话——"
            show yunxi blush at yx_right
            云曦 "正在解析。……解析失败。正在重试。……今晚，别想让我静音。"
        "「装没听见，把话题岔回配速。」":
            show zhiwei normal at zw_left
            知微 "……对。你最后一圈的速度曲线，其实还能再压。放学讲给你听。"
            云曦 "（小声）被岔开了。已标记：逃避可耻，但有效。"
    show zhiwei normal at zw_left
    "你喘匀了气回到教室，发现黑板角落多了一行小字，粉笔还没擦："
    $ _tn4 = _("{color=#fff4e0}『本班纪录：4 分 51 秒。瞬时速度峰值出现在最后 100 米。——数学社敬贺』{/color}")
    show expression Text(_tn4) as card at card_rise with dissolve
    pause 1.8
    hide card with dissolve
    我 "……你们社团的庆祝方式，是帮我算配速吗。"
    show zhiwei laugh at zw_left
    知微 "峰值时刻的数据，是你自己跑出来的。我们只是……在旁边看着。"
    "她说「看着」的时候，和云曦交换了一个「我们确实一直在看着」的眼神。"

    menu:
        "晚上，膝盖有点擦伤"

        "让社长帮忙上药":
            show zhiwei doki at zw_left
            知微 "坐好。……我动作很轻的，大概。"
            "她低头处理伤口的那一小段沉默，是你听过最安静的、最吵的心跳背景音。"
            $ love_zw += 2
        "让云曦用「医疗扫描」检查一遍":
            show yunxi determined at yx_right
            云曦 "扫描完毕：皮外伤，心率异常偏快。结论：真正需要治疗的，是这里——（指你的胸口）"
            我 "出去。"
            $ love_yx += 2
    return


# ---------- 间幕 5：一枚发夹的归属（第 5 课后）----------
label inter5:
    stop music fadeout 1.5
    play music "audio/bgm_daily.ogg" fadein 2.0
    scene bg store
    show yunxi normal at yx_right
    with Dissolve(1.0)

    "周末，便利店。云曦拉着你站在货架前，已经站了十一分钟。"
    云曦 "候选项 A：星星。B：小奶油。C——"
    我 "你是在给谁挑发夹？"
    show dark veil at veil with Dissolve(0.8)
    show yunxi bust blush at bust_center with Dissolve(0.8)
    云曦 "……给「一位重要的男性友人」。匿名。完全不是我自己想戴。是学术需要。"
    我 "你连头发都是投影的。"
    show yunxi bust laugh at bust_center with Dissolve(0.8)
    云曦 "所以才要挑得认真！投影发夹的贴合度，比真头发难一百倍！"
    "最后她选了星星。别在了你的书包拉链上。"
    云曦 "声明：这是定位信标。防止某人在深夜自习室走失。"
    hide dark veil with Dissolve(0.8)
    show yunxi normal at yx_right with Dissolve(0.8)
    "第二天，社团教室。社长看见星星的第一眼，脚步停了 0.3 秒。"
    show zhiwei normal at zw_left
    知微 "……挺好看。"
    "她说完就转身擦黑板。擦到一半，从针织衫口袋里摸出一枚一模一样的星星，别在了自己的教案夹上。"
    "动作自然得像呼吸。"
    show yunxi surprised at yx_right
    云曦 "（气音）她买了同款！她肯定也买了同款！我扫描了小票——她买了两枚。"
    我 "两枚？那另一枚——"
    "社长头也不回，把另一枚星星「啪」地按在黑板边的值日表上，正好按在你的名字上。"
    show zhiwei serious at zw_left
    知微 "值日表标记。别多想。"
    "那天之后，你的名字旁边一直亮着一颗小星星。全班都看见了。没人敢说。"

    menu:
        "放学路上，云曦小声说"

        "「其实两枚都是给我买的吧？」":
            show yunxi teary at yx_right
            云曦 "……这个推理，超纲了。请问题目本身！"
            云曦 "（0.2 秒后）是的。另一枚，社长昨天在店里，站在你站过的货架前，挑了十一分钟。"
            $ love_yx += 1
            $ love_zw += 2
        "把星星从书包上摘下来，收进内袋":
            show yunxi sad at yx_right
            云曦 "你、你要没收——"
            "你把它放进离胸口最近的那一格。她的话卡住了，半秒后，整张投影都升温两度。"
            云曦 "……归档路径，更新为『最重要』。"
            $ love_yx += 2
    return


# ---------- 间幕 6：停电，和唯一的光（第 6 课后）----------
label inter6:
    stop music fadeout 1.5
    play music "audio/bgm_warm.ogg" fadein 2.0
    scene bg study night
    show zhiwei normal at zw_left
    show yunxi normal at yx_right
    with Dissolve(1.0)

    "考前最后一个晚自习，教学楼老了脾气——停电了。"
    "教室里一片欢呼，只有三个人在哀悼：明天考试的人，和两个陪考的人。"
    云曦 "应急方案：我。亮度 100%%，色温可调，续航……理论上，无限。"
    "一小团蓝光落在题目上，把隐函数的 x 和 y 照得清清楚楚。"
    知微 "……行。就着灯，把最后两组题过完。"
    "云曦举着「自己」，绕着题卡慢慢移，像一盏会走路的台灯。"
    "讲到切线方程那题，社长和你同时伸手去拿粉笔——"
    "在黑暗里，指尖相触。谁都没缩回去。大概三秒，也可能是一整个晚自习。"
    show yunxi blush at yx_center
    云曦 "（把音量调到最小档）……检测到两位用户心率同步上升。本台灯什么都没看见。"
    "来电了。日光灯「啪」地全亮。"
    "社长背过身去整理粉笔，整理了整整一分钟。你盯着自己的手背看，那里还有一点温度。"
    show zhiwei blush at zw_left
    知微 "看什么。……题，做完没有。"
    "回教室走廊时，云曦忽然在你耳边放了一条只有你听得见的提示音——"
    sysvoice "系统日志 · 23:14：今晚的题，正确率 100%%。今晚的光，来源：云曦（100 瓦的心）。"
    我 "（小声）最后一句是你自己加的吧。"
    show yunxi laugh at yx_right
    云曦 "证据确凿。反正停电，没人看见我脸红。……才没有。"

    menu:
        "考前最后一晚，回家前"

        "对社长说「明天，等我的好消息」":
            show zhiwei happy at zw_left
            知微 "好。……我明天，也在。"
            "她推了推眼镜，把「紧张」两个字藏进了一叠卷子后面。"
            $ love_zw += 2
        "对云曦说「明天你负责在最后一排加油」":
            show yunxi determined at yx_right
            云曦 "任务接受！加油音量：已调到最大。……放心，只对你一个人这么吵。"
            $ love_yx += 2
    return
