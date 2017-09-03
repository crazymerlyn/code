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

res = 0

with open("./p105_sets.txt") as f:
    for line in f.readlines():
        a = [int(x) for x in line.strip().split(",")]
        s = subsetsums(a)
        if len(set(s)) == len(s) and condition2(a):
            res += sum(a)
print res

