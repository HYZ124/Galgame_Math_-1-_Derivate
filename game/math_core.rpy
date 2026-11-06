# ============================================================
# 《导数物语》数学判题引擎
# 题型：mc = 选择题（opts + ans 下标），in = 填空题（ans 接受列表）
#
# 【本文件负责什么】做题界面（mc_screen / in_screen）、判题（norm_ans →
# try_eval → check_answer）、计分（do_problem）、批次循环（practice）、
# 错题本（wrong_* / screen notebook / drill_wrong / review_wrong），
# 黑板开关（show_board/hide_board），以及两段 init 数据加工。
#
# 【i18n 注意】本文件里有几处"前缀 + 运行时才算出来的值"（正确答案：/解析：/提示：）。
#   必须写成 `_tl(_("正确答案：")) + 值`（_tl 在 defines.rpy）。直接
#   `_("正确答案：") + 值` 会让英文模式漏出中文——_() 只登记不翻译，查表发生在
#   Text 显示整串时（README 坑 34）。改完中文串要重跑 i18n 管线。
#
# 【init 顺序，别搞反】
#   init 10：把题库里所有 q/hint/why/opts 的 [ ] 转成全角（_mb_esc），并把
#            lessons/l*_en.rpy 的英文条目按 id 合并成 q_en/hint_en/why_en/opts_en。
#   init 20：选择题正确项轮换。题库里正确项一律写在下标 0（A），这里按 B→C→D→A
#            的固定节奏把正确项挪到别的位置，中英文选项用同一置换保持一致。
#   → 所以：**新题只写题面，正确答案永远放 A**，位置由引擎管，别手改分布。
#
# 【加一种题型】① 在 lessons 里给题加 "type": "你的类型"；② 在 do_problem 里加
#   分支 call 一个新屏幕，屏幕用 `Return(值)` 交回答案；③ 判题走 check_answer
#   （它同时吃 "1/2"、"0.5"、"x^2"、"2x" 这类写法，数值答案按 1e-9 容差比较）。
#
# 【计分规则】首次作答且未看提示 +10；看提示后一次答对 +7；其他情况 +5。
#   演示题（tutorial 里的 T0）带 "demo": True，不计分、不进错题本。
#   ⚠这套规则只在 scenes/tutorial.rpy 讲一次，做题界面**不复述**：按钮就叫「提 示」，
#   不写"得分打七折"；「支持写法」那行也只在第一道填空题挂出来（fmt_hint_seen）。
#   原则=一屏最多一条常驻提示，多余的解释交给教程和答错时的 sysvoice。
#   答对时题面上方飘一次「+N」（tag=pts，动效是 defines.rpy 的 score_pop）。这里
#   故意不 pause：show 语句不阻塞，动效在「回答正确！」和 react() 期间自己走完。
#
# 【错题本】两次都错的题 id 进 wrong_list（本局）+ persistent.wrong_ids（跨周目）。
#   - 浏览界面 screen notebook(mode=...)。两种 mode 的差别只在**能不能操作**：
#       mode="menu" → 主菜单/游戏菜单用 ShowMenu("notebook", mode="menu") 打开，
#                     只能看解析，底栏只有「关闭」= Return()。
#                     （ShowMenu 打开的屏幕里 Return() 就是"退出这个菜单"，语义正确；
#                      必须 Hide() 的是用 Show() 叠上去的层，见 README 坑 26。）
#                     菜单上下文里也没法 call drill_wrong，所以重做按钮不给它。
#       mode="game" → 课内 `call screen notebook(mode="game")`，从 _return 读按钮值：
#                     ""=合上 / "drill"=重做全部 / "L3-24"=只重做这题 /
#                     "skip:L3-24"=看懂了就划掉（只有这条会写 wrong_ids）。
#                     ⚠别把「合上」写成 Return(None)：引擎会给 _return 塞 True 而不是
#                     None（Return 的 None 是"结束交互"哨兵），str 方法会 AttributeError。
#   - notebook 是模态屏 + ShowMenu 打开，所以自己画全屏底色；mode="menu" 不透明、
#     mode="game" 半透明（要透出教室）。列表用 viewport + ysize，别写 yfill（坑 27）。
#   - 重做走 label drill_wrong(pid=None)：drill_mode=True 时 do_problem 不计分、
#     不计 total_questions，答对才 wrong_clear() 划掉，答错继续留本（不会重复塞）。
#   - 每课收尾调 label review_wrong（wrong_list 为空时它自己直接 return，不打扰）。
#   - 题目回查全靠 ALL_PROBS（init 30 把 L1..L7 摊平成 id→题目），旧存档里已删除的
#     题号会被 .get() 跳过，不会崩——改题库 id 时不用迁移存档。
#   - 想加「一键清空」之类的按钮别用 Function()+restart_interaction（call screen
#     的交互会被打断，_return 拿不到值）；正常路径下划掉错题只有一条路：真的重做对。
# ============================================================

