def f(n):
    if n < 3: return 1
    if n % 10 == 0:
        return f(n//10)
    if n % 10 == 5:
        return 2 * f(n//5)
    seen = set()
    queue = [1, 2]
    i = 0
    while queue:
        t = queue[i]
        i += 1
        r = t % n

        if r == 0:
            return t // n

        if r not in seen:
            seen.add(r)
            queue.append(t * 10)
            queue.append(t * 10 + 1)
            queue.append(t * 10 + 2)

    return "Not Possible"

limit = 10000
res = 0
for n in range(1, limit+1):
    res += f(n)
print res

