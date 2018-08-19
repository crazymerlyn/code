limit = 50
dp = [[0 for _ in range(limit)] for _ in range(501)]

for left in range(1, 501):
    dp[left][1] = 1
    for size in range(2, limit):
        for x in range(1, left):
            if left <= x * size: break
            dp[left][size] += dp[left - x * size][size-1]

n = int(input())
print(sum(dp[n]) - 1)
