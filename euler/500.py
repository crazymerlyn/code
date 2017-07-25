from utils import primes
import heapq

ps = primes(10**7)

heapq.heapify(ps)

res = 1
for _ in range(500500):
    p = heapq.heappop(ps)
    res *= p
    res %= 500500507
    heapq.heappush(ps, p*p)

print res
