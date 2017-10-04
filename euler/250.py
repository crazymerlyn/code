lim = 250250
mod = 10 ** 16

ar = []
for i in xrange(1, lim + 1):
    ar.append(pow(i, i, 250))


dp = [0 for _ in range(250)]
dp[0] = 1
current = 0

for rem in ar:
    current = (current + rem) % 250
    dp = [(a + b) % mod for a, b in zip(dp, dp[-rem:]+dp)]

print dp[0]

