limit = 10 ** 6

sumdiv = [0]*(limit+1)
for i in xrange(1, limit+1):
    for j in xrange(2*i, limit+1, i):
        sumdiv[j] += i

chain_length = [0] * (limit+1)
chain_length[0] = -1
chain_length[1] = -1

for i in xrange(2, limit+1):
    if chain_length[i]: continue
    chain = [i]
    i = sumdiv[i]
    while i not in chain and i <= limit and chain_length[i] == 0:
        chain.append(i)
        i = sumdiv[i]
    if i in chain:
        id = chain.index(i)
        for j in chain[:id]: chain_length[j] = -1
        for j in chain[id:]: chain_length[j] = len(chain) - id - 1
    else:
        for j in chain: chain_length[j] = -1
print chain_length.index(max(chain_length))
