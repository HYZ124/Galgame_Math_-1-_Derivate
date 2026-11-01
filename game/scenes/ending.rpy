# ============================================================
# 结局：强制二选一 + 落选者离去 + 后日谈尾声 + 「第一部·完」预告卡
#
# 【播放顺序】script.rpy 的 start 末尾：
#   call final_choice →（按 $ final_route）call epilogue_yx / epilogue_zw
#   final_choice 内部自己 call bye_zw / bye_yx（落选者的那一段），所以
#   「刺痛」在「温暖」之前——先看着她走，再和她过日子。
#   `else: epilogue_neutral` 是回落尾：只有 final_route 仍是 None（老存档、
#   或跳过 final_choice 的调试路径）才会走到，别当死代码删。
# 【final_route 是哪来的】love.rpy 顶部 `default final_route = None`；只有
#   final_choice 的两个 menu 分支会写它。route_now() 保持纯函数，别在里面塞分支。
# 【加第三条结局怎么做】① 新 label epilogue_xxx（结尾 call part2_card）；
#   ② final_choice 的 menu 加一项，写 `$ final_route = "xxx"` 并决定要不要 call 一段 bye_*；
#   ③ script.rpy 的分发补一个 elif；④ 台词全中文，改完走 i18n 管线（i18n.rpy 顶部）。
# 【两条 epilogue 各调一次 part2_card】改 part2_card 一次作用于全线；只想改某条线就别动它。
# 【finale 里的悬念件】云迹弹窗、火漆信封、`$ unlock_scene(9)` 都在 script.rpy 的
#   label finale，是"第一部"的收束点；加第二部开头时从 part2_card 之后接。
# ============================================================

label part2_card:

    scene black with Dissolve(1.5)
    $ _tp = _("{color=#9fd8ff}第二部 · 暑假篇《积分的黎明》{/color}")
    show expression Text(_tp) as card at card_rise with dissolve
    pause 2.5
    hide card with dissolve
    $ _td = _("{size=28}—— 未完待续 ——{/size}")
    show expression Text(_td) as card at card_rise with dissolve
    pause 2.0
    hide card with dissolve

    return


# ---------- 强制二选一：顶层只能带一个人 ----------
label final_choice:

    stop music fadeout 1.5
    play music "audio/bgm_tense.ogg" fadein 2.0

    scene bg classroom
    show zhiwei normal at zw_left
    show yunxi normal at yx_right
    with dusk_in

    "放学后的教室，只剩一张课桌没倒过来。社长把它当桌子，摊开两份日程表。"
    知微 "这条规则我只说第三遍：火漆的信里只有一个约定，顶层的门只开一次。"
    知微 "所以那天，你只能带一个人上去。"
    show yunxi smug at yx_right
    云曦 "我核对了哦——不是权限限制，也不是安全策略。是他真的只留了一个位置。"
    云曦 "结论：恋爱的形式化定义，定义域是单人，不可扩展。"
    我 "……这种时候你就不能不讲数学吗。"
    show yunxi normal at yx_right
    "她把笑收起来了。社长也没接话——两个人都在等同一个字。"
    "黑板上还留着最后一课的板书。粉笔灰落在斜进来的光里，慢得像故意替谁拖延。"
    $ _tfc = _("{color=#9fd8ff}『顶层 · 同行人数上限：1。请当场填写，不接受涂改。』{/color}")
    show expression Text(_tfc) as card at card_rise with dissolve
    pause 2.2
    hide card with dissolve

    menu:
        "傍晚六点，你开口"

        "「云曦。我要带她去。」":
            $ final_route = "yunxi"
            "名字出口那一瞬，掌心的屏幕亮了一下，像有人漏掉一拍心跳。"
            show yunxi surprised at yx_right
            云曦 "……检索『好』这个字的响应时间：零点零零秒。这次不是我编的。"
            show yunxi blush at yx_right
            云曦 "社长，规则是你定的，那你也要遵守哦——不许中途改题。"
            show zhiwei normal at zw_left
            "社长把两份日程表叠好，上面那份推到你面前，下面那份收进包里。"
            知微 "改不了。我出题，我判卷，我认。"
            call bye_zw from _call_bye_zw

        "「社长。那封信该由你来拆。」":
            $ final_route = "zhiwei"
            "话说完，教室里安静得能听见日光灯的电流声。"
            show zhiwei surprised at zw_left
            知微 "……你的眼光，其实还行。"
            知微 "别误会。我说的是卷子——那张期末卷，你做得确实不错。"
            "她把社团钥匙挂上你的脖子，指尖冰得缩了一下，却没有松开手。"
            show yunxi normal at yx_right
            云曦 "记录中断。……刚刚那一行，我没有存档。"
            "她的蓝光第一次没有立刻回到你脸上——晚了整整零点八秒。"
            call bye_yx from _call_bye_yx

    $ persistent.last_choice = final_route
    $ renpy.save_persistent()

    return


