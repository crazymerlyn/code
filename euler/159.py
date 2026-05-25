def dr(n):
    return 1 + (n - 1) % 9

N = 1000000
mdrs = [0] * N
for i in range(2, N):
    mdrs[i] = dr(i)

for a in range(2, N):
    da = dr(a)
    for n in range(2 * a, N, a):
        b = n // a
        cand = da + mdrs[b]
        if cand > mdrs[n]:
            mdrs[n] = cand

print(sum(mdrs))
