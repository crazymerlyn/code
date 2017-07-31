x = 2*10**6
m = 0
res = None
for a in range(1, 200):
    for b in range(a, 200):
        r = a * b * (a+1) * (b+1) // 4
        if abs(r-x) < abs(m -x):
            m = r
            res = (a, b)
a, b = res
print(a*b)
