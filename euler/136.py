from utils import primes

n = 5 * 10 ** 7

res = 2

ps = list(primes(n))[1:]

for p in ps:
    if p < n / 4: res += 1
    if p < n / 16: res += 1
    if p % 4 == 3: res += 1

print res

