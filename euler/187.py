LIMIT = 10**8
# Sieve primes up to LIMIT // 2
n = LIMIT // 2
sieve = bytearray(b'\x01') * (n + 1)
sieve[0:2] = b'\x00\x00'
for i in range(2, int(n**0.5) + 1):
    if sieve[i]:
        sieve[i*i:n+1:i] = b'\x00' * ((n - i*i)//i + 1)

primes = [i for i, v in enumerate(sieve) if v]
count = 0
j = len(primes) - 1
for i, p in enumerate(primes):
    while j >= i and p * primes[j] >= LIMIT:
        j -= 1
    if j < i:
        break
    count += j - i + 1
print(count)
