def solve():
    cache = {1: 1}
    def chain(n):
        if n not in cache:
            cache[n] = 1 + chain(3 * n + 1 if n % 2 else n // 2)
        return cache[n]
    max_len, best = 0, 0
    for i in range(1, 1000000):
        l = chain(i)
        if l > max_len:
            max_len, best = l, i
    print(best)

solve()
