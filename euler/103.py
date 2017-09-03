from itertools import product

def subsetsums(a):
    res = []
    n = 2 ** len(a)
    for i in range(n):
        res.append(sum(x for j, x in enumerate(a) if i & (2 ** j)))

    return res

def condition2(a):
    a = sorted(a)
    for i in range(2, len(a)):
        if sum(a[:i]) < sum(a[-i+1:]):
            return False
    return True

seed = [11, 18, 19, 20, 22, 25]
seed = [seed[3]] + [x + seed[3] for x in seed]

res = seed[:]

for diff in product(range(-3, 4), repeat=len(seed)):
    test = [x + y for x, y in zip(seed, diff)]
    if len(set(test)) != len(test) or sorted(test) != test:
        continue
    if sum(test) > sum(seed):
        continue
    s = subsetsums(test)
    if len(set(s)) == len(s) and condition2(test):
        res = test
print "".join(map(str, res))

