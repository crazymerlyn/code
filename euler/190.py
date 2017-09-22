def f(m, n):
    if n == 1: return m
    term =  2.0 * m / (n + 1)

    return term ** n * f(m - term, n - 1)

print sum(int(f(n, n)) for n in range(2, 16))

