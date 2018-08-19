n = int(input())

sqs = set(x ** 2 for x in range(250))
pairs = set(x + y for x in sqs for y in sqs)

if n in sqs:
    print(1)
elif n in pairs:
    print(2)
else:
    for s in sqs:
        if n - s in pairs:
            print(3)
            break
    else:
        print(4)
