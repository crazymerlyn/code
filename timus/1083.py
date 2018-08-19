n, xs = input().split()

res = 1

for i in range(int(n), 0, -len(xs)):
    res *= i

print(res)
