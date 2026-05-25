from math import gcd

p, q = 1009, 3643
phi = (p - 1) * (q - 1)

best = None
total = 0

for e in range(2, phi):
    if gcd(e, phi) != 1:
        continue
    g1 = gcd(e - 1, p - 1)
    g2 = gcd(e - 1, q - 1)
    v = (1 + g1) * (1 + g2)
    if best is None or v < best:
        best = v
        total = e
    elif v == best:
        total += e

print(total)
