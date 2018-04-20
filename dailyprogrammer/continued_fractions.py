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

    print(improper_to_continued(Fraction(45, 16)))
    print(continued_to_improper([2, 1, 7]))
    print(continued_to_improper([2, 2, 1, 1]))
