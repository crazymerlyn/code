from collections import defaultdict

n = int(input())

graph = defaultdict(set)

for _ in range(n):
    names = input().split()
    for name in names:
        for name2 in names:
            if name != name2: graph[name].add(name2)

s = "Isenbaev"
dist = {s: 0}

q = [s]
while q:
    name = q.pop(0)
    if name not in graph: continue
    for adj in graph[name]:
        if adj in dist: continue
        dist[adj] = dist[name] + 1
        q.append(adj)

for name in sorted(graph):
    print(name, dist[name] if name in dist else "undefined")
