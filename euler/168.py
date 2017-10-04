n = 100

ans = 0

for x in range(1, 10):
    for last in range(1, 10):
        carry = 0
        next = last
        number = str(last)
        for _ in range(2, n+1):
            next = next * x + carry
            carry = next // 10
            next %= 10
            number = str(next) + number
            if next * x + carry == last and next:
                ans += int(number)
print ans % 100000


