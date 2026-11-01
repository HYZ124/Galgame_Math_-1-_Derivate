# Lesson 5 English problem data, keyed by problem id fields.
# 第 5 课的英文题库：按 id 与 l5_*.rpy 文件一一对应，只放 q/opts/hint/why 四个字段，
# type/ans 以中文文件为准。合并发生在 math_core.rpy 的 init 10（_mb_esc 会一并转义
# [ ]）。加题时中文文件写完整 dict，这里补同 id 的英文条目；
# 注意英文串里不要出现裸 %（会被当格式符），要写百分号就用 "percent"。
init python:
    L5_EN = [
        {"id": "L5-01", "q": "Chain rule: what is the derivative of y = f(g(x))?", "opts": ["f′(g(x)) · g′(x)", "f′(x) · g′(x)", "f′(g(x))", "f(g′(x))"], "hint": "Differentiate the outer layer first (keeping the inner layer as it is), then multiply by the derivative of the inner layer.", "why": "y′ = f′(g(x))·g′(x): outer derivative times inner derivative, linked together like a chain."},
        {"id": "L5-02", "q": "Differentiate: f(x) = (3x+1)⁵ (write it as (3x+1)^5)", "hint": "Outer u⁵ → 5u⁴; inner 3x+1 → 3. Multiply them.", "why": "5(3x+1)⁴ · 3 = 15(3x+1)⁴. Do not forget the inner derivative 3."},
        {"id": "L5-03", "q": "Differentiate: f(x) = sin 2x", "hint": "Outer cos; the derivative of the inner 2x is 2.", "why": "cos(2x)·2 = 2cos 2x. Writing only cos2x is the most common point lost."},
        {"id": "L5-04", "q": "Differentiate: f(x) = cos 3x", "hint": "The cosine derivative carries a minus sign, then multiply by the inner derivative 3.", "why": "−sin(3x)·3 = −3 sin 3x."},
        {"id": "L5-05", "q": "Differentiate: f(x) = e^(2x)", "hint": "Differentiating e^u still gives e^u, then multiply by u′ = 2.", "why": "e^(2x)·2 = 2e^(2x)."},
        {"id": "L5-06", "q": "Differentiate: f(x) = (2x−1)³ (write it as (2x-1)^3)", "hint": "Outer 3u², inner derivative 2.", "why": "3(2x−1)²·2 = 6(2x−1)²."},
        {"id": "L5-07", "q": "Differentiate: f(x) = (1−2x)⁴ (write it as (1-2x)^4)", "hint": "The inner 1−2x differentiates to −2; do not lose the minus sign.", "why": "4(1−2x)³·(−2) = −8(1−2x)³."},
        {"id": "L5-08", "q": "Differentiate: f(x) = e^(x²) (write it as e^(x^2))", "hint": "The outer e^u stays unchanged; differentiating the inner x² gives 2x.", "why": "e^(x²)·2x = 2x·e^(x²)."},
        {"id": "L5-09", "q": "Differentiate: f(x) = (x²+1)² (write it as (x^2+1)^2)", "hint": "Outer 2u, inner 2x; multiply.", "why": "2(x²+1)·2x = 4x(x²+1) = 4x³+4x; both forms are correct."},
        {"id": "L5-10", "q": "(ln(x²+1))′ = ?", "opts": ["2x ÷ (x²+1)", "1 ÷ (x²+1)", "2 ÷ (x²+1)", "x ÷ (x²+1)"], "hint": "(ln u)′ = u′/u.", "why": "u = x²+1, u′ = 2x, so the derivative = 2x/(x²+1)."},
        {"id": "L5-11", "q": "(√(x+1))′ = ?", "opts": ["1 ÷ (2√(x+1))", "√(x+1) ÷ 2", "1 ÷ √(x+1)", "2√(x+1)"], "hint": "Outer (√u)′ = 1/(2√u); inner (x+1)′ = 1.", "why": "= 1/(2√(x+1)). The inner derivative happens to be 1, so the chain rule goes invisible here."},
        {"id": "L5-12", "q": "(sin²x)′ = ? (sin²x means (sin x)²)", "opts": ["2 sin x · cos x", "2 sin x", "cos²x", "−2 sin x · cos x"], "hint": "Treat sin²x as u² with u = sin x.", "why": "2 sin x · (sin x)′ = 2 sin x cos x. It also equals sin 2x."},
        {"id": "L5-13", "q": "(cos(ln x))′ = ?", "opts": ["−sin(ln x) ÷ x", "sin(ln x) ÷ x", "−sin(ln x)", "cos(ln x) ÷ x"], "hint": "Outer −sin(u); inner u = ln x, u′ = 1/x.", "why": "−sin(ln x)·(1/x) = −sin(ln x)/x. Neither layer may be skipped."},
        {"id": "L5-14", "q": "(3^(x²))′ = ?", "opts": ["3^(x²) · ln 3 · 2x", "3^(x²) · ln 3", "x² · 3^(x²−1)", "3^(x²) · 2x"], "hint": "Exponential type: (a^u)′ = a^u · ln a · u′.", "why": "The a^u rule first gives 3^(x²)ln3, then multiply by the inner (x²)′ = 2x. All three factors are indispensable."},
        {"id": "L5-15", "q": "Differentiate: f(x) = ln 2x", "hint": "Chain rule: 1/(2x) · 2 = ? Or use ln2x = ln2 + lnx.", "why": "(ln 2x)′ = (1/2x)·2 = 1/x. ln2 is a constant, so it should not appear in the derivative."},
        {"id": "L5-16", "q": "Differentiate: f(x) = sin(2x+1)", "hint": "Outer cos; the derivative of the inner 2x+1 is 2.", "why": "cos(2x+1)·2 = 2cos(2x+1)."},
        {"id": "L5-17", "q": "f(x) = sin²x (that is, (sin x)²); find f′(π/4).", "hint": "f′ = 2 sin x cos x; sin(π/4)=cos(π/4)=√2/2.", "why": "f′(π/4) = 2·(√2/2)·(√2/2) = 1."},
        {"id": "L5-18", "q": "Differentiate: f(x) = e^(−3x) (write it as e^(-3x))", "hint": "The derivative of the inner −3x is −3.", "why": "e^(−3x)·(−3) = −3e^(−3x)."},
        {"id": "L5-19", "q": "Differentiate: f(x) = (5x+2)³ (write it as (5x+2)^3)", "hint": "Outer 3u², inner 5.", "why": "3(5x+2)²·5 = 15(5x+2)²."},
        {"id": "L5-20", "q": "Differentiate: f(x) = 1 ÷ (2x+1) (write it as 1/(2x+1))", "hint": "View it as (2x+1)⁻¹: power rule plus inner derivative 2.", "why": "−(2x+1)⁻²·2 = −2/(2x+1)²."},
        {"id": "L5-21", "q": "(√(x²+1))′ = ?", "opts": ["x ÷ √(x²+1)", "1 ÷ (2√(x²+1))", "x ÷ √x", "2x ÷ √(x²+1)"], "hint": "Outer 1/(2√u), inner u′ = 2x; multiply and cancel.", "why": "[1/(2√(x²+1))]·2x = x/√(x²+1)."},
        {"id": "L5-22", "q": "Differentiate: f(x) = cos²x (that is, (cos x)²)", "hint": "Outer 2u; inner (cos x)′ = −sin x.", "why": "2cos x·(−sin x) = −2 sin x cos x = −sin 2x."},
        {"id": "L5-23", "q": "f(x) = e^(5x); find f′(0).", "hint": "f′(x) = 5e^(5x); when substituting x=0, e⁰=1.", "why": "f′(0) = 5e⁰ = 5."},
        {"id": "L5-24", "q": "(tan 3x)′ = ?", "opts": ["3 ÷ cos²3x", "3 ÷ cos²x", "1 ÷ cos²3x", "−3 ÷ cos²3x"], "hint": "(tan u)′ = u′/cos²u.", "why": "u=3x, u′=3, so the answer is 3/cos²(3x). Keep the factor 3 and do not move it anywhere else."},
        {"id": "L5-25", "q": "Differentiate: f(x) = (x−1) ÷ (x+1) (write it as (x-1)/(x+1))", "hint": "Quotient rule: [1·(x+1) − (x−1)·1]/(x+1)²; the numerator is a constant.", "why": "(x+1−x+1)/(x+1)² = 2/(x+1)²."},
    ]
