n, k = [int(x) for x in input().split()]

start = 1
steps = 0

while start < n and start <= k:
    start += start
    steps += 1

if start < n:
    steps += (n - start + k - 1) // k
print(steps)
