from itertools import combinations
from collections import Counter
from math import factorial

def div11(ns):
    s = sum(ns)
    res = 0
    seen = set()
    for comb in combinations(ns, len(ns) // 2):
        comb = tuple(sorted(comb))
        if comb not in seen:
            seen.add(comb)
        else:
            continue
        if (s - sum(comb) * 2) % 11 == 0:
            cur = factorial(len(ns) // 2)
            for _, v in Counter(comb).items():
                cur //= factorial(v)
            cur2 = factorial(len(ns) - len(ns) // 2)
            for _, v in (Counter(ns) - Counter(comb)).items():
                cur2 //= factorial(v)
            res += cur * cur2
    return res

print(div11(range(10) * 2) - div11(range(10) + range(1, 10)))
