def digit4(ns):
    return [n for n in ns if 1000 <= n <= 9999]

def polygons(n):
    return [(1, n*(n+1)//2), (2, n*n), (3, n*(3*n-1)//2), (4, n*(2*n-1)), (5, n*(5*n-3)//2), (6, n*(3*n-2))]

ps = []
for n in range(1, 200):
    for tag, value in polygons(n):
        if 1000 <= value <= 9999:
            ps.append((tag, value))

from collections import defaultdict
adjacent = defaultdict(list)

for tag1, value1 in ps:
    for tag2, value2 in ps:
        if tag1 != tag2 and value1 % 100 == value2 // 100:
            adjacent[(tag1, value1)].append((tag2, value2))

to_visit = [[polygon] for polygon in ps]

while to_visit:
    chain = to_visit.pop()
    if len(chain) == 6 and chain[0][1] // 100 == chain[-1][1] % 100:
        print(sum(value for tag, value in chain))
        break
    tags_seen = [tag for tag, _ in chain]
    for tag, value in adjacent[chain[-1]]:
        if tag not in tags_seen and chain[-1][1] % 100 == value // 100:
            newchain = chain + [(tag, value)]
            to_visit.append(newchain)

