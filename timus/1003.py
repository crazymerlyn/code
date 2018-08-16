import sys

sys.setrecursionlimit(10000)

while True:
    try:
        n = int(input())
        if n == -1: break
        k = int(input())
    except:
        break
    odd = {}
    prev = {}

    def add(a, b, c):
        if b not in odd:
            odd[b] = c
            prev[b] = a
            return True
        i = prev[b]
        if i == a:
            return odd[b] == c
        if i < a:
            return add(i, a-1, odd[b] != c)
        else:
            return add(a, i-1, odd[b] != c)

    data = []
    for _ in range(k):
        try:
            data.append(input().split())
        except:
            break

    for i, (a, b, c) in enumerate(data):
        a, b = [int(a), int(b)]
        if a < 0 or b > n or (not add(a, b, c == "odd")):
            print(i)
            break
    else:
        print(len(data))
