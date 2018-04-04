from random import uniform

def graph(n):
    adj = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            adj[i][j] = uniform(0, 1)
            adj[j][i] = adj[i][j]
    return adj

def mst(g):
    n = len(g) - 1
    dist = {}
    for adj in range(2, n+1):
        dist[adj] = g[1][adj]

    seen = set([1])

    res = 0
    for _ in range(n-1):
        res += min(dist.values())
        k = min(dist, key=lambda i: dist[i])
        del dist[k]
        seen.add(k)
        for adj in range(1, n+1):
            if adj not in seen:
                dist[adj] = min(dist[adj], g[k][adj])

    return res

print(mst(graph(1000)))
