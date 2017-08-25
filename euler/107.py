with open("./p107_network.txt") as f:
    adj = []
    for line in f.readlines():
        adj.append({i: int(x) for i, x in enumerate(line.strip().split(",")) if x.isdigit()})

res = 0
v = 0

seen = set([v])
possib = []

for _ in range(len(adj) - 1):
    for next_v in  adj[v]:
        possib.append((v, next_v))
    possib = [(a, b) for a, b in possib if b not in seen]

    i, j = min(possib, key=lambda x:adj[x[0]][x[1]])
    v = j
    seen.add(j)
    res += adj[i][j]

print sum(sum(l.values()) for l in adj)/2 - res

