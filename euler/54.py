values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
}

def hand_rank(cards):
    ranks = sorted([values[c[0]] for c in cards], reverse=True)
    suits = [c[1] for c in cards]
    flush = len(set(suits)) == 1
    straight = False
    if ranks == [14, 13, 12, 11, 10]:
        straight = True
    elif ranks[0] - ranks[4] == 4 and len(set(ranks)) == 5:
        straight = True
    elif ranks == [14, 5, 4, 3, 2]:
        straight = True
        ranks = [5, 4, 3, 2, 1]

    counts = {}
    for r in ranks:
        counts[r] = counts.get(r, 0) + 1
    groups = sorted(counts.values(), reverse=True)

    if straight and flush:
        return (9, ranks)
    if groups[0] == 4:
        four = [r for r, c in counts.items() if c == 4][0]
        kicker = [r for r in ranks if r != four][0]
        return (8, [four], [kicker])
    if groups[0] == 3 and groups[1] == 2:
        three = [r for r, c in counts.items() if c == 3][0]
        pair = [r for r, c in counts.items() if c == 2][0]
        return (7, [three], [pair])
    if flush:
        return (6, ranks)
    if straight:
        return (5, ranks)
    if groups[0] == 3:
        three = [r for r, c in counts.items() if c == 3][0]
        kickers = sorted([r for r in ranks if r != three], reverse=True)
        return (4, [three], kickers)
    if groups[0] == 2 and groups[1] == 2:
        pairs = sorted([r for r, c in counts.items() if c == 2], reverse=True)
        kicker = [r for r in ranks if r not in pairs][0]
        return (3, pairs, [kicker])
    if groups[0] == 2:
        pair = [r for r, c in counts.items() if c == 2][0]
        kickers = sorted([r for r in ranks if r != pair], reverse=True)
        return (2, [pair], kickers)
    return (1, ranks)

with open('p054_poker.txt') as f:
    total = 0
    for line in f:
        cards = line.strip().split()
        p1 = hand_rank(cards[:5])
        p2 = hand_rank(cards[5:])
        if p1 > p2:
            total += 1
print(total)
