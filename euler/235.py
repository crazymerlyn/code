def s(r):
    n = 5000.0
    a = 900.0 - 3.0
    d = -3.0
    return (a - (a + (n - 1) * d) * r ** n + d * (r ** n - r) / (r - 1)) / (1 - r)

a = 2
b = 0.1

def f(guess): return s(guess) + 6e11

while abs(a - b) > 1e-15:
    c = (a + b) / 2

    if f(c) < 0:
        a = c
    else:
        b = c

print "%.13f %.13f" % (a, b)

print s(b)

