from utils import is_prime as isprime
limit = 2000
count = 1
n = 1

while True:
    if isprime(6*n-1) and isprime(6*n+1) and isprime(12 * n + 5):
        count += 1
        if count == limit:
            print 3 * n*n - 3 * n + 2
            break
    if n>1 and isprime(6*n - 1) and isprime(6 * n + 5) and isprime(12*n-7):
        count += 1
        if count == limit:
            print 3 * n*n + 3*n + 1
            break
    n += 1


