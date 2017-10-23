def combinations(n, s):
    if len(s) == 2 ** n:
        for i in range(1, n):
            if (s[-i:] + s)[:n] in s:
                return []
        return [s]
    res = []
    for i in ("0", "1"):
        if s[-n+1:] + i not in s:
            res.extend(combinations(n, s + i))
    return res

print sum(int(x, 2) for x in combinations(5, "00000"))
