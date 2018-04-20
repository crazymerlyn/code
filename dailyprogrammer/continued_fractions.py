from fractions import Fraction

def improper_to_continued(fraction):
    res = []
    while fraction:
        n = fraction.numerator // fraction.denominator
        res.append(n)
        fraction -= n
        if fraction:
            fraction = 1 / fraction
    return res

def continued_to_improper(gauss):
    res = Fraction(gauss[-1], 1)
    for n in gauss[::-1][1:]:
        res = n + 1 / res
    return res

def continued_to_latex(gauss):
    if len(gauss) == 1: return str(gauss[0])
    return "%d + \cfrac{1}{%s}" % (gauss[0], continued_to_latex(gauss[1:]))

def continued_to_mathml(gauss):
    if len(gauss) == 1: return "<mn>%d</mn>" % gauss[0]
    return "<mrow><mn>%d</mn><mo>+</mo><mfrac><mn>1</mn>%s</mfrac></mrow>" % (gauss[0], continued_to_mathml(gauss[1:]))

print(improper_to_continued(Fraction(45, 16)))
print(continued_to_improper([2, 1, 7]))
print(continued_to_improper([2, 2, 1, 1]))
print(continued_to_latex([2, 2, 1, 1]))
print(continued_to_mathml([2, 2, 1, 1]))
