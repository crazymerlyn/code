res = 0
with open("./oes46655.txt") as f:
    for line in f:
        a, b = line.strip().split()
        b = int(b)
        if b > 64 * 10 ** 6:
            break
        res += b
print res
