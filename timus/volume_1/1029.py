m, n = [int(x) for x in input().split()]

graph = []
for _ in range(m):
    graph.append([int(x) for x in input().split()])

dp = [[float('inf') for _ in range(n)] for _ in range(m)]

dp[0] = graph[0]

for i in range(1, m):
    dp[i] = [x + y for x, y in zip(dp[i-1], graph[i])]
    for j in range(1, n):
        dp[i][j] = min(dp[i][j], dp[i][j-1] + graph[i][j])
    for j in range(n-2, -1, -1):
        dp[i][j] = min(dp[i][j], dp[i][j+1] + graph[i][j])

res = [(m-1, min(range(n), key=lambda j: dp[-1][j]))]

while res[-1][0] != 0:
    floor, room = res[-1]
    choices = [(floor - 1, room)]
    if room > 0: choices.append((floor, room-1))
    if room < n - 1: choices.append((floor, room+1))
    res.append(min(choices, key=lambda x: dp[x[0]][x[1]]))

print(*[room + 1 for floor, room in res[::-1]])
