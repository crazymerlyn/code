count = 0
for i in range(1, 10):
    for j in range(1, 100):
        if 10 ** (j-1) <= i ** j < 10 ** j:
            count += 1
print count
