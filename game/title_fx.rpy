# ============================================================
# 《导数物语》封面动效 v2（osu!lazer 风格）：
# 软光斑缓慢漂移 + 鼠标视差分层 + 菜单滑入。
# 旧版漂浮数学符号已移除。
#
# ⚠ 2026-11-06 起**全部停用**：玩家嫌主菜单背景"动来动去"，screens.rpy 的
#   main_menu 已改成纯静态背景（不再 use title_fx，不再挂 title_breathe /
#   fx_parallax / title_float）。本文件的变换都保留着没删，想恢复动效就把
#   screens.rpy main_menu 里注释掉的 at 变换加回来（对照 git 历史即可）。
#   唯一还在用的：menu_slide（主菜单入场一次性滑入，不循环）。
#
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

# 标题文字：悬浮 + 视差（已停用，见文件头）
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

# screen title_fx() 已于 2026-11-06 删除（背景静态化后无引用，留着会挂
# audit 的 C_unused_screens）。要恢复动效：从 git 历史取回该 screen，
# 并在 screens.rpy main_menu 里加回 `use title_fx` 与各 at 变换。
