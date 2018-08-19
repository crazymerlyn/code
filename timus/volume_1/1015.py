from collections import defaultdict

def get_key(l):
    opp = {0: 1, 1: 0, 2: 4, 4: 2, 3: 5, 5: 3}
    front = {0: [3, 2, 5, 4], 1: [3, 4, 5, 2],
             2: [0, 3, 1, 5], 3: [2, 0, 4, 1],
             4: [0, 5, 1, 3], 5: [2, 1, 4, 0]}
    i = l.index(1)
    bottom = l[opp[i]]

    left = min(l[j] for j in range(6) if j not in (i, opp[i]))
    lefti = l.index(left)
    right = l[opp[lefti]]

    choices = front[i]
    k = choices.index(lefti)
    fronti = choices[(k + 1) % len(choices)]

    return (bottom, right, l[fronti])

res = defaultdict(list)
cat = {}
for index in range(1, int(input()) + 1):
    xs = [int(x) for x in input().split()]
    key = get_key(xs)
    if key not in res:
        cat[index] = key
    res[key].append(index)

print(len(res))
for k in sorted(cat):
    print(*res[cat[k]])
