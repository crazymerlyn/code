def f(a, c, k):
    return 4 * k * a - (3 * k + 1) * c

a = 21 ** 7
b = 7 ** 21
c = 12 ** 7

from math  import ceil
res = b * (b + 1) // 2
n = b // a
left = b % a
res += (2 * n * (n + 1) * a - (3 * n * (n + 1) // 2 + n) * c) * a
res += f(a, c, n+1) * (left + 1)
print(res % 10 ** 9)
