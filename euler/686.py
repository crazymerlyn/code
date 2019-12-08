from math import log, exp

def mantissa(x):
    l = log(x, 10)
    return l - int(l)

def between(x, a, b):
    x -= int(x)
    return a <= x < b

def p(pref, n):
    a, b = mantissa(pref), mantissa(pref+1)
    start = log(2, 10)
    count = 0

    for i in range(n):
        val = i + b
        fac = int(val / start)
        if between(start*fac, a, b):
            count += 1
            if count == 678910:
                print(count, fac)

p(123, 60000000)
