k = int(input())

def primes(limit):
    if limit >= 2:
        yield 2

    import array
    from math import sqrt
    isprime = array.array("B", b"\x01" * ((limit - 1) // 2))
    sieveend = sqrt(limit)
    for i in range(len(isprime)):
        if isprime[i] == 1:
            p = i * 2 + 3
            yield p
            if i <= sieveend:
                for j in range((p * p - 3) >> 1, len(isprime), p):
                    isprime[j] = 0

ps = list(primes(2 * 10 ** 5))
for _ in range(k):
    n = int(input())
    print(ps[n-1])
