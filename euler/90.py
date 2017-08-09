from itertools import combinations

def helper(a):
    res = set(a)
    if 6 in res or 9 in res:
        res |= set([6, 9])
    return res

res = 0
for da in combinations(range(10), 6):
    for db in combinations(range(10), 6):
        d1 = helper(da)
        d2 = helper(db)

        for i in range(1, 10):
            n = i * i
            if not ((n%10 in d1 and n//10 in d2) or (n%10 in d2 and n//10 in d1)):
                break
        else:
            res += 1
print res // 2

