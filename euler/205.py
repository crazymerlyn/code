from itertools import product

colin = [0 for _ in range(37)]
peter = [0 for _ in range(37)]
for choice in product([1, 2, 3, 4], repeat=9):
    peter[sum(choice)] += 1

for choice in product(range(1, 7), repeat=6):
    colin[sum(choice)] += 1

res = 0

for i in range(6, 37):
    for j in range(i+1, 37):
        res += colin[i] * peter[j]

print(1.0 * res / 4**9 / 6**6)

