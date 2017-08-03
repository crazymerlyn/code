def min_path(matrix):
    n = len(matrix)
    m = len(matrix[0])
    queue = [(0, 0)]
    dist = {(0, 0): matrix[0][0]}

    def adjacent(i, j):
        if i > 0: yield (i-1, j)
        if i < n-1: yield (i+1, j)
        if j > 0: yield (i, j-1)
        if j < m-1: yield (i, j+1)

    index = 0
    while index < len(queue):
        i, j = queue[index]
        index += 1
        for x, y in adjacent(i, j):
            if (x, y) not in dist or dist[(x, y)] > dist[(i,j)]+matrix[x][y]:
                dist[(x, y)] = dist[(i, j)] + matrix[x][y]
                queue.append((x, y))

    return dist[(n-1), (m-1)]


with open("./p083_matrix.txt") as f:
    matrix = []
    for line in f:
        matrix.append([int(x) for x in line.strip().split(",")])
    print(min_path(matrix))