default user_answer = ""
default q_prob = {}
default q_round = 0
default hint_used = False
default board_img = None
# 填空题「支持写法」那行只在第一道题出现，所以要有个地方记着"已经给过了"。
default fmt_hint_seen = False

# 全局成绩
default score = 0
default total_questions = 0
default first_try_correct = 0
default wrong_list = []
# True = 正在重做错题（不计分、不计数，答对才划掉）
default drill_mode = False

init python:
    import re

    # 把玩家输入归一化成能比对的样子：全角符号→半角、²³⁴→^2/^3/^4、去掉乘号和
    # 多余括号、脱掉 "y'=" / "答案=" 这类前缀、sin(x)→sinx。
    # 以后凡是"我明明答对了却判错"的反馈，第一个来看这个函数。
    def norm_ans(s):
        s = str(s).lower().strip()
        s = s.replace("＋", "+").replace("－", "-").replace("＝", "=")
        s = s.replace("（", "(").replace("）", ")")
        s = s.replace("×", "*").replace("·", "*").replace("＊", "*").replace("÷", "/")
        s = s.replace("²", "^2").replace("³", "^3").replace("⁴", "^4")
        s = s.replace("**", "^")
        s = re.sub(r"\s+", "", s)
        s = re.sub(r"^(y'|f'\(x\)|y|dy/dx|导数|答案)[:=]", "", s)
        for _ in range(3):
            s = re.sub(r"(sin|cos|tan|ln|log|exp|arctan|arcsin|arccos)\(([^()]+)\)", r"\1\2", s)
        s = s.replace("*", "")
        s = re.sub(r"\(([^()+\-*/^]+)\)", r"\1", s)
        while len(s) > 1 and s[0] == "(" and s[-1] == ")":
            depth = 0
            wrapped = True
            for i, ch in enumerate(s):
                if ch == "(":
                    depth += 1
                elif ch == ")":
                    depth -= 1
                    if depth == 0 and i < len(s) - 1:
                        wrapped = False
                        break
            if wrapped:
                s = s[1:-1]
            else:
                break
        return s

    # 数值等价判定：先 fullmatch 白名单（只允许数字和 + - * / ( )），过了才 eval。
    # 这层白名单是安全边界——输入框里的东西是玩家任意文本，别放宽成允许字母。
    def try_eval(s):
        s2 = s.replace("^", "**")
        if re.fullmatch(r"[0-9+\-*/().]+", s2):
            try:
                return float(eval(s2))
            except Exception:
                return None
        return None

    # 判对 = 归一化后字符串完全相同，或两边都能算成数值且差 < 1e-9。
    # 所以填空题的 ans 写成列表，把常见等价写法（"1/2"、"0.5"、"2^-1"）都塞进去。
    def check_answer(user, accepted):
        u = norm_ans(user)
        if not u:
            return False
        un = try_eval(u)
        for a in accepted:
            na = norm_ans(a)
            if u == na:
                return True
            if un is not None:
                an = try_eval(na)
                if an is not None and abs(un - an) < 1e-9:
                    return True
        return False

    # 中英切换：题库数据是 python dict，不能走 strings 翻译表，
    # 显示时按当前语言取 *_en 字段（在 init 10 由题库英文文件合并进来）。
    # _is_en() 定义在 defines.rpy（strings 表按文件作用域）。
    def q_field(prob, key):
        if _is_en():
            v = prob.get(key + "_en")
            if v:
                return v
        return prob[key]

    # 答对/答错的随机反馈池（react 从这里抽一条）。这里的 _() 串会进翻译表，
    # 增删句子必须重跑 i18n 管线，否则英文模式下直接显示中文。
    def _ok_lines():
        return [
            ("zw", _("很好，这一步很干净。")),
            ("zw", _("看，导数其实就是这么回事。")),
            ("zw", _("嗯，有进步。保持这个手感。")),
            ("zw", _("这题的解法，比我当年考场上写得还利落。")),
            ("yx", _("检测到正确率飙升！玩家状态：开挂边缘。")),
            ("yx", _("哇，你刚才零点几秒就答完了，我都没看清。")),
            ("yx", _("这笔，划给满分。")),
        ]

    def _bad_lines():
        return [
            ("zw", _("别慌，这个错很典型，我们拆开看。")),
            ("zw", _("错不可怕，可怕的是错得不知所以。看解析。")),
            ("zw", _("这题我见过一百个学生错。你是第一百零一个——但会是最后一个。")),
            ("yx", _("错误数据已归档。放心，我给它起了个名字叫'成长'。")),
            ("yx", _("没关系，我的情绪支持模块为你全功率运转。")),
        ]

    def react(kind):
        who, line = renpy.random.choice(_ok_lines() if kind == "ok" else _bad_lines())
        if who == "zw":
            renpy.say(知微, line)
        else:
            renpy.say(云曦, line)