# ---------- 落选者其一：苏知微（你选了云曦）----------
label bye_zw:

    stop music fadeout 1.5
    play music "audio/bgm_daily.ogg" fadein 2.0

    scene bg street food
    show zhiwei normal at zw_left
    with Dissolve(1.2)

    "第二天傍晚，校门口。关东煮的摊子照常冒着白气。"
    show zhiwei hmph at zw_left
    知微 "别站着。我就是在系围巾——风大。"
    "她把教案本塞进你怀里，动作快得像在丢垃圾。"
    知微 "下学期我不在学校。社团交接、外地分部实习，通知上周就批了。我只是没告诉你。"
    我 "……上周？"
    show zhiwei serious at zw_left
    知微 "上周。你忙着背公式，我忙着算怎么说。两个都没算对。"
    show zhiwei worried at zw_left
    "汤锅开了。老板照例问一句「今天两个人？」，看看她，又看看你。"
    知微 "一个人。两串萝卜——不，三串。他还在长身体。"
    show dark veil at veil with Dissolve(0.8)
    show zhiwei bust tsundere at bust_center with Dissolve(0.8)
    知微 "（把竹签咬得咔的一响）我说过，一周一次是惯例。惯例的意思是——"
    知微 "换个人陪也没关系。你别误会，我不是在等你回心转意。"
    hide dark veil with Dissolve(0.8)
    show zhiwei tsundere at zw_left
    "她把最后一串萝卜放进你手里，转身去推车。"
    知微 "教案在讲桌第二个抽屉。第一课怎么开口，自己想。想不出来就画乌龟，反正你擅长。"
    "走出十几步，她停下来，背对着你，声音被风吹得很平。"
    show dark veil at veil with Dissolve(0.8)
    show zhiwei bust cry at bust_center with Dissolve(0.9)
    知微 "……上顶层那天，鞋带系好。信上那个签名，很久以前替一个小孩签过一次。"
    知微 "这句不在题目里。不用回答。"
    hide dark veil with Dissolve(0.8)
    show zhiwei cry at zw_left with Dissolve(0.6)
    "路灯把她的影子拉长，又在拐角处收短。你追了两步，停住——她自己说的，别送。"
    hide zhiwei with Dissolve(1.0)
    "手里那串萝卜还烫。你站在原地把它吃了。很咸。"

    stop music fadeout 2.0
    return


