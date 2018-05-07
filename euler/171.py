n = 20
limit = 81 * n
dp = [[0 for _ in range(limit+1)] for _ in range(21)]
dp2 = [[0 for _ in range(limit+1)] for _ in range(21)]

for i in range(1, 10): dp[1][i*i] = 1
for i in range(1, 10): dp2[1][i*i] = i

for i in range(2, n+1):
    for j in range(1,limit+1):
        if not dp[i-1][j]: continue
        for k in range(10):
            dp[i][j + k * k] += dp[i-1][j]
            dp2[i][j + k * k] += dp2[i-1][j]*10 + dp[i-1][j] * k
res = 0
for i in range(1, 100):
    if i * i > limit: break
    res += sum(dp2[j][i*i] for j in range(1, n+1))
print(res%10**9)
