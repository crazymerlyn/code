from collections import defaultdict

n = 10000
d = defaultdict(list)
for i in range(1, n):
    d["".join(sorted(str(i * i * i)))].append(i)

for item in d.items():
    if len(item[1]) == 5:
        print(item)
