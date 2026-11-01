# ============================================================
# 第 4 课题库：导数的四则运算（25 题）
#
# 【实跑题量】本文件存 25 题，游戏里只取前 8 题——切片位置在 script.rpy 的
#   `call practice(L4[a:b], off)`（off 只续接界面题号）。要加题量改切片，别删题。
# 【加一题的字段】id（L4-NN，全工程唯一）/ type（mc 或 in）/ q / opts（4 项，仅 mc）/
#   ans / hint / why。ans：mc 写正确项下标且**永远写 0**，位置由 math_core 的 init 20
#   自动轮换；in 写可接受答案列表，把 "1/2"、"0.5" 这类等价写法都列上。
#   题面里可以直接写 [ ]，引擎会转全角，不会触发 Text 插值。
# 【必须同步】同 id 的英文条目要一起加进 l4_en.rpy，漏了不报错，但英文模式下
#   这道题会退回显示中文（q_field 兜底）。
# ============================================================

init python:
    L4 = [
        {"id": "L4-01", "type": "mc",
         "q": "和差的求导法则是？",
         "opts": ["(u ± v)′ = u′ ± v′", "(u ± v)′ = u′ · v′", "(u ± v)′ = u ± v′", "(u ± v)′ = u′ ± v"],
         "ans": 0,
         "hint": "加减法是最宽容的：可以一项一项分开求导。",
         "why": "和（差）的导数等于导数的和（差），逐项求导即可。"},

        {"id": "L4-02", "type": "mc",
         "q": "乘积的求导法则 (uv)′ = ？",
         "opts": ["u′v + uv′", "u′v′", "uv′ − u′v", "u′v − uv′"],
         "ans": 0,
         "hint": "口诀：前导后不动，加后导前不动。",
         "why": "(uv)′ = u′v + uv′。两项相“加”，这是乘积法则的标志。"},

        {"id": "L4-03", "type": "mc",
         "q": "商的求导法则 (u/v)′ = ？（v ≠ 0）",
         "opts": ["(u′v − uv′) ÷ v²", "(uv′ − u′v) ÷ v²", "u′ ÷ v′", "(u′v + uv′) ÷ v²"],
         "ans": 0,
         "hint": "口诀：子导母不动，减母导子不动，分母平方。（分子顺序：u′v 在前）",
         "why": "(u/v)′ = (u′v − uv′)/v²。分子是“减”，分母要平方。"},

        {"id": "L4-04", "type": "in",
         "q": "求导：f(x) = x² + sin x",
         "ans": ["2x+cosx"],
         "hint": "逐项求导。",
         "why": "(x²)′ + (sin x)′ = 2x + cos x。"},

        {"id": "L4-05", "type": "in",
         "q": "求导：f(x) = x³ − cos x",
         "ans": ["3x^2+sinx"],
         "hint": "注意 (cos x)′ = −sin x，负负得正。",
         "why": "3x² − (−sin x) = 3x² + sin x。减负号变加，是高频错误点。"},

        {"id": "L4-06", "type": "in",
         "q": "求导：f(x) = x·e^x",
         "ans": ["(x+1)e^x", "xe^x+e^x", "e^x(x+1)", "e^x(x+1)"],
         "hint": "乘积法则：u=x，v=e^x。",
         "why": "1·e^x + x·e^x = (x+1)e^x。提取公因式 e^x 更简洁。"},

        {"id": "L4-07", "type": "in",
         "q": "求导：f(x) = x·sin x",
         "ans": ["sinx+xcosx", "xcosx+sinx"],
         "hint": "(uv)′ = u′v + uv′，u=x，v=sin x。",
         "why": "1·sin x + x·cos x = sin x + x cos x。"},

        {"id": "L4-08", "type": "in",
         "q": "求导：f(x) = x²·ln x",
         "ans": ["2xlnx+x", "x+2xlnx"],
         "hint": "u=x²，v=ln x，用乘积法则。",
         "why": "2x·ln x + x²·(1/x) = 2x ln x + x。第二项约掉一个 x。"},

        {"id": "L4-09", "type": "in",
         "q": "求导：f(x) = x ÷ e^x",
         "ans": ["(1-x)/e^x", "(1-x)e^-x"],
         "hint": "商法则：u=x，v=e^x；或者看成乘积 x·e^(−x)。",
         "why": "(1·e^x − x·e^x)/e^(2x) = (1−x)/e^x。"},

        {"id": "L4-10", "type": "in",
         "q": "求导：f(x) = ln x ÷ x",
         "ans": ["(1-lnx)/x^2"],
         "hint": "u=ln x，v=x，商法则。",
         "why": "[(1/x)·x − ln x·1]/x² = (1 − ln x)/x²。"},

        {"id": "L4-11", "type": "in",
         "q": "求导：f(x) = (x+1)(x−1)。提示：可以先化简再求导。",
         "ans": ["2x"],
         "hint": "(x+1)(x−1) 是平方差公式，先展开。",
         "why": "f(x) = x² − 1，所以 f′(x) = 2x。能化简先化简，比硬上乘积法则快。"},

        {"id": "L4-12", "type": "in",
         "q": "求导：f(x) = x² + 1/x",
         "ans": ["2x-1/x^2"],
         "hint": "第一项用幂公式，第二项 (1/x)′ = −1/x²。",
         "why": "(x²)′ + (x⁻¹)′ = 2x − 1/x²。"},

        {"id": "L4-13", "type": "in",
         "q": "求导：f(x) = 3x² + 2x − 5",
         "ans": ["6x+2"],
         "hint": "逐项求导，常数项变 0。",
         "why": "6x + 2 − 0 = 6x + 2。"},

        {"id": "L4-14", "type": "in",
         "q": "求导：f(x) = sin x − x + 1",
         "ans": ["cosx-1"],
         "hint": "三项分别求导。",
         "why": "cos x − 1 + 0 = cos x − 1。"},

        {"id": "L4-15", "type": "mc",
         "q": "下列计算正确的是？",
         "opts": ["(x·cos x)′ = cos x − x·sin x", "(x·cos x)′ = cos x + x·sin x", "(x·cos x)′ = −x·sin x", "(x·cos x)′ = x·cos x"],
         "ans": 0,
         "hint": "乘积法则，注意 (cos x)′ 自带负号。",
         "why": "1·cos x + x·(−sin x) = cos x − x sin x。漏掉余弦导数的负号就会选 B。"},

        {"id": "L4-16", "type": "in",
         "q": "求导：f(x) = e^x·sin x",
         "ans": ["e^x(sinx+cosx)", "e^xsinx+e^xcosx"],
         "hint": "u=e^x，v=sin x；e^x 求导不变。",
         "why": "e^x·sin x + e^x·cos x = e^x(sin x + cos x)。"},

        {"id": "L4-17", "type": "in",
         "q": "求导：f(x) = (x²+1)(x²−1)。提示：先化简。",
         "ans": ["4x^3"],
         "hint": "平方差：f = x⁴ − 1。",
         "why": "f(x) = x⁴ − 1，f′(x) = 4x³。"},

        {"id": "L4-18", "type": "in",
         "q": "求导：f(x) = x³·ln x",
         "ans": ["3x^2lnx+x^2"],
         "hint": "乘积法则，(ln x)′ = 1/x，x³·(1/x) 约分。",
         "why": "3x²·ln x + x³/x = 3x² ln x + x²。"},

        {"id": "L4-19", "type": "in",
         "q": "求导：f(x) = (x+1)·e^x",
         "ans": ["(x+2)e^x", "xe^x+2e^x", "e^x(x+2)", "e^x(x+2)"],
         "hint": "1·e^x + (x+1)·e^x，提取 e^x。",
         "why": "e^x + (x+1)e^x = (x+2)e^x。"},

        {"id": "L4-20", "type": "in",
         "q": "求导：f(x) = (x+1) ÷ x。提示：先拆成 1 + 1/x。",
         "ans": ["-1/x^2"],
         "hint": "(x+1)/x = 1 + 1/x，常数求导为 0。",
         "why": "f = 1 + x⁻¹，f′ = −x⁻² = −1/x²。化简永远优先于硬算。"},

        {"id": "L4-21", "type": "in",
         "q": "求导：f(x) = 1/x + 1/x²",
         "ans": ["-1/x^2-2/x^3", "-x^-2-2x^-3"],
         "hint": "写成 x⁻¹ + x⁻² 再逐项求导。",
         "why": "−x⁻² − 2x⁻³ = −1/x² − 2/x³。"},

        {"id": "L4-22", "type": "in",
         "q": "f(x) = (x²+1)(x−1)，求 f′(1)。",
         "ans": ["2", "2.0"],
         "hint": "乘积法则后代入 x=1；或者先展开成三次多项式。",
         "why": "f′ = 2x(x−1) + (x²+1)，代入 x=1 得 0 + 2 = 2。"},

        {"id": "L4-23", "type": "mc",
         "q": "(sin x ÷ x)′ 等于？（x ≠ 0）",
         "opts": ["(x·cos x − sin x) ÷ x²", "(x·cos x + sin x) ÷ x²", "cos x ÷ x", "(sin x − x·cos x) ÷ x²"],
         "ans": 0,
         "hint": "商法则：u′v − uv′，u=sin x，v=x。",
         "why": "[cos x·x − sin x·1]/x² = (x cos x − sin x)/x²。"},

        {"id": "L4-24", "type": "in",
         "q": "求导：f(x) = x² · x³。提示：先合并指数。",
         "ans": ["5x^4"],
         "hint": "同底数幂相乘，指数相加。",
         "why": "f = x⁵，f′ = 5x⁴。先化简，别对着乘积法则硬算。"},

        {"id": "L4-25", "type": "mc",
         "q": "y = x − 1/x 的导数是？",
         "opts": ["1 + 1/x²", "1 − 1/x²", "1 + x²", "−1/x²"],
         "ans": 0,
         "hint": "减去 (1/x)′ = −1/x²，负负得正。",
         "why": "1 − (−1/x²) = 1 + 1/x²。"},
    ]
