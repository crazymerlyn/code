count = 0
for n in range(1, 100):
    for k in range(1, 100):
        if len(str(n**k)) == k:
            count += 1
        elif len(str(n**k)) < k:
            break
print(count)
