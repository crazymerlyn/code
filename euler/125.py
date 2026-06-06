LIMIT = 10**8
pal_sums = set()
for i in range(1, int(LIMIT**0.5)):
    s = i*i
    for j in range(i+1, int(LIMIT**0.5)+1):
        s += j*j
        if s >= LIMIT:
            break
        if str(s) == str(s)[::-1]:
            pal_sums.add(s)
print(sum(pal_sums))
