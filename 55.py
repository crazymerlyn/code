def lychrel(n):
    for i in range(52):
        n = int(str(n)[::-1]) + n
        if str(n) == str(n)[::-1]:
            return False
    return True

print sum(1 for x in range(1, 10001) if lychrel(x))

