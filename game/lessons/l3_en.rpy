# Lesson 3 English problem data, keyed by problem id fields.
# 第 3 课的英文题库：按 id 与 l3_*.rpy 文件一一对应，只放 q/opts/hint/why 四个字段，
# type/ans 以中文文件为准。合并发生在 math_core.rpy 的 init 10（_mb_esc 会一并转义
# [ ]）。加题时中文文件写完整 dict，这里补同 id 的英文条目；
# 注意英文串里不要出现裸 %（会被当格式符），要写百分号就用 "percent"。
init python:
    L3_EN = [
        {"id": "L3-01", "q": "What is the derivative of the constant function f(x) = π?", "opts": ["0", "π", "1/π", "Does not exist"], "hint": "π is written as a letter, but it is a constant - a constant has no change at all.", "why": "C′ = 0 holds for any constant, and π is a constant, so its derivative is 0. (If you picked π, you mixed up a constant with a function.)"},
        {"id": "L3-02", "q": "Differentiate: f(x) = x⁵ (write as x^5)", "hint": "Power rule: (xⁿ)′ = n·xⁿ⁻¹.", "why": "(x^5)′ = 5x⁴. Bring the exponent down as a coefficient and subtract one from the exponent."},
        {"id": "L3-03", "q": "Differentiate: f(x) = x", "hint": "x = x¹, so use the power rule; or just think of the slope of this line.", "why": "(x)′ = 1: the line y=x has slope 1 everywhere."},
        {"id": "L3-04", "q": "Differentiate: f(x) = 1/x", "hint": "Rewrite 1/x as x⁻¹ and then apply the power rule.", "why": "(x⁻¹)′ = −1·x⁻² = −1/x²."},
        {"id": "L3-05", "q": "Differentiate: f(x) = x⁻³ (write as x^-3)", "hint": "The power rule still holds for negative exponents: here n = −3.", "why": "(x⁻³)′ = −3x⁻⁴ = −3/x⁴. Even with a negative exponent, still bring it down and subtract one."},
        {"id": "L3-06", "q": "What is (√x)′ equal to?", "opts": ["1 ÷ (2√x)", "2√x", "√x ÷ 2", "−1 ÷ (2x√x)"], "hint": "√x = x^(1/2); bring the exponent 1/2 down and subtract one.", "why": "(x^(1/2))′ = (1/2)x^(−1/2) = 1/(2√x)."},
        {"id": "L3-07", "q": "Differentiate: f(x) = sin x", "hint": "The derivative of sine is cosine - one of the two rotation formulas.", "why": "(sin x)′ = cos x."},
        {"id": "L3-08", "q": "Differentiate: f(x) = cos x", "hint": "The derivative of cosine carries a minus sign: minus sine.", "why": "(cos x)′ = −sin x. Mnemonic: sine and cosine derivative each other, and cosine brings a minus along."},
        {"id": "L3-09", "q": "What is (tan x)′ equal to?", "opts": ["1 ÷ cos²x", "1 ÷ sin²x", "−1 ÷ cos²x", "cot x"], "hint": "View tan x as sin x / cos x and use the quotient rule (a preview of what is to come).", "why": "(sin/cos)′ = (cos²+sin²)/cos² = 1/cos²x. Tangent rises everywhere, so its derivative is always positive."},
        {"id": "L3-10", "q": "Differentiate: f(x) = e^x", "hint": "e^x is the stubborn one of mathematics - differentiating it returns itself.", "why": "(e^x)′ = e^x. This is the most remarkable property of the natural exponential."},
        {"id": "L3-11", "q": "What is (2^x)′ equal to?", "opts": ["2^x · ln 2", "x · 2^(x−1)", "2^x", "x · 2^(x−1) · ln 2"], "hint": "When differentiating an exponential function, the exponent stays put and you multiply by the natural log of the base.", "why": "(a^x)′ = a^x·ln a. Note the contrast with the power function xⁿ: in 2^x the variable sits in the exponent."},
        {"id": "L3-12", "q": "Differentiate: f(x) = ln x", "hint": "The derivative of the natural log is an extremely simple fraction.", "why": "(ln x)′ = 1/x."},
        {"id": "L3-13", "q": "What is (log₂x)′ equal to?", "opts": ["1 ÷ (x · ln 2)", "1/x", "ln 2 ÷ x", "1 ÷ (x · ln x)"], "hint": "(logₐx)′ = 1/(x·ln a).", "why": "Change of base: log₂x = ln x / ln 2, so the derivative = 1/(x·ln2)."},
        {"id": "L3-14", "q": "Differentiate: f(x) = 3x²", "hint": "The constant coefficient 3 stays in place; only differentiate x².", "why": "(3x²)′ = 3·2x = 6x. A constant factor can be pulled out of the derivative."},
        {"id": "L3-15", "q": "Differentiate: f(x) = x³ − 2x", "hint": "Differentiate one term at a time.", "why": "(x³)′ − (2x)′ = 3x² − 2. The derivative of a sum or difference equals the sum or difference of the derivatives."},
        {"id": "L3-16", "q": "Differentiate: f(x) = 4x³", "hint": "4 stays put, and (x³)′ = 3x².", "why": "4 · 3x² = 12x²."},
        {"id": "L3-17", "q": "Differentiate: f(x) = x⁴ (write as x^4)", "hint": "Bring the exponent down and subtract one.", "why": "(x⁴)′ = 4x³."},
        {"id": "L3-18", "q": "Differentiate: f(x) = x⁶ (write as x^6)", "hint": "Same as before, the power rule.", "why": "(x⁶)′ = 6x⁵."},
        {"id": "L3-19", "q": "Differentiate: f(x) = x² − 1/x² (write as x^2 - 1/x^2)", "hint": "−1/x² = −x⁻², and it contributes −(−2x⁻³) to the derivative.", "why": "(x²)′ = 2x; (−x⁻²)′ = 2x⁻³ = 2/x³. Minus times minus gives plus, so the middle sign is addition."},
        {"id": "L3-20", "q": "If f(x) = e^x, then f′(0) = ?", "hint": "What does the derivative of e^x give? Then substitute x=0.", "why": "f′(x) = e^x, so f′(0) = e⁰ = 1."},
        {"id": "L3-21", "q": "If f(x) = sin x, then f′(π/2) = ?", "hint": "First differentiate to get cos x, then substitute π/2.", "why": "f′(π/2) = cos(π/2) = 0: at the crest of the sine wave the tangent line is horizontal."},
        {"id": "L3-22", "q": "If f(x) = cos x, then f′(π/2) = ?", "hint": "(cos x)′ = −sin x.", "why": "f′(π/2) = −sin(π/2) = −1: the cosine curve falls fastest at π/2."},
        {"id": "L3-23", "q": "What is the power rule (xⁿ)′ = ? (n is a constant)", "opts": ["n·xⁿ⁻¹", "n·xⁿ", "xⁿ⁻¹ ÷ (n−1)", "xⁿ⁺¹ ÷ (n+1)"], "hint": "Bring the exponent down and subtract one.", "why": "(xⁿ)′ = n·xⁿ⁻¹. The option written as xⁿ⁺¹ ÷ (n+1) is an integration formula - do not grab the wrong weapon."},
        {"id": "L3-24", "q": "Which of the following derivative formulas is correct?", "opts": ["(ln x)′ = 1/x", "(1/x)′ = 1/x²", "(cos x)′ = sin x", "(e^x)′ = x·e^(x−1)"], "hint": "Rule out errors one by one: the derivative of 1/x carries a minus sign; the derivative of cos carries a minus sign; differentiating e^x still gives e^x.", "why": "Only (ln x)′ = 1/x is correct. The rest are three classic mistake hotspots."},
        {"id": "L3-25", "q": "Differentiate: f(x) = 5x", "hint": "What is the slope of the line y=5x?", "why": "(5x)′ = 5; the derivative of a linear function is exactly its slope."},
        {"id": "L3-26", "q": "What is (1/√x)′ equal to?", "opts": ["−1 ÷ (2x√x)", "1 ÷ (2√x)", "−√x ÷ 2", "1 ÷ (2x√x)"], "hint": "1/√x = x^(−1/2); use the power rule as usual.", "why": "(x^(−1/2))′ = −(1/2)x^(−3/2) = −1/(2x√x)."},
        {"id": "L3-27", "q": "Differentiate: f(x) = log₃x (write as log3(x); the answer may contain ln3)", "hint": "(logₐx)′ = 1/(x·ln a).", "why": "log₃x = ln x/ln 3; pull the coefficient 1/ln3 out front, so the derivative is 1/(x·ln3)."},
        {"id": "L3-28", "q": "If f(x) = x⁴ (write as x^4), find f′(2).", "hint": "First find f′(x) = 4x³, then substitute x=2.", "why": "f′(2) = 4·8 = 32."},
        {"id": "L3-29", "q": "Which of the following functions has derivative 2x?", "opts": ["f(x) = x²", "f(x) = x", "f(x) = 2x²", "f(x) = x³ ÷ 2"], "hint": "Differentiation lowers the degree by one, so which function - after adjusting coefficients - lands exactly on 2x?", "why": "(x²)′ = 2x. Check the other options: (2x²)′=4x, (x³/2)′=(3/2)x²."},
        {"id": "L3-30", "q": "Differentiate: f(x) = (1/2)x² (entering x^2/2 or 0.5x^2 both work)", "hint": "The coefficient 1/2 and the exponent 2 multiply to cancel exactly.", "why": "(x²/2)′ = (1/2)·2x = x. This is also why a factor of 1/2 shows up in integration."},
    ]
