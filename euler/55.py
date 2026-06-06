def is_lychrel(n, limit=50):
    for _ in range(limit):
        s = str(n)
        if s == s[::-1] and _ > 0:
            return False
        n += int(s[::-1])
    return True

print(sum(1 for n in range(1, 10000) if is_lychrel(n)))
