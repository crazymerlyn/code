from collections import defaultdict

count = defaultdict(int)

limit = 10**12

for b in range(2, int(limit**0.5)+1):
    for p in range(3, 50):
        res = (b ** p - 1) / (b - 1)
        if res > limit: break
        count[res] += 1

print sum(v for v in count) + 1