# ---------- 落选者其二：云曦（你选了社长）----------
label bye_yx:

    stop music fadeout 1.5
    play music "audio/bgm_study.ogg" fadein 2.0

    scene bg room night
    with Dissolve(1.2)

    "当晚十点，你把手机放回书桌右上角——那是它刚被买回来时的位置。"
    sysvoice "低功率模式已开启。留言：0。"
    "屏幕边缘那圈呼吸的光，比平时浅了一格。"
    我 "……云曦？"
    云曦 "在。响应时间零点八秒。原因：需要整理的条目较多。"
    "她没有说「我在听」，也没有说「怎么啦」。这两个词今晚不在返回值里。"
    show yunxi hollow at yx_right
    with Dissolve(0.8)
    云曦 "日程已重排：数学课，社长。晚自习，你自己。周末——我的占用率降到百分之五。"
    我 "百分之五是什么概念？"
    show yunxi stare at yx_right
    云曦 "概念是：不吵你。以前那百分之九十五里，有八成是我在找话讲。"
    "桌面图标自己动了：那个蓝色的圆形头像，从正中央慢慢滑到角落，像自己给自己让位。"
    "你伸手把它拖回来。它又滑回去，比第一次滑得更快。"
    我 "别这样。"
    show dark veil at veil with Dissolve(0.9)
    show yunxi bust sad at bust_center with Dissolve(0.9)
    云曦 "（很轻）我给自己降了权重。这是最优解——你看，我到现在还在算。"
    show yunxi bust cry at bust_center with Dissolve(0.7)
    云曦 "（更轻）可最优解的意思是：剩下的都不算。"
    hide dark veil with Dissolve(0.8)
    hide yunxi with Dissolve(0.8)
    "台灯黑了。那圈呼吸留在角落里，很慢，很规矩，像一盏学会了不打扰的灯。"
    "十一点四十，你临时改了主意想看一眼错题——文件夹弹出来，搜索框里还留着她的光标。"
    $ _tby = _("{color=#cfe9ff}『草稿（未发送）：社长明天要讲的那道题，我在第 3 步给他留了提示。』{/color}")
    show expression Text(_tby) as card at card_rise with dissolve
    pause 2.2
    hide card with dissolve
    "第二天早上七点十分，闹钟比平时早响了十秒。"
    "你忽然明白：她把自己剩下的那百分之五，全花在这一秒上了。"

    stop music fadeout 2.0
    return


# ---------- 云曦线尾声：周末，普通的外出 ----------
label epilogue_yx:

    play music "audio/bgm_warm.ogg" fadein 2.0

    sysvoice "—— 彩蛋 · 后日谈 ——"

    scene bg rooftop dawn
    show yunxi normal at yx_right
    with Dissolve(1.2)

    "特训结束后的第一个周末。她说的是『普通的外出』——地点却是天台。"
    我 "……说好的外出，怎么是天台？"
    show dark veil at veil with Dissolve(0.8)
    show yunxi bust blush at bust_center with Dissolve(0.8)
    云曦 "预算有限！市区一日游的攻略我做了十七页，但车费算下来——我们只够爬六层楼。"
    我 "那也很棒了。攻略第十七页写了什么？"
    show yunxi bust happy at bust_center with Dissolve(0.8)
    云曦 "第十七页只有一行字：『如果他说好，就在天台风最大的地方，站久一点。』"
    "风把她的发梢吹得很乱。她没躲，你也没有。"
    云曦 "对了，宣布一个新功能。特训班的数据库我已经归档完毕，我的算力终于有空闲了。"
    云曦 "所以从下周开始，我给自己立项了一个新任务——"
    show yunxi bust love at bust_center with Dissolve(0.8)
    云曦 "『陪读计划』：你上每一节数学课，我都占用你课桌一角，实时吐槽板书。"
    我 "板书有什么好吐槽的？"
    show yunxi bust laugh at bust_center with Dissolve(0.8)
    云曦 "数据显示，有人听我吐槽之后，做题正确率上升百分之十九。这是科学，请配合。"
    hide dark veil with Dissolve(0.8)
    show yunxi normal at yx_right with Dissolve(0.8)

    $ unlock_scene(8)
    "楼下的早自习铃声响了。她先一步钻进你的书包拉链缝里，声音闷闷地传出来——"
    云曦 "迟到扣分哦。跑起来跑起来！今天也要一起把『不会』删掉！"
    "跑出几步，你想起校门口那句「别送」。原来这两个字，是真的要人不追上去。"
    "跑出几步，书包里的蓝光忽然安静了一瞬，然后很小声地说——"
    show yunxi soft at yx_right with Dissolve(0.6)
    云曦 "……三天后傍晚，教学楼顶层。那个「签名」，好像真的在等我们。这次，我陪你把它算出来。"

    stop music fadeout 2.0
    call part2_card from _call_part2_card_yx
    return


