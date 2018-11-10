def a(start, end):
    if start == end: return "sin(%d)" % start
    return "sin(%d%s%s)" % (start, '-' if start % 2 else '+', a(start + 1, end))

def s(start, end):
    if start == end:
        return "%s+%s" % (a(1, 1), end)
    return "(%s)%s+%d" % (s(start + 1, end), a(1, end - start + 1), start)

n = int(input())
print(s(1, n))
