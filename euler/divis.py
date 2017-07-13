from itertools import permutations

def mint(ar):
    res = 0
    for d in ar:
        res = res * 10 + d
    return res

res = 0
for p in permutations(range(10)):
    p = list(p)
    if p[0] == 0: continue
    if p[3] % 2: continue
    if sum(p[2:5]) % 3: continue
    if p[5] % 5: continue
    if mint(p[4:7]) % 7: continue
    if (p[5] + p[7] - p[6]) % 11: continue
    if mint(p[6:9]) % 13: continue
    if mint(p[7:]) % 17: continue
    res += mint(p)

print res
