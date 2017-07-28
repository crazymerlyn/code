from fractions import Fraction

res = Fraction(1, 1)
for i in range(99, 1, -1):
    digit = 2*i//3 if i % 3 == 0 else 1
    res = digit + 1/res
res = 2 + 1/res

print(sum(int(d) for d in str(res.numerator)))
