n = int(input())
res = []
for _ in range(n):
    res.append(int(input()))

res.sort()
input()
for _ in range(int(input())):
    print(res[int(input())-1])
