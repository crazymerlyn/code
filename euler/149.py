SIZE = 2000

s = [0] * (SIZE * SIZE + 1)
for k in range(1, 56):
    s[k] = ((100003 - 200003 * k + 300007 * k * k * k) % 1000000) - 500000
for k in range(56, SIZE * SIZE + 1):
    s[k] = ((s[k-24] + s[k-55] + 1000000) % 1000000) - 500000

grid = [[s[r * SIZE + c + 1] for c in range(SIZE)] for r in range(SIZE)]

del s

best = 0
for r in range(SIZE):
    cur = 0
    for v in grid[r]:
        cur += v
        if cur > best: best = cur
        if cur < 0: cur = 0

for c in range(SIZE):
    cur = 0
    for r in range(SIZE):
        cur += grid[r][c]
        if cur > best: best = cur
        if cur < 0: cur = 0

for start in range(SIZE):
    cur = 0
    r, c = start, 0
    while r < SIZE and c < SIZE:
        cur += grid[r][c]
        if cur > best: best = cur
        if cur < 0: cur = 0
        r += 1
        c += 1

for start in range(1, SIZE):
    cur = 0
    r, c = 0, start
    while r < SIZE and c < SIZE:
        cur += grid[r][c]
        if cur > best: best = cur
        if cur < 0: cur = 0
        r += 1
        c += 1

for start in range(SIZE):
    cur = 0
    r, c = 0, start
    while r < SIZE and c >= 0:
        cur += grid[r][c]
        if cur > best: best = cur
        if cur < 0: cur = 0
        r += 1
        c -= 1

for start in range(1, SIZE):
    cur = 0
    r, c = start, SIZE - 1
    while r < SIZE and c >= 0:
        cur += grid[r][c]
        if cur > best: best = cur
        if cur < 0: cur = 0
        r += 1
        c -= 1

print(best)