# 题库文本里出现 "[...]" 会被当作 Text 插值表达式求值（例如
# "[f(x₂) − f(x₁)] ÷ (x₂ − x₁)" 会抛 SyntaxError），统一转义为字面量。
init 10 python:
    def _mb_esc(s):
        # 运行时 Text 不认 "\["，只有 .rpy 源字符串解析器认；
        # 数据是运行时拼的，所以直接用全角括号，彻底避开插值。
        return str(s).replace("[", "［").replace("]", "］")

    for _bank in (L1, L2, L3, L4, L5, L6, L7):
        for _prob in _bank:
            for _key in ("q", "hint", "why"):
                if _prob.get(_key):
                    _prob[_key] = _mb_esc(_prob[_key])
            if _prob.get("opts"):
                _prob["opts"] = [_mb_esc(o) for o in _prob["opts"]]

    # 合并英文题库（lessons/l*_en.rpy 里的 L*_EN 列表）
    for _bn, _bank in (("L1", L1), ("L2", L2), ("L3", L3), ("L4", L4), ("L5", L5), ("L6", L6), ("L7", L7)):
        _enbank = globals().get(_bn + "_EN", [])
        _enmap = dict((_ep["id"], _ep) for _ep in _enbank) if _enbank else {}
        for _prob in _bank:
            _e = _enmap.get(_prob["id"])
            if not _e:
                continue
            for _k in ("q", "hint", "why"):
                if _e.get(_k):
                    _prob[_k + "_en"] = _mb_esc(_e[_k])
            if _e.get("opts"):
                _prob["opts_en"] = [_mb_esc(o) for o in _e["opts"]]

