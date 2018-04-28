def f(n):
    res = 0
    while n:
        n //= 2
        res += n
    return res

n = 10 ** 12

l = n // 2
m = 904961 + 1

print(f(l) * m)
