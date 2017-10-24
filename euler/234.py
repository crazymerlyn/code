from utils import primes
from math import ceil

def sum_div(low, high, n):
    low_i = int(ceil(float(low) / n))
    high_i = high / n

    return n * (high_i + low_i) * (high_i - low_i + 1) / 2

n = 999966663333

ps = list(primes(int(n ** 0.5) * 2))

res = 0

for i in range(len(ps) - 1):
    lps = ps[i]
    ups = ps[i + 1]

    if lps ** 2 > n: break

    # range is lps ** 2 + 1 , ups ** 2 - 1
    res += sum_div(lps ** 2 + 1, min(n, ups**2 - 1), lps)
    res += sum_div(lps ** 2 + 1, min(n, ups**2 - 1), ups)
    res -= 2*sum_div(lps ** 2 + 1, min(n, ups**2 - 1), lps * ups)

print res



