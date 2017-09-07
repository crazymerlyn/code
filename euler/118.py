from utils import is_prime2 as isprime

digits = set(range(1, 10))
cur = []

def count(n, cur):
    if not digits:
        return [cur + [n]] if isprime(n) and n > max(cur) else []
    res = []

    if isprime(n) and n > max(cur + [0]):
        res += count(0, cur + [n])


    for d in digits:
        digits.remove(d)
        rest = count(n * 10 + d, cur)
        res += rest

        digits.add(d)

    return res

res = count(0, [])

print res
