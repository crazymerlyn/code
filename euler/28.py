total = 1
n = 1
step = 2
while step <= 1000:
    for _ in range(4):
        n += step
        total += n
    step += 2
print(total)
