from collections import defaultdict

n = int(input())

n //= 2

count = defaultdict(int)
for i in range(10 ** n):
    count[sum(int(d) for d in str(i))] += 1

print(sum(v ** 2 for v in count.values()))

