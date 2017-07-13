n, k = map(int, raw_input().split())

a, b = 0, 1

for i in range(n):
    a, b = b, b + k*a

print a

