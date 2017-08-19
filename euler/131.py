from utils import primes

ps = set(primes(10**6))

count = 0
for a in range(1, 10000):
    b = a + 1
    p = b ** 3 - a ** 3
    if p > 10**6: break
    if p in ps:
        count += 1

print count
