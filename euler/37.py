def primes(n):
    is_prime = [True] * (n + 1)
    ps = []
    for i in range(2, n + 1):
        if is_prime[i]:
            ps.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return set(ps)

ps = primes(1000000)
total = 0
for p in ps:
    if p < 10:
        continue
    s = str(p)
    ok = True
    for i in range(1, len(s)):
        if int(s[i:]) not in ps or int(s[:i]) not in ps:
            ok = False
            break
    if ok:
        total += p
print(total)
