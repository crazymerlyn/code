from itertools import product
def next_iter(s):
    return s[1:] + (s[0] ^ (s[1] & s[2]),)

lengths = []

seen = set()
for var in product(range(2), repeat=6):
    var = tuple(var)
    if var in seen: continue
    seen.add(var)
    n = next_iter(var)
    seen.add(n)
    res = 1
    while n != var:
        n = next_iter(n)
        seen.add(n)
        res += 1
    lengths.append(res)

print(lengths)
def func(l):
    a, b = 2, 1
    for _ in range(l):
        a, b = b, a + b
    return a

res = 1
for length in lengths:
    res *= func(length)

print(res)

