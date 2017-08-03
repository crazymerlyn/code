from utils import primes, phi as totient

ps = primes(1000)

n = 1
phi = 1

for p in ps:
    n *= p
    phi *= p - 1
    if (n-1) * 15499 > 94744 * phi:
        break

max_p = p
n //= p

for i in range(2, max_p):
    m = n * i
    x = totient(m)
    if (m-1) * 15499 > 94744 * x:
        print m, x
        break

