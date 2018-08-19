n = int(input())
xs = set()
for _ in range(n):
    xs.add(int(input()))

for _ in range(int(input())):
    val = int(input())
    if 10000 - val in xs:
        print("YES")
        break
else:
    print("NO")
