from itertools import cycle

def keys():
    for i in range(26):
        for j in range(26):
            for  k in range(26):
                yield [i + 97, j + 97, k + 97]

def score(text):
    return sum(chr(c).isalnum() or chr(c).isspace() for c in text)

def xor(key, text):
    for a, b in zip(cycle(key), text):
        yield a ^ b

with open("cipher.txt") as f:
    codes = map(int, f.read().split(","))

    texts = [list(xor(key, codes)) for key in keys()]

    text = max(texts, key=score)

    print sum(text)

