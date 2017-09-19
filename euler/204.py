from utils import primes

ty = 100
limit = 10 ** 9

ps = list(primes(ty))
ns = [1]

res = set()
while ns:
    n = ns.pop()
    if n in res: continue
    res.add(n)
    for p in ps:
        x = n * p
        if x <= limit:
            ns.append(x)
print len(res)
