res = 0
for a in range(3, 1001):
    m = 2
    for n in range(1, a+1):
        m = max(m, 2*n*a % (a*a))
    res += m
print res
