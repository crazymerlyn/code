n = int(input())
graph = [[] for _ in range(n+1)]

for i in range(1, n+1):
    graph[i] = [int(x) for x in input().split()[:-1]]

group = [-1 for _ in range(n+1)]
for i in range(n+1):
    if group[i] != -1: continue
    q = [i]
    group[i] = 0
    count = 1
    while q:
        node = q.pop(0)
        count += 1
        for child in graph[node]:
            if group[child] != -1: continue
            group[child] = 1 - group[node]
            q.append(child)
    if count == 1:
        print(0)
        exit()

team1 = [i for i in range(1, n+1) if group[i] == 1]
print(len(team1))
print(*team1)