# 题库里所有选择题的正确项都写在下标 0（A）。加载时按固定节奏
# B→C→D→A 轮换正确项位置，中英文选项用同一置换保持答案一致。
init 20 python:
    _pos_cycle = (1, 2, 3, 0)
    _ci = 0
    for _bank in (L1, L2, L3, L4, L5, L6, L7):
        for _prob in _bank:
            if _prob.get("type") == "mc" and _prob.get("opts"):
                _a = _prob["ans"]
                _np = _pos_cycle[_ci % 4]
                _ci += 1
                if _np != _a:
                    for _key in ("opts", "opts_en"):
                        _o = _prob.get(_key)
                        if _o and len(_o) > _np:
                            _o[_a], _o[_np] = _o[_np], _o[_a]
                    _prob["ans"] = _np

# ------------------------------------------------------------
# 错题本：id → 题目 反查表 + 增删工具
# init 30 排在题库加工（init 10/20）之后，所以这里拿到的就是最终数据：
# 全角转义过、英文字段合并过、正确项也轮换过了。
# ------------------------------------------------------------
init 30 python:
    # ⚠循环临时变量**绝不能**叫 `_p`：那是 Ren'Py 注入 store 的段落翻译函数
    # （options.rpy 的 `define gui.about = _p("""...""")` 要用它）。init 里覆盖它，
    # 中文线看不出问题，一旦 `_init_language → change_language(force=True) →
    # gui._apply_rebuild → redefine` 重跑 define 就在英文启动时崩
    # "TypeError: ... object is not callable"。统一用 `_np`。
    ALL_PROBS = {}
    for _bank in (L1, L2, L3, L4, L5, L6, L7):
        for _np in _bank:
            ALL_PROBS[_np["id"]] = _np

    if persistent.wrong_ids is None:
        persistent.wrong_ids = []

    def wrong_add(pid):
        if pid not in wrong_list:
            wrong_list.append(pid)
        if pid not in persistent.wrong_ids:
            persistent.wrong_ids.append(pid)

    def wrong_clear(pid):
        while pid in wrong_list:
            wrong_list.remove(pid)
        while pid in persistent.wrong_ids:
            persistent.wrong_ids.remove(pid)

    # 一键清空（错题本界面「清空错题本」按钮用，2026-11-06 加）：
    # 本局 wrong_list 原地清空；persistent.wrong_ids 用赋值触发脏标记，
    # 再 update(force_save=True) 强制落盘——只抹错题记录，其他
    # persistent 数据（相册解锁、音乐开关…）一概不动。
    def wrong_clear_all():
        wrong_list[:] = []
        persistent.wrong_ids = []
        renpy.persistent.update(force_save=True)

    def wrong_probs():
        _out = []
        for _pid in persistent.wrong_ids:
            _np = ALL_PROBS.get(_pid)
            if _np:
                _out.append(_np)
        return _out

    # 正确答案的展示串：选择题是「B. 选项文本」，填空题取第一个可接受写法。
    def wrong_answer_text(prob):
        if prob.get("type") == "mc":
            return "ABCD"[prob["ans"]] + ". " + q_field(prob, "opts")[prob["ans"]]
        return str(prob["ans"][0])

    # 解析文本：有的题没写 why，返回空串而不是 KeyError（q_field 会）。
    def wrong_why(prob):
        if _is_en() and prob.get("why_en"):
            return prob["why_en"]
        return prob.get("why") or ""

