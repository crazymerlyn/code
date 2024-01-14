limit = 10**14
n = int(limit ** 0.5)

vals = [i**2 for i in range(n+1)]

for i in range(1, n+1):
    for j in range(i*2, n+1, i):
        vals[j] -= vals[i]

print(sum(vals[i] * (limit//(i*i)) for i in range(1, n+1)) % (10 ** 9 + 7))

