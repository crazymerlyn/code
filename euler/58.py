import random

def isprime(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))

n = 3
sl = 2
c = 9
while 1.0*n/(2*sl+1) > 0.10:
    sl += 2
    for i in range(3):
        c += sl
        if isprime(c): n += 1
    c += sl

print sl+1

