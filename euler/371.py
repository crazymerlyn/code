dp = [0. for _ in range(500)]
dp2 = [0. for _ in range(500)]

dp[-1] = 2.
dp2[-1] = 2.004

for k in range(498, -1, -1):
    dp[k] = (1000 + (1000 - 2*k - 2) * dp[k+1]) / (1000. - k - 1)
    dp2[k] = (1000 + (1000 - 2*k - 2) * dp2[k+1] + dp[k]) / (1000. - k - 1)

print(dp2[0])
