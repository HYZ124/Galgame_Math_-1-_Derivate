# ============================================================
# 中英双语切换
# 中文 = 源语言（language None），English = tl/english 翻译。
# 语言探针 _is_en() 定义在 defines.rpy（strings 表按来源文件作用域）。
#
# 【只要动了带 _() 的中文，就必须跑完这条管线】（tools/ 在工程上一级）
#   1. cd 工程目录，`/d/workspace/renpy/renpy.exe . translate english`
#      —— 重新生成 tl 骨架。注意它会把已填英文的块重写成中文，
#      **英文资产只认 tools/tl_en.json 这份字典**，所以第 2 步不能省。
#   2. `python ../tools/norm_tl.py`  —— 清占位、删孤儿块。
#   3. 往 `../tools/tl_en.json` 里补新键（中文原文 → 英文译文）。
#      缺哪些键：`python ../tools/tl_new.py`（推荐——直接扫剧情源文件，不用先跑第 1 步，
#      还能按 PAIRS 片段 `--fill` 自动补进去并自检 CJK/裸%）；
#      `python ../tools/missing_keys.py` 只在 regen 之后按空占位列缺键。
#   4. `python ../tools/fill_tl.py`  —— 按字典回填（纯 ASCII 键自动恒等回填）。
#   5. `python ../tools/drop_orphans.py` —— 清掉源文已不存在的陈旧块。
#      先 `--dry` 看清单。它现在会自己找工程根（CWD 在 galgame-math 那层也能跑，
#      以前会安静地扫到 0 个文件 = 等于没跑）。`translate english <blockid>:` 的
#      对白块和 `old/new` 字符串块都管。跑完仍用 `renpy.exe . lint` 兜底：
#      lint 报 Orphan Translations 就按块 id 手删（第九轮 4 条：pre4/clue3/inter1/side1）。
#   6. `python ../tools/scan_tl_cjk.py`（tl 里残留中文）+
#      `python ../tools/scan_pct.py`（字符串里裸 %，会被当格式符崩英文线）
#      + `renpy.exe . lint`，最后**中英文各跑一遍冒烟**（中文过不代表英文过）。
#
# 【为什么改行号不影响翻译】翻译 id = md5(所在 block + 源串)，与行号无关；
#   但改一个中文字 = 换一把 key = 老译文变孤儿。所以只有"改文案"要跑管线，
#   挪代码/调 size/加 show 语句都不用。
#
# 【题库是例外】题目 dict 不走 strings 表，英文在 lessons/l*_en.rpy 里按 id
#   合并成 *_en 字段，由 math_core.q_field() 运行时挑（见 math_core.rpy 顶部）。
# ============================================================

screen lang_switcher(xalign=0.02, yalign=0.985, spacing=14):

    hbox:
        xalign xalign
        yalign yalign
        spacing spacing

        # 两个语言名故意不包 _()：切错语言时也得让人看得懂怎么切回来。
        # Language() 后面必须跟 Function(_sync_sysvoice)——Ren'Py 没有"语言变了"回调。
        textbutton "中文" action [Language(None), Function(_sync_sysvoice)] text_color ("#8aa596" if _is_en() else "#ffd27f")
        textbutton "English" action [Language("english"), Function(_sync_sysvoice)] text_color ("#ffd27f" if _is_en() else "#8aa596")
