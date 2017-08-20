from utils import factorize, phi

limit = 10 ** 6

for n in range(limit+1, 2*limit):
    if n % 2 == 0 or n % 5 == 0: continue
    a = phi(9*n)
    if a <= limit: continue
    valid = True
    for i in range(2, int(a**0.5)+1):
        if a % i: continue
        if pow(10, i, 9*n) == 1 and i <= limit:
            valid = False
        f = a // i
        if pow(10, f, 9*n) == 1 and f <= limit:
            valid = False

    if valid:
        print n
        break


