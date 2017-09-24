from collections import defaultdict

matrix = []
with open("./p345_matrix.txt") as f:
    for line in f:
        matrix.append([int(x) for x in line.strip().split()])

results = defaultdict(int)
results[tuple()] = 0

for i in range(len(matrix)):
    newresults = defaultdict(int)
    for j in range(len(matrix[0])):
        for done in results:
            if j not in done:
                comb = tuple(sorted(done + (j,)))
                newresults[comb] = max(newresults[comb], results[done] + matrix[i][j])
    results = newresults

print max(results.values())