# ------------------------------------------------------------
# 错题本浏览界面
# mode="game"  → 课内 call screen，按钮 Return 值：None 合上 / "drill" 全做 /
#                "L3-24" 只重做这题 / "skip:L3-24" 看懂了就划掉
# mode="menu"  → 主菜单/游戏菜单用 ShowMenu("notebook", mode="menu") 打开，只能看；
#                关闭用 Return()（ShowMenu 打开的菜单里 Return 就是"退出本菜单"；
#                只有用 Show() 叠在菜单上的屏幕才必须 Hide，见 README 坑 26）
# ------------------------------------------------------------
screen notebook(mode="game"):
    modal True
    tag notebook
    $ probs = wrong_probs()
    # 课内叠在教室场景上→半透明（ee）能透出背景保持临场感；主菜单/游戏菜单
    # 背景是封面图，透出来会打架，所以 mode="menu" 用不透明底色。
    $ nb_bg = "#0b1712" if mode == "menu" else "#0b1712ee"

    add Solid(nb_bg)

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1160
        ysize 660
        padding (30, 22)
        background Solid("#173729f8")

        has vbox spacing 12

        text _("错 题 本") size 34 color "#ffd27f" xalign 0.5
        text _("两次都答错的题会留在这里。重做答对，才算真的划掉。") size 20 color "#8aa596" xalign 0.5

        if not probs:
            null height 30
            text _("空的。目前没有需要补的题——很好。") size 26 color "#f2f7f0" xalign 0.5
        else:
            viewport:
                id "nbvp"
                xfill True
                # 这里**不能**写 yfill True：vbox 里带 yfill 的子项会把后面的
                # 「重做全部错题 / 合上错题本」那一栏顶出 660 高的 frame（Ren'Py
                # 不报错，只是裁掉），和第四轮相册溢出是同一类 bug（README 坑 27）。
                # 616 = 660 - 上下 padding；减去标题 40 + 副标题 24 + 底栏 40 + 3×12
                # 的 spacing，留 460 并往下取整，短屏也不会切到底栏。
                ysize 460
                mousewheel True
                draggable True

                has vbox spacing 14

                for pb in probs:
                    frame:
                        xfill True
                        padding (18, 14)
                        background Solid("#0f261d")

                        has vbox spacing 6

                        text pb["id"] color "#ffd27f" size 20
                        text q_field(pb, "q") color "#f2f7f0" size 24
                        text (_tl(_("正确答案：")) + wrong_answer_text(pb)) color "#9fd8ff" size 22
                        if pb.get("why"):
                            text (_tl(_("解析：")) + wrong_why(pb)) color "#c9d6cd" size 20
                        if mode == "game":
                            hbox:
                                spacing 16
                                textbutton _("只重做这题") action Return(pb["id"])
                                textbutton _("看懂了，划掉") action Return("skip:" + pb["id"])

        hbox:
            spacing 18
            xalign 0.5
            if mode == "game":
                if probs:
                    textbutton _("重做全部错题") action Return("drill")
                # ⚠这里**必须**传一个非 None 的值：Return(None)（以及不传参的 Return()）
                # 在引擎里是「结束交互」的哨兵，它给 _return 塞的是 **True**（见
                # renpy/common/00action_control.rpy 的 Return.__call__），于是
                # review_wrong 里 nb_ret.startswith(...) 会 AttributeError 崩掉——
                # 玩家点「合上错题本」必崩。空串既是 str 又是假值，落回"什么也没选"。
                textbutton _("合上错题本") action Return("")
            else:
                textbutton _("关闭") action Return()
            # 清空入口（2026-11-06 加）：菜单里打开错题本也能一键抹掉全部记录。
            # 用 Confirm 弹出确认，确认后 wrong_clear_all 清空并强制落盘；
            # 下一轮屏幕重算 probs 变空，本按钮和导航里的「错题本」入口一起消失。
            if probs:
                textbutton _("清空错题本") action Confirm(
                    _("要把错题本全部清空吗？所有记录都会被抹掉，无法撤销。"),
                    Function(wrong_clear_all))

# ------------------------------------------------------------
# 错题重做：drill_mode 下不计分、不计入总题数，答对才划掉
# ------------------------------------------------------------
label drill_wrong(pid=None):
    if pid:
        $ redo_list = [ALL_PROBS[pid]]
    else:
        $ redo_list = wrong_probs()

    if not redo_list:
        $ renpy.say(sysvoice, _("错题本是空的，没有需要重做的题。"))
        return

    $ nb_before = len(persistent.wrong_ids)
    $ drill_mode = True
    call practice(redo_list)
    $ drill_mode = False
    $ nb_after = len(persistent.wrong_ids)

    if nb_after == 0:
        $ renpy.say(sysvoice, _("错题本清空了——一道不剩。"))
        云曦 "全划掉了！这份成就感请收好，它是可以复用的那种。"
    elif nb_after < nb_before:
        $ renpy.say(sysvoice, _("错题本还剩 [nb_after] 题。"))
        知微 "有进步。剩下的这几道，明天再啃一次，效率比今晚硬撑高。"
    else:
        知微 "一道都没划掉。那就别急着走——把解析读一遍，我等你。"
    return

