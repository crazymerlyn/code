import sys
from collections import Counter, defaultdict

matrix = defaultdict(Counter)
row = ""
for line in sys.stdin.readlines():
    if line.startswith(">"):
        if not row: continue
        for i, c in enumerate(row.strip()):
            matrix[i][c] += 1
        row = ""
    else:
        row += line.strip()

for i, c in enumerate(row.strip()):
    matrix[i][c] += 1

print "".join(str(matrix[i].most_common()[0][0]) for i in range(len(matrix)))

for c in "ACGT":
    print c+":", " ".join(str(matrix[i][c]) for i in range(len(matrix)))


