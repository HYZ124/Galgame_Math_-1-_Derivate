# ============================================================
# 开局教程（新手引导）：推进/选择/做题/提示/菜单/相册
# 由 script.rpy 的 start 在最开头 `call tutorial from _call_tutorial`。
#
# 演示题存在文件头部的 init 列表 T0 里，走的是和正式题库同一套 do_problem
# 流程，只是带 "demo": True —— 不计分、不进错题本、不计入总题数。
#
# 【加一步热身】① 往 T0 追加一个 dict，字段和正式题一样（id/type/q/opts/ans/
#   hint/why，填空题 ans 写成列表，多种等价写法都列上）；② 中文原文直接改
#   q/hint/why，英文另起 *_en 字段就地写——注意 T0 不在 lessons/l*_en.rpy
#   的合并范围内，q_en 这类字段得自己填，缺了英文模式会显示中文；
#   ③ 在 label tutorial 正文里加一句讲解，然后 call do_problem(T0[n])。
#
# 【和正式题库不一样的一处】math_core.rpy 的 init 20 只轮换 L1~L7 的选项位置，
#   T0 不在名单里。所以这里 mc 题的 ans 下标必须和 opts 顺序手动对上（例如
#   T0-01 的正确答案 "f′(x)" 写在 opts 下标 1，ans 就必须是 1）。
# ============================================================

init python:
    T0 = [
        {"id": "T0-01", "type": "mc", "demo": True,
         "q": "热身一：下面哪个符号，表示函数 f(x) 的导数？",
         "q_en": "Warm-up 1: which symbol stands for the derivative of f(x)?",
         "opts": ["f(x)²", "f′(x)", "Δx", "sin f"],
         "opts_en": ["f(x)²", "f′(x)", "Δx", "sin f"],
         "ans": 1,
         "hint": "导数喜欢在函数头上别一枚小小的“撇”。",
         "hint_en": "A derivative likes to wear a tiny prime mark on its forehead.",
         "why": "f′(x) 就是导数的签名。这一撇，接下来七天会一直跟着你。",
         "why_en": "f′(x) is the signature of a derivative. That little prime stays with you all seven days."},

        {"id": "T0-02", "type": "in", "demo": True,
         "q": "热身二：f(x) = x²，那么 f(3) 等于多少？（这是函数值，不是导数）",
         "q_en": "Warm-up 2: f(x) = x², so what is f(3)? (this is a function value, not a derivative)",
         "ans": ["9", "9.0"],
         "hint": "把 3 代进 x，然后平方。",
         "hint_en": "Put 3 where x is, then square it.",
         "why": "f(3) = 9。代入算的是“等于多少”，求导算的是“变化多快”——先把这两件事分清楚。",
         "why_en": "f(3) = 9. Substitution asks how much it is; differentiation asks how fast it changes. Tell the two apart first."},
    ]

label tutorial:

    scene bg classroom
    show zhiwei normal at zw_teach
    show yunxi happy at yx_hover
    with Dissolve(0.8)

    云曦 "慢着——正式开课之前，有一段雷打不动的「新手引导」。"
    我 "连 AI 都有义务流程？"
    云曦 "文档写明：在玩家第一次说出“啊？这怎么操作”之前，必须完成教学。"
    show zhiwei normal at zw_teach
    知微 "……她的原话是：不教的话，等下有人两次都答错，然后开始怀疑人生。"
    我 "我还没那么脆弱。大概。"

    云曦 "第一课：阅读。点击鼠标、按空格，对话就会前进；按住 Ctrl 可以快进。"
    云曦 "错过的对白想回看？滚动鼠标滚轮可以往回翻；菜单里的「回想记录」能读到全部历史。"
    知微 "这一点也不玄乎：文字游戏，文字先行。"

    云曦 "第二课：选择。剧情走到岔路口时，会出现这样的选项——"

    menu:
        "云曦清了清嗓子，弹出一块大字报：「此处有选项，随便挑」"

        "选左边，观察会发生什么":
            云曦 "记录完毕：玩家偏爱左边。已建档，不解释。"
        "选右边，顺便看看有没有彩蛋":
            云曦 "彩蛋暂时没有，好奇心的档案先建好了。保持——做题也要靠它。"

    show zhiwei serious at zw_teach
    知微 "第三课，也是最重要的一课：做题。随堂练习只有两种题型。"
    知微 "选择题——四个选项，点你认定的那一个；填空题——自己动手写答案。"
    知微 "填空题不要求字迹工整：x^2、1/2、sinx、e^x 这类写法我都认。"
    云曦 "计分广播：第一次答对 +10；看了提示再答对 +7；第二次才答对 +5；两次都错 0 分，进错题本。"
    知微 "提示不是耻辱，是租来的梯子——租金是这道题的三分之一的分数。"

    云曦 "口说无凭。下面两道演示题，不计分、不进错题本，答错也不会被写在黑板上。"
    $ q_round = 1
    call do_problem(prob=T0[0])
    $ q_round = 2
    call do_problem(prob=T0[1])

    show yunxi laugh at yx_hover
    云曦 "看，就是这么回事。实在卡住再点提示，分数打七折，尊严不打折。"
    show zhiwei normal at zw_teach
    知微 "中途想歇：按 Esc（或右键）打开菜单——存档、读档、自动、快进、语言，都在里面。"
    知微 "还有，主菜单挂着一个「回忆相册」。一起走过的画面，会一张一张存进去。"
    云曦 "没解锁的格子会亮着「？？？」——那是留给未来的位置。"

    我 "……好的，我大概明白我来的是个什么社团了。"
    我 "一个把数学课上成游戏的社团。"
    show yunxi determined at yx_hover
    云曦 "新手引导，通关！经验值 +0，自信 +1。"
    show zhiwei happy at zw_teach
    知微 "现在，把“我不会”这三个字——"
    我 "从词典里删掉。对吧，黑板上写着呢。"
    知微 "……学得挺快。上课。"

    return