# ------------------------------------------------------------
# 每课收尾：只有本局记了错题才弹，全对的玩家不会被打扰
# ------------------------------------------------------------
label review_wrong:
    if not wrong_list:
        return

    云曦 "等一下——错题本上记了 [len(wrong_list)] 题。现在清一清，还是留着过夜？"

    menu:
        "现在重做错题":
            call drill_wrong
        "翻错题本，看解析":
            call screen notebook(mode="game")
            # notebook 只承诺返回 str；万一交互被回滚/异常中断，_return 会是引擎的
            # True 哨兵（见上面「合上错题本」的注释），这里统一压成空串再往下判。
            $ nb_ret = _return if isinstance(_return, str) else ""
            if nb_ret == "drill":
                call drill_wrong
            elif nb_ret.startswith("skip:"):
                $ wrong_clear(nb_ret[5:])
                $ renpy.say(sysvoice, _("这一题从错题本上划掉了。"))
            elif nb_ret:
                call drill_wrong(pid=nb_ret)
        "先留着，明天再说":
            知微 "可以。但明天早上我要看到它变短。"
    return

# ------------------------------------------------------------
# 选择题界面
# ------------------------------------------------------------
screen mc_screen():
    modal True
    default shown_hint = False
    add Solid("#000000aa")
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1080
        padding (36, 28)
        background Solid("#173729f2")
        has vbox spacing 16
        text (_("错题重做 · 第 [q_round] 题") if drill_mode else _("随堂练习 · 第 [q_round] 题")) color "#ffd27f" size 24
        text q_field(q_prob, "q") color "#f2f7f0" size 32
        null height 6
        for i, opt in enumerate(q_field(q_prob, "opts")):
            textbutton ("　%s　%s" % ("ABCD"[i], opt)) action Return(i) xalign 0.0
        null height 4
        textbutton _("提 示") action [ToggleScreenVariable("shown_hint"), SetVariable("hint_used", True)]
        if shown_hint:
            text (_tl(_("提示：")) + q_field(q_prob, "hint")) color "#9fd8ff" size 24

# ------------------------------------------------------------
# 填空题界面
# ------------------------------------------------------------
screen in_screen():
    modal True
    default shown_hint = False
    add Solid("#000000aa")
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1080
        padding (36, 28)
        background Solid("#173729f2")
        has vbox spacing 16
        text (_("错题重做 · 第 [q_round] 题") if drill_mode else _("随堂练习 · 第 [q_round] 题")) color "#ffd27f" size 24
        text q_field(q_prob, "q") color "#f2f7f0" size 32
        # 只在第一道填空题出现一次；规则开局教程讲过，见 fmt_hint_seen。
        if not fmt_hint_seen:
            text _("支持写法：x^2、3x、1/2、sinx、e^x、1/x 等") color "#8aa596" size 20
        null height 6
        $ nv = VariableInputValue("user_answer")
        input:
            value nv
            xsize 900
            color "#fff4e0"
            size 34
        hbox:
            spacing 20
            textbutton _("交 卷") action Return(user_answer)
            textbutton _("提 示") action [ToggleScreenVariable("shown_hint"), SetVariable("hint_used", True)]
        if shown_hint:
            text (_tl(_("提示：")) + q_field(q_prob, "hint")) color "#9fd8ff" size 24

