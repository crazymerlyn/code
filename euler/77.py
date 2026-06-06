def primes_upto(n):
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i*i:n+1:i] = [False] * ((n - i*i)//i + 1)
    return [i for i, p in enumerate(sieve) if p]

primes = primes_upto(1000)
LIMIT = 5000
ways = [0] * (LIMIT + 1)
ways[0] = 1
for p in primes:
    for i in range(p, LIMIT + 1):
        ways[i] += ways[i - p]
for n in range(2, LIMIT + 1):
    if ways[n] > 5000:
        print(n)
        break
