from utils import is_square

pos = 15
res = []

for l in range(900000):
    for add in (2, 4):
        k = (l + (5 * l * l + add) ** 0.5) / 2.0
        n = k * l
        if n % 1 == 0: res.append(int(n))

    if l > 0:
        for sub in (1, 2):
            k = 2*l + (5 * l * l - sub) ** 0.5
            n = k * l
            if n % 1 == 0: res.append(int(n))

res = [n for n in sorted(set(res)) if is_square((n+1)**2 + 4*n**2)]

print res[pos]

