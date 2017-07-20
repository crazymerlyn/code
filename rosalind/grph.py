import sys

table = {}
name = ""
for line in sys.stdin.readlines():
    line = line.strip()
    if line.startswith(">"):
        name = line[1:]
        table[name] = ""
    else:
        table[name] += line

for name, value in table.items():
    for name2, value2 in table.items():
        if value2 == value: continue
        if value[-3:] == value2[:3]:
            print name, name2