# ------------------------------------------------------------
# 单题流程：出题 → 判定 → 反馈（最多两次尝试，之后看答案）
# ------------------------------------------------------------
label do_problem(prob):
    $ q_prob = prob
    $ _demo = bool(prob.get("demo"))
    if not _demo and not drill_mode:
        $ total_questions += 1
    $ attempts = 0
    $ hint_used = False
    $ solved = False
    $ done = False
    while not done:
        $ empty = False
        if prob["type"] == "mc":
            call screen mc_screen
            $ resp = _return
        else:
            $ user_answer = ""
            call screen in_screen
            $ resp = _return
            $ fmt_hint_seen = True
            $ empty = (not str(resp).strip())
        if empty:
            $ renpy.say(sysvoice, _("先写出你的答案，再交卷。"))
            $ done = False
        else:
            $ attempts += 1
            if prob["type"] == "mc":
                $ ok = (resp == prob["ans"])
            else:
                $ ok = check_answer(resp, prob["ans"])
            if ok:
                $ solved = True
                $ done = True
            elif attempts >= 2:
                $ done = True
            else:
                $ renpy.say(sysvoice, _("回答不对。再看一眼题目，还有最后一次机会。"))
    if solved:
        $ _awarded = 0
        if _demo:
            $ renpy.say(sysvoice, _("（演示题，答对了！正式做题才开始计分。）"))
        elif drill_mode:
            $ wrong_clear(prob["id"])
            $ renpy.say(sysvoice, _("答对了。这题从错题本上划掉。"))
        elif attempts == 1 and not hint_used:
            $ score += 10
            $ _awarded = 10
            $ first_try_correct += 1
        elif attempts == 1 and hint_used:
            $ score += 7
            $ _awarded = 7
        else:
            $ score += 5
            $ _awarded = 5
        if _awarded:
            show expression Text("{size=44}{color=#ffd27f}+" + str(_awarded) + "{/color}{/size}") as pts at score_pop
        $ renpy.say(sysvoice, _("回答正确！"))
        $ react("ok")
        if _awarded:
            hide pts
    else:
        if not _demo:
            $ wrong_add(prob["id"])
            if drill_mode:
                $ renpy.say(sysvoice, _("还是不对——它继续留在错题本上。"))
            else:
                $ renpy.say(sysvoice, _("这题先记在错题本上。"))
        $ react("bad")
        if prob["type"] == "mc":
            $ anstext = "ABCD"[prob["ans"]] + ". " + q_field(prob, "opts")[prob["ans"]]
        else:
            $ anstext = prob["ans"][0]
        $ renpy.say(sysvoice, _tl(_("正确答案：")) + anstext)
        $ renpy.say(sysvoice, _tl(_("解析：")) + q_field(prob, "why"))
    return

# ------------------------------------------------------------
# 一组练习：进批次切 bgm_solve、出批次切回 bgm_study（剧情BGM）。
# offset 只用来续接界面上的「第 N 题」编号：一节课拆成两批时，
# 第二批要写 call practice(L1[5:10], 5)，不写的话题号会从 1 重新开始。
# ------------------------------------------------------------
label practice(plist, offset=0):
    stop music fadeout 1.2
    play music "audio/bgm_solve.ogg" fadein 1.6
    $ pi = 0
    $ n = len(plist)
    while pi < n:
        $ prob = plist[pi]
        $ pi += 1
        $ q_round = pi + offset
        call do_problem(prob=prob)
    stop music fadeout 1.2
    play music "audio/bgm_study.ogg" fadein 2.0
    return

# ------------------------------------------------------------
# 黑板插图开关
# ------------------------------------------------------------
label show_board(img):
    $ board_img = img
    # 必须带 `as board`：加了 `at board_show` 之后引擎给的自动 tag 不是 "board"，
    # 老写法 `hide expression board_img` 关不掉它，黑板会一直压到下一个 scene。
    show expression board_img as board at board_show with Dissolve(0.6)
    return

label hide_board:
    hide board with Dissolve(0.4)
    return
