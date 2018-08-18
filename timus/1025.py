n = int(input())
xs = [int(x) for x in input().split()]
xs.sort()

print(sum(x // 2 + 1 for x in xs[:len(xs) // 2+1]))
