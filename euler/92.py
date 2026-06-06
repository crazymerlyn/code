LIMIT = 10000000

def sq_sum(n):
    s = 0
    while n:
        s += (n % 10) ** 2
        n //= 10
    return s

ends = {1: 1, 89: 89}
count = 0

for n in range(1, LIMIT):
    chain = []
    x = n
    while x not in ends:
        chain.append(x)
        x = sq_sum(x)
    end = ends[x]
    for c in chain:
        ends[c] = end
    if end == 89:
        count += 1

print(count)
