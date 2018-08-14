n = int(input())
k = int(input())

res = [[0, 0] for _ in range(n)]
res[0] = [k-1, 0]

for i in range(1, n):
    res[i][0] = (k-1) * sum(res[i-1])
    res[i][1] = res[i-1][0]

print(sum(res[-1]))
