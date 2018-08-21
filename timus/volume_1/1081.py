dp = [1, 2, 3]
for _ in range(44):
    dp.append(dp[-1] + dp[-2])

def calc(n, k):
    if k > dp[n]: return -1
    if n == 0: return ""
    if n == 1: return '01'[k-1]
    if k <= dp[n-1]: return '0' + calc(n-1, k)
    return '10' + calc(n-2, k - dp[n-1])

n, k = [int(x) for x in input().split()]
print(calc(n, k))
