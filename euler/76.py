dp = [[0 for _ in range(101)] for _ in range(101)]

dp[0] = [1 for _ in range(101)]

for n in range(1, 101):
    dp[n][1] = 1
    for j in range(2, n+1):
        dp[n][j] = dp[n-j][j] + dp[n][j-1]
    for j in range(n+1, 101):
        dp[n][j] = dp[n][n]
print dp[100][100] -1
