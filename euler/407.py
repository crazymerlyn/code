from utils import factorize, modinv
from itertools import product

def M(n):
    fs = [p ** pp for p, pp in factorize(n)]

    f2 = [n // f * modinv(n // f, f) % n for f in fs]

    ans = 0
    for i in range(2 ** len(fs)):
        cur = sum(f2[j] for j in range(len(fs)) if i & (1 << j))
        ans = max(ans, cur % n)

    return ans

limit = 10 ** 7 + 1

res = 0
for n in range(1, limit):
    res += M(n)

print(res)

