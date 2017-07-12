from fractions import Fraction

count = 0
res = Fraction(1, 1)
for i in range(1, 1001):
    res = 1 + 1 / (1 + res)
    if len(str(res.numerator)) > len(str(res.denominator)):
        count += 1
print count
