def memoized(func):
    cache = {}
    def newfunc(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return newfunc

@memoized
def sum_factorial_digits(n):
    factorial = {
        0: 1,
        1: 1,
        2: 2,
        3: 6,
        4: 24,
        5: 120,
        6: 720,
        7: 5040,
        8: 40320,
        9: 362880
    }
    if n in factorial: return factorial[n]
    res = 0
    while n:
        res += factorial[n % 10]
        n //= 10
    return res

res = 0
for i in xrange(1, 10**6):
    chain = set([i])
    i = sum_factorial_digits(i)
    while i not in chain:
        chain.add(i)
        i = sum_factorial_digits(i)
    if len(chain) == 60:
        res += 1

print(res)
