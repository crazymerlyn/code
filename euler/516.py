from utils import is_prime2 as isprime
from heapq import *

q = [2, 3, 5]
heapify(q)
limit = 10 ** 12

els = set([1])

while q:
    el = heappop(q)
    if el in els: continue
    els.add(el)
    if el * 2 <= limit:
        heappush(q, el * 2)
        if el * 3 <= limit:
            heappush(q, el * 3)
            if el * 5 <= limit:
                heappush(q, el * 5)
primes = []
for el in els:
    val = el + 1
    if 6 <= val <= limit and isprime(val):
        primes.append(val)

primes = sorted(primes)
choices = [1]
final = []
for prime in primes:
    newchoices = []
    for choice in choices:
        if choice * prime <= limit:
            newchoices.append(choice)
            newchoices.append(choice * prime)
        else:
            final.append(choice)
    choices = newchoices

choices = sorted(final + choices)

schoices = choices[:]
for i in range(1, len(schoices)):
    schoices[i] += schoices[i-1]

from bisect import bisect_right
res = 0
for el in sorted(els):
    i = bisect_right(choices, limit // el)
    res += el * schoices[i-1]
    res &= 0xffffffff
print(res)
