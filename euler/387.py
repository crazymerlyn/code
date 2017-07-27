from utils import is_prime2 as is_prime

limit = 10**14
def is_harshad(n):
    return n > 0 and n % sum(int(d) for d in str(n)) == 0

def sum_harshad_primes(n):
    s = sum(int(d) for d in str(n))
    assert n % s == 0
    res = 0
    for i in range(10):
        m = n * 10 + i
        if m > limit: break
        s2 = s + i
        if is_prime(m) and is_prime(n // s) and is_harshad(n // 10):
            res += m
        if m % s2 == 0:
            res += sum_harshad_primes(m)
    return res

res = 0
for i in range(1, 10):
    res += sum_harshad_primes(i)
print(res)

