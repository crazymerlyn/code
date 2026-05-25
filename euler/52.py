n = 1
while True:
    s = sorted(str(n))
    if all(sorted(str(n * k)) == s for k in range(2, 7)):
        print(n)
        break
    n += 1
