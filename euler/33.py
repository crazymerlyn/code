from math import gcd

num = 1
den = 1
for a in range(10, 100):
    for b in range(a + 1, 100):
        if a % 10 == 0 and b % 10 == 0:
            continue
        s = str(a)
        t = str(b)
        if s[0] == t[1] and s[1] != '0':
            if int(s[1]) * b == int(t[0]) * a:
                num *= a
                den *= b
        if s[1] == t[0] and t[0] != '0':
            if int(s[0]) * b == int(t[1]) * a:
                num *= a
                den *= b
print(den // gcd(num, den))
