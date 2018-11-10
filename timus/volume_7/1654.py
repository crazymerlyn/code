s = input()

r = []

for c in s:
    if r and r[-1] == c:
        r.pop()
    else:
        r.append(c)
print("".join(r))
