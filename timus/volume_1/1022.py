n = int(input())
graph = [[] for _ in range(n+1)]
count = [0 for _ in range(n+1)]
zeroes = []

for i in range(1, n+1):
    vs = [int(x) for x in input().split()][:-1]
    count[i] = len(vs)
    if count[i] == 0:
        zeroes.append(i)
    for v in vs:
        graph[v].append(i)

res = []
while zeroes:
    node = zeroes.pop()
    res.append(node)
    for child in graph[node]:
        count[child] -= 1
        if count[child] == 0:
            zeroes.append(child)

print(*res[::-1])
