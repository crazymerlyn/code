SIZE = 1000000
TARGET = 990000
PM = 524287

def lfg():
    buf = [0] * 55
    for k in range(1, 56):
        buf[k-1] = (100003 - 200003 * k + 300007 * k * k * k) % SIZE
    ptr = 0
    while True:
        yield buf[ptr]
        nxt = (buf[(ptr + 31) % 55] + buf[ptr]) % SIZE
        buf[ptr] = nxt
        ptr = (ptr + 1) % 55

parent = list(range(SIZE))
sz = [1] * SIZE

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return
    if sz[ra] < sz[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    sz[ra] += sz[rb]

gen = lfg()
calls = 0
while True:
    caller = next(gen)
    callee = next(gen)
    if caller == callee:
        continue
    calls += 1
    union(caller, callee)
    if sz[find(PM)] >= TARGET:
        print(calls)
        break
