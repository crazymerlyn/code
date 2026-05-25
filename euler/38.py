best = 0
for n in range(1, 10000):
    s = ''
    k = 1
    while len(s) < 9:
        s += str(n * k)
        k += 1
    if len(s) == 9 and len(set(s)) == 9 and '0' not in s:
        best = max(best, int(s))
print(best)
