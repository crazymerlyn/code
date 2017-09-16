seed = [(0, -1), (0, 1), (-3, -2), (-3, 2), (-4, -5), (-4, 5), (2, -7), (2, 7)]

count = 30

res = 0
seen = set()

i = 0
while True:
    k, b = seed[i]
    i += 1
    knew = -  9 * k - 4 * b - 14
    bnew = - 20 * k - 9 * b - 28

    seed.append((knew, bnew))

    if (knew > 0 and knew not in seen):
        res += knew
        seen.add(knew)
        count -= 1
        if count == 0:
            break

print res
