# Lesson 4 English problem data, keyed by problem id fields.
# 第 4 课的英文题库：按 id 与 l4_*.rpy 文件一一对应，只放 q/opts/hint/why 四个字段，
# type/ans 以中文文件为准。合并发生在 math_core.rpy 的 init 10（_mb_esc 会一并转义
# [ ]）。加题时中文文件写完整 dict，这里补同 id 的英文条目；
# 注意英文串里不要出现裸 %（会被当格式符），要写百分号就用 "percent"。
init python:
    L4_EN = [
        {"id": "L4-01", "q": "What is the sum/difference rule for derivatives?", "opts": ["(u ± v)′ = u′ ± v′", "(u ± v)′ = u′ · v′", "(u ± v)′ = u ± v′", "(u ± v)′ = u′ ± v"], "hint": "Sums and differences are the friendliest: differentiate term by term.", "why": "The derivative of a sum (difference) equals the sum (difference) of the derivatives; just differentiate each term separately."},
        {"id": "L4-02", "q": "Product rule: (uv)′ = ?", "opts": ["u′v + uv′", "u′v′", "uv′ − u′v", "u′v − uv′"], "hint": "Mnemonic: derivative of the first times the second, plus derivative of the second times the first.", "why": "(uv)′ = u′v + uv′. The two terms are joined by a plus sign — the hallmark of the product rule."},
        {"id": "L4-03", "q": "Quotient rule: (u/v)′ = ? (v ≠ 0)", "opts": ["(u′v − uv′) ÷ v²", "(uv′ − u′v) ÷ v²", "u′ ÷ v′", "(u′v + uv′) ÷ v²"], "hint": "Mnemonic: derivative of the numerator times the denominator, minus derivative of the denominator times the numerator, over the denominator squared. (Order in the numerator: u′v comes first.)", "why": "(u/v)′ = (u′v − uv′)/v². The numerator uses a minus sign, and the denominator is squared."},
        {"id": "L4-04", "q": "Differentiate: f(x) = x² + sin x", "hint": "Differentiate term by term.", "why": "(x²)′ + (sin x)′ = 2x + cos x."},
        {"id": "L4-05", "q": "Differentiate: f(x) = x³ − cos x", "hint": "Note that (cos x)′ = −sin x, so the two negatives combine into a plus.", "why": "3x² − (−sin x) = 3x² + sin x. Subtracting a negative turns into addition — a very common mistake."},
        {"id": "L4-06", "q": "Differentiate: f(x) = x·e^x", "hint": "Product rule: u=x, v=e^x.", "why": "1·e^x + x·e^x = (x+1)e^x. Factoring out the common e^x is cleaner."},
        {"id": "L4-07", "q": "Differentiate: f(x) = x·sin x", "hint": "(uv)′ = u′v + uv′, with u=x and v=sin x.", "why": "1·sin x + x·cos x = sin x + x cos x."},
        {"id": "L4-08", "q": "Differentiate: f(x) = x²·ln x", "hint": "u=x², v=ln x; use the product rule.", "why": "2x·ln x + x²·(1/x) = 2x ln x + x. One x cancels in the second term."},
        {"id": "L4-09", "q": "Differentiate: f(x) = x ÷ e^x", "hint": "Quotient rule with u=x and v=e^x; or view it as the product x·e^(−x).", "why": "(1·e^x − x·e^x)/e^(2x) = (1−x)/e^x."},
        {"id": "L4-10", "q": "Differentiate: f(x) = ln x ÷ x", "hint": "u=ln x, v=x; use the quotient rule.", "why": "[(1/x)·x − ln x·1]/x² = (1 − ln x)/x²."},
        {"id": "L4-11", "q": "Differentiate: f(x) = (x+1)(x−1). Note: you can simplify first, then differentiate.", "hint": "(x+1)(x−1) is a difference of squares; expand it first.", "why": "f(x) = x² − 1, so f′(x) = 2x. Simplifying first is faster than forcing the product rule."},
        {"id": "L4-12", "q": "Differentiate: f(x) = x² + 1/x", "hint": "Power rule for the first term; for the second, (1/x)′ = −1/x².", "why": "(x²)′ + (x⁻¹)′ = 2x − 1/x²."},
        {"id": "L4-13", "q": "Differentiate: f(x) = 3x² + 2x − 5", "hint": "Differentiate term by term; the constant term becomes 0.", "why": "6x + 2 − 0 = 6x + 2."},
        {"id": "L4-14", "q": "Differentiate: f(x) = sin x − x + 1", "hint": "Differentiate the three terms separately.", "why": "cos x − 1 + 0 = cos x − 1."},
        {"id": "L4-15", "q": "Which of the following computations is correct?", "opts": ["(x·cos x)′ = cos x − x·sin x", "(x·cos x)′ = cos x + x·sin x", "(x·cos x)′ = −x·sin x", "(x·cos x)′ = x·cos x"], "hint": "Product rule; note that (cos x)′ already carries a minus sign.", "why": "1·cos x + x·(−sin x) = cos x − x sin x. Dropping the minus sign from the cosine derivative leads you to pick B."},
        {"id": "L4-16", "q": "Differentiate: f(x) = e^x·sin x", "hint": "u=e^x, v=sin x; differentiating e^x leaves it unchanged.", "why": "e^x·sin x + e^x·cos x = e^x(sin x + cos x)."},
        {"id": "L4-17", "q": "Differentiate: f(x) = (x²+1)(x²−1). Note: simplify first.", "hint": "Difference of squares: f = x⁴ − 1.", "why": "f(x) = x⁴ − 1, f′(x) = 4x³."},
        {"id": "L4-18", "q": "Differentiate: f(x) = x³·ln x", "hint": "Product rule; (ln x)′ = 1/x, and x³·(1/x) cancels down.", "why": "3x²·ln x + x³/x = 3x² ln x + x²."},
        {"id": "L4-19", "q": "Differentiate: f(x) = (x+1)·e^x", "hint": "1·e^x + (x+1)·e^x; factor out e^x.", "why": "e^x + (x+1)e^x = (x+2)e^x."},
        {"id": "L4-20", "q": "Differentiate: f(x) = (x+1) ÷ x. Note: split it into 1 + 1/x first.", "hint": "(x+1)/x = 1 + 1/x, and the constant differentiates to 0.", "why": "f = 1 + x⁻¹, f′ = −x⁻² = −1/x². Simplifying always beats brute force."},
        {"id": "L4-21", "q": "Differentiate: f(x) = 1/x + 1/x²", "hint": "Rewrite as x⁻¹ + x⁻² and differentiate term by term.", "why": "−x⁻² − 2x⁻³ = −1/x² − 2/x³."},
        {"id": "L4-22", "q": "f(x) = (x²+1)(x−1); find f′(1).", "hint": "Apply the product rule and then substitute x=1; or expand into a cubic polynomial first.", "why": "f′ = 2x(x−1) + (x²+1); substituting x=1 gives 0 + 2 = 2."},
        {"id": "L4-23", "q": "What is (sin x ÷ x)′? (x ≠ 0)", "opts": ["(x·cos x − sin x) ÷ x²", "(x·cos x + sin x) ÷ x²", "cos x ÷ x", "(sin x − x·cos x) ÷ x²"], "hint": "Quotient rule: u′v − uv′, with u=sin x and v=x.", "why": "[cos x·x − sin x·1]/x² = (x cos x − sin x)/x²."},
        {"id": "L4-24", "q": "Differentiate: f(x) = x² · x³. Note: combine the exponents first.", "hint": "Powers with the same base multiply by adding exponents.", "why": "f = x⁵, f′ = 5x⁴. Simplify first instead of grinding through the product rule."},
        {"id": "L4-25", "q": "What is the derivative of y = x − 1/x?", "opts": ["1 + 1/x²", "1 − 1/x²", "1 + x²", "−1/x²"], "hint": "Subtracting (1/x)′ = −1/x² turns minus-minus into plus.", "why": "1 − (−1/x²) = 1 + 1/x²."},
    ]
