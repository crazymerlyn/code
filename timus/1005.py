n = int(input())

xs = [int(x) for x in input().split()]

sums = set([0])
for x in xs:
    newsums = set(sums)
    for y in sums:
        newsums.add(y + x)
    sums = newsums

total = sum(xs)
result =  min(abs(total - x * 2) for x in sums)

print(result)
