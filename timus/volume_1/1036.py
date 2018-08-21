from collections import defaultdict

n, s = [int(x) for x in input().split()]

dp = {x: 1 for x in range(10)}

if s % 2 == 1:
    print(0)
else:
    s //= 2
    for i in range(2, n+1):
        newdp = defaultdict(int)
        for v in dp:
            for d in range(10):
                newdp[v + d] += dp[v]
        dp = newdp
    print(dp.get(s, 0) ** 2)
