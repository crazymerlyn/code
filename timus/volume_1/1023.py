n = int(input())

for i in range(3, int(n ** 0.5) + 1):
    if n % i == 0:
        print(i - 1)
        break
else:
    count = 0
    while n % 2 == 0:
        n //= 2
        count += 1
    if count > 1:
        print(3)
    else:
        print(n-1)
