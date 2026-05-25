B, W = 60, 40
dp = [[0] * (W + 1) for _ in range(B + 1)]
dp[0][0] = 1

for i in range(B + 1):
    for j in range(W + 1):
        if i == 0 and j == 0:
            continue
        for b in range(i, B + 1):
            for w in range(j, W + 1):
                dp[b][w] += dp[b - i][w - j]

print(dp[B][W])
