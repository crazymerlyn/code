from collections import defaultdict
from utils import is_square

def generalize(s):
    mapping = {}
    cur = 0
    res = ""
    for d in s:
        if d in mapping:
            res += mapping[d]
        else:
            mapping[d] = str(cur)
            cur += 1
            res += mapping[d]
    return res

squares = defaultdict(list)

for n in range(1, 1000):
    x = n ** 2
    squares[generalize(str(x))].append(x)

words = defaultdict(list)

with open("./p098_words.txt") as f:
    for word in f.read().split(","):
        word = word[1:-1]
        words["".join(sorted(word))].append(word)

words = {k:l for k,l in words.items() if len(l) > 1}

res = 0
for word_chain in words.values():
    for a in word_chain:
        for b in word_chain:
            if a == b: continue
            if generalize(a) in squares:
                for n in squares[generalize(a)]:
                    if len(a) != len(str(n)): continue
                    mapping = {c:d for c,d in zip(a, str(n))}
                    m = int("".join(mapping[c] for c in b))
                    if is_square(m) and len(str(m)) == len(b):
                        res = max(res, n, m)

print res
