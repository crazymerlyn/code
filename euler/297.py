def fib(n):
    a, b = 1, 2
    while a < n:
        yield a
        a, b = b, a + b
fibs = list(fib(10**21))

res = {}
res[1] = 1
res[2] = 2

for i in range(1, len(fibs)-1):
    a = fibs[i]
    b = fibs[i+1]
    res[b] = res[a] + res[b-a] - 1 + b - a

def func(n):
    if n in res: return res[n]
    i = 0
    while fibs[i+1] <= n:
        i += 1
    return res[fibs[i]] + func(n - fibs[i]) + n - fibs[i]

print(func(10 ** 17-1))
