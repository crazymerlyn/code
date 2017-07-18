s = raw_input().strip()
t = raw_input().strip()

res = []

for i in range(0, len(s) - len(t)):
    if s[i:i+len(t)] == t:
        res.append(i)


print " ".join(str(x+1) for x in res)
