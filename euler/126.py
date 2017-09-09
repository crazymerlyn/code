limit = 2 * 10 ** 4

count = [0 for _ in range(limit)]

for a in range(1, 6000):
    for b in range(1, a+1):
        if a * b + a + b > limit: break
        for c in range(1, b+1):
            start = 2 * (a * b + b * c + c * a)
            step  = 4 * (a + b + c)
            if start > limit: break
            while start < limit:
                count[start] += 1
                start += step
                step += 8
for k in range(1, limit):
    if count[k] == 1000:
        print k
        break

