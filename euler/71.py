from fractions import gcd, Fraction

m = Fraction(0, 1)

for i in range(2, 1000001):
    if i % 7 ==0: continue
    numerator = (3 * i) / 7
    if gcd(numerator, i) == 1 and Fraction(numerator, i) > m:
        m = Fraction(numerator, i)

print m

