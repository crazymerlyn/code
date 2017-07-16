n, m = map(int, raw_input().split())

a, b = 0, 1

prev = {}

for i in range(n):
    a, b = b, a + b - (prev[i-m] if i > m else 1 if i > m-2 else 0)
    prev[i] = a

print a

