def hyperexp(a, b, m):
    res = 1
    for _ in range(b):
        res = pow(a, res, m)
    return res

print hyperexp(1777, 1885, 10**8)
