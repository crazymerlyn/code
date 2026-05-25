from itertools import permutations

def solve():
    nums = list(range(1, 11))
    best = ''
    for p in permutations(nums):
        groups = [(p[0], p[1], p[2]),
                  (p[3], p[2], p[4]),
                  (p[5], p[4], p[6]),
                  (p[7], p[6], p[8]),
                  (p[9], p[8], p[1])]
        s = sum(groups[0])
        if all(sum(g) == s for g in groups):
            outer = [g[0] for g in groups]
            if min(outer) == outer[0]:
                s = ''.join(str(x) for g in groups for x in g)
                if len(s) == 16 and s > best:
                    best = s
    print(best)

solve()
