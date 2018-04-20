from utils import factorize, chinese
from itertools import product

n = 91

def roots(n):
    res = []
    for i in range(n):
        if i ** 3 % n == 1:
            res.append(i)
    return res

rems = []
mods = []
for p, pow in factorize(n):
    rems.append(roots(p ** pow))
    mods.append(p ** pow)

ans = set()
for p in product(*rems):
    ans.add(chinese(list(p), mods))

print(sum(ans))
