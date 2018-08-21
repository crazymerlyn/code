n, m = [int(x) for x in input().split()]

ks = [int(x) for x in input().split()]

state = [False for _ in range(10001)]
state[0] = True

for i in range(1, 10001):
    for k in ks:
        if k > i: continue
        if state[i - k] == False:
            state[i] = True
            break
print(1 if state[n] else 2)
