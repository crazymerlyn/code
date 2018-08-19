from fractions import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

n = int(input())
ps = [int(x) for x in input().split()]
done = [False] * n

res = 1

for i in range(n):
    q = i
    length = 1
    if done[i]: continue
    done[i] = True
    while ps[q] != i + 1:
        q = ps[q] - 1
        length += 1
        done[q] = True
    res = lcm(res, length)

print(res)
