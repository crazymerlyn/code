def term(n):
    res = 0
    a = 1
    for i in range(11):
        res += a
        a *= -n
    return res

def extrapolate(seq):
    if len(seq) == 1:
        return seq[0]
    return seq[-1] + extrapolate([y - x for x, y in zip(seq, seq[1:])])

seq = [term(i) for i in range(1, 12)]

res = 0

for k in range(1, 11):
    terms = seq[:k]
    res += extrapolate(terms)

print res

