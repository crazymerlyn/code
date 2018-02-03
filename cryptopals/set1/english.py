from string import ascii_lowercase as ascii_lower

order = "eariotnslcudpmhgbfywkvxzjq";
ranks = {c: order.index(c) for c in ascii_lower}

def score(s):
    from collections import Counter

    if any(ord(c) < 10 for c in s):
        return 0

    freqs =  Counter(s.lower())
    for c in ascii_lower:
        if c not in freqs:
            freqs[c] = 0

    s_order = [c for c, f in freqs.most_common()]
    s_ranks = {c: s_order.index(c) for c in ascii_lower}

    s = 6 * sum((s_ranks[c] - ranks[c])**2 for c in ascii_lower)
    s /= 26 ** 3 - 26.0
    s = 1.0 - s

    return s

