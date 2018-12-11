n, m = [int(x) for x in input().split()]

k = int(input())
points = []
for _ in range(k):
    points.append([int(x) for x in input().split()])

graph = [[] for _ in range(k)]
revgraph = [[] for _ in range(k)]
for i, p1 in enumerate(points):
    for j, p2 in enumerate(points):
        if p2[0] > p1[0] and p2[1] > p1[1]:
            graph[i].append(j)
            revgraph[j].append(i)

zeros = []
score = [1] * k
tscore = [1] * k
for i in range(k):
    if not graph[i]: zeros.append(i)
    score[i] = len(graph[i])

res = 0
while zeros:
    node = zeros.pop()
    if graph[node]:
        tscore[node] = max(tscore[adj] for adj in graph[node]) + 1
    res = max(res, tscore[node])
    for adj in revgraph[node]:
        score[adj] -= 1
        if score[adj] == 0: zeros.append(adj)

print(round(100 * (n + m - res * 2 + res * 2 ** 0.5)))

