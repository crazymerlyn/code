from collections import defaultdict

n = 40

ns = {(i, 1 << i): 1 for i in range(1, 10)}

res = 0

for d in range(1, n):
    newns = defaultdict(int)
    for (digit, digits), val in ns.items():
        if digit > 0:
            newns[(digit - 1, digits | (1 << (digit - 1)))] += val
        if digit < 9:
            newns[(digit + 1, digits | (1 << (digit + 1)))] += val
    ns = newns
    for (digit, digits), val in ns.items():
        if digits == 0b1111111111:
            res += val

print res
