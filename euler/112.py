def is_bouncy(n):
    last = n % 10
    n //= 10
    inc, dec = False, False
    while n:
        d = n % 10
        n //= 10
        if last > d:
            dec = True
        elif last < d:
            inc = True
        if inc and dec:
            return True
        last = d
    return inc and dec

count = 0
for n in xrange(1, 10**7):
    if is_bouncy(n): count += 1
    if count * 100 == 99 * n:
        print n
        break

