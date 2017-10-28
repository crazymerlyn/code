from utils import lcm

def P(s, N):
    if s == 1:
        return (N - 1) / 2
    k = 1
    for i in range(1, s+1):
        k = lcm(k, i)

    l = lcm(k, s+1)

    res = 0
    for i in range(k + 1, N, k):
        if i % l != 1:
            res += 1

    return res

print sum(P(i, 4 ** i) for i in range(1, 32))