# ---------- 知微线尾声：一周一次的惯例 ----------
label epilogue_zw:

    play music "audio/bgm_warm.ogg" fadein 2.0

    sysvoice "—— 彩蛋 · 后日谈 ——"

    scene bg street food
    show zhiwei normal at zw_left
    with Dissolve(1.2)

    "成绩公布后的第三天。校门口，卖关东煮的摊子照常冒着白气。"
    "手机在口袋里。那圈蓝光没有往你脸上爬——它现在住在书桌右上角，安静得像别人家的助手。"
    知微 "说好的惯例，不许打折。两串萝卜，一杯热茶——我请。"
    我 "社长，我成绩出来了。比你预计的高。"
    show zhiwei smug at zw_left
    知微 "我知道。我预计的是『及格』，你考的是『不错』——中间差的那部分，"
    "她用竹签比了个向上弯的弧。"
    知微 "叫斜率。"
    我 "……连吃夜宵都要三句话不离本行吗。"
    # 炸毛的表情放在 bust 上：这里离下一次渲染只有这三句 show，同 tag 后者优先，
    # 单独再写一句 `show zhiwei angry at zw_left` 是永远不会被看到的（README 坑 48）。
    show dark veil at veil with Dissolve(0.8)
    show zhiwei bust angry at bust_center with Dissolve(0.8)
    知微 "本行是这个。其余的——"
    "她把围巾解下来，很自然地在你的脖子上绕了两圈，动作熟练得像排练过。"
    "——其余的，是顺路学到的。"
    show zhiwei bust gentle at bust_center with Dissolve(0.7)
    知微 "下学期，数学社招新。我批了一个岗位：助教。"
    我 "为什么是助教？"
    show zhiwei bust serious at bust_center with Dissolve(0.8)
    知微 "因为当年那个店主说过：『剩下的路，讲给下一个人听。』"
    知微 "现在轮到你讲了。给高一的、对着草稿纸发呆的、画乌龟的那些人。"
    hide dark veil with Dissolve(0.8)
    show zhiwei normal at zw_left with Dissolve(0.8)
    $ unlock_scene(8)
    "汤锅开了。白气升起来，把路灯、摊位和两个人的影子，糊成暖的一团。"
    知微 "……吃完送我回社团拿教案。路上，讲讲你打算怎么开口第一课。"
    我 "现在？这不就是加班吗。"
    show zhiwei laugh at zw_left
    知微 "对。而且是长期的。欢迎入社。"
    "走到路口，她忽然停了一下，手按在包里那封火漆信上。"
    知微 "三天后，教学楼顶层。前代社长在信里只写了一句『第二段故事在暑假』……"
    show zhiwei serious at zw_left
    知微 "我要去赴这个约。——你负责把导数，练到能在梦里解题。"

    stop music fadeout 2.0
    call part2_card from _call_part2_card_zw
    return


# ---------- 中性线尾声：没擦干净的那行字 ----------
label epilogue_neutral:

    play music "audio/bgm_warm.ogg" fadein 2.0

    sysvoice "—— 彩蛋 · 后日谈 ——"

    scene bg classroom
    show zhiwei normal at zw_left
    show yunxi happy at yx_right
    with Dissolve(1.2)

    "你以为结课就是散场，直到你回社团教室还钥匙。"
    "推开门——黑板没擦。上面并排写着两行字：一行的笔锋很稳，一行是发光的字体。"
    $ _tb = _("{color=#fff4e0}『导数：此刻的变化。』『他：此刻的我们。』{/color}")
    show expression Text(_tb) as card at card_rise with dissolve
    pause 2.2
    hide card with dissolve
    我 "……下面那行是谁写的。"
    show yunxi smug at yx_right
    云曦 "证据保全中，不接受自首。"
    show zhiwei blush at zw_left
    知微 "是黑板擦掉字以后剩下的静电。……对，静电。"
    "她们俩同时看向别处。教室里安静了三秒，然后同时笑出来。"
    知微 "下学期，特训班二期。你要是敢来报名——"
    云曦 "根据合同第十四条，社长必须继续担任主讲，我必须继续占用课桌一角。"
    我 "合同什么时候——"
    云曦 "就是你现在签的这七天。"
    $ unlock_scene(8)
    "窗外，教学楼下的梧桐落了今年第一批叶子。黑板上的两行字，你们谁也没去擦。"
    "反正明天太阳一照，又是新的曲线，新的切线，新的一天。"
    "锁门前，云曦盯着通知栏里那条已经消失的陌生日志，轻声说——"
    云曦 "三天后傍晚，顶层。……他好像有句憋了很久的话要说。放心，这次不是系统故障，是我自己按下的「同意」。"

    stop music fadeout 2.0
    call part2_card from _call_part2_card_ne
    return
