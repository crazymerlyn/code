from collections import defaultdict

states = {(0, 0) : 1}

n = 30

for i in range(n):
    newstates = defaultdict(int)
    for k, v in states.items():
        late, absents = k
        if not late:
            newstates[(1, 0)] += v
        if absents < 2:
            newstates[(late, absents + 1)] += v

        newstates[(late, 0)] += v
    states = newstates

print sum(states.values())
