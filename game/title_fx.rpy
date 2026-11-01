# ============================================================
# 《导数物语》封面动效 v2（osu!lazer 风格）：
# 软光斑缓慢漂移 + 鼠标视差分层 + 菜单滑入。
# 旧版漂浮数学符号已移除。
#
# 【谁在用】screens.rpy 的 main_menu：`use title_fx`（光斑/尘埃层）、
#   背景 `at title_breathe`、菜单 `at menu_slide`、版本号 `at title_float`。
# 【想再加一层视差】把内容包进 `fixed: at fx_parallax(depth)`：depth 正负决定
#   跟手还是逆手，绝对值越大位移越明显（现在用 0.012~0.018 这个量级）。
# 【引擎限制，别再踩】多个变换叠加只能嵌套 fixed，`at A + B` 在 8.5 不支持；
#   ATL 里没有 while / $ / rotation 属性，循环动画用 function 语句 + repeat。
# ============================================================

# 背景：极慢的镜头呼吸（保留一点点），配合鼠标反向视差
transform title_breathe:
    xalign 0.5
    yalign 0.5
    zoom 1.03
    parallel:
        linear 13.0 zoom 1.07
        linear 13.0 zoom 1.03
        repeat

# 鼠标视差：depth>0 顺鼠标，depth<0 逆鼠标（像素 = 偏移比例 * 半屏）
init python:
    def _fx_parallax_apply(depth):
        def _fn(trans, st, a):
            try:
                pos = renpy.get_mouse_pos()
                vw, vh = renpy.virtual_size()
            except Exception:
                return 0.05
            if pos is None or pos[0] < 0:
                tx = ty = 0.0
            else:
                tx = (pos[0] - vw / 2.0) * depth
                ty = (pos[1] - vh / 2.0) * depth
            cx = trans.xoffset or 0
            cy = trans.yoffset or 0
            trans.xoffset = cx + (tx - cx) * 0.18
            trans.yoffset = cy + (ty - cy) * 0.18
            return 0.05
        return _fn

transform fx_parallax(depth):
    function _fx_parallax_apply(depth)

# 光斑漂移：从中心慢慢游到别处再回来，附带呼吸缩放与淡入
transform fx_drift(x, y, dx, dy, dur, a, z0, z1):
    xalign x
    yalign y
    zoom z0
    alpha 0.0
    easein 1.6 alpha a
    parallel:
        ease dur xalign (x + dx)
        ease dur xalign (x - dx)
        ease dur xalign x
        repeat
    parallel:
        ease (dur * 0.8) yalign (y + dy)
        ease (dur * 1.2) yalign (y - dy)
        ease (dur * 0.8) yalign y
        repeat
    parallel:
        ease (dur * 0.9) zoom z1
        ease (dur * 0.9) zoom z0
        repeat

# 小方块尘埃（lazer 式漂浮几何）
transform fx_dust(x, y, dur):
    xalign x
    yalign y
    alpha 0.0
    easein 2.0 alpha 0.14
    parallel:
        ease dur yalign (y - 0.22)
        ease 0.01 yalign (y + 0.18)
        ease dur yalign y
        repeat
    parallel:
        ease (dur * 0.35) zoom 1.5
        ease (dur * 0.35) zoom 1.0
        repeat

# 菜单整体滑入（lazer：从左缓出 + 轻微上浮）
transform menu_slide:
    xoffset 0
    alpha 1.0
    time 0.0
    xoffset -90
    alpha 0.0
    easeout 0.8 xoffset 0
    easein 0.55 alpha 1.0

# 标题文字：悬浮 + 视差
transform title_float:
    alpha 0.95
    parallel:
        linear 3.0 alpha 1.0
        linear 3.0 alpha 0.95
        repeat
    parallel:
        ease 2.6 yoffset -6
        ease 2.6 yoffset 0
        repeat

screen title_fx():
    zorder 10
    # 外层 fixed 只做鼠标视差，内层 add 做自身漂移（Ren'Py 不支持 at A + B 链式）
    fixed:
        at fx_parallax(0.050)
        add "images/fx/blob_cyan.png" at fx_drift(0.78, 0.30, 0.05, 0.05, 11, 0.50, 1.5, 1.9)
    fixed:
        at fx_parallax(0.038)
        add "images/fx/blob_amber.png" at fx_drift(0.16, 0.72, 0.06, 0.04, 14, 0.40, 1.7, 2.1)
    fixed:
        at fx_parallax(0.060)
        add "images/fx/blob_teal.png" at fx_drift(0.62, 0.82, 0.04, 0.05, 12, 0.45, 1.3, 1.6)
    fixed:
        at fx_parallax(0.030)
        add "images/fx/blob_blue.png" at fx_drift(0.30, 0.22, 0.05, 0.03, 16, 0.42, 1.9, 2.3)
    fixed:
        at fx_parallax(0.055)
        add "images/fx/blob_pink.png" at fx_drift(0.90, 0.55, 0.03, 0.06, 13, 0.35, 1.1, 1.4)
    # 漂浮小方块
    fixed:
        at fx_parallax(0.07)
        for _i, (_x, _y, _d) in enumerate([(0.12, 0.35, 15), (0.45, 0.12, 18), (0.86, 0.78, 16), (0.55, 0.62, 20), (0.25, 0.88, 17)]):
            add Solid("#dff2ff", xsize=14, ysize=14) at fx_dust(_x, _y, _d)
