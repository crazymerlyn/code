masks = []
for i in range(4):
    for j in range(4):
        affected = [(i, j)]
        if i > 0: affected.append((i - 1, j))
        if i < 3: affected.append((i + 1, j))
        if j > 0: affected.append((i, j - 1))
        if j < 3: affected.append((i, j + 1))
        masks.append(sum(1 << (4 * i + j) for i, j in affected))

def form(s):
    s = bin(s)[2:].zfill(16).replace('0', 'b').replace('1', 'w')
    return "".join(s[i:i+4] + "\n" for i in range(0, len(s), 4))

def moves(board):
    return [board ^ mask for mask in masks]

board = ""
for _ in range(4):
    board += input()

board = int(board.replace("b", '0').replace("w", '1'), 2)
targets = set([0, 2 ** 16 - 1])

q = [board]
dist = {board: 0}
while q:
    node = q.pop(0)
    if node in targets:
        print(dist[node])
        break
    for child in moves(node):
        if child not in dist:
            dist[child] = dist[node] + 1
            q.append(child)
else:
    print("Impossible")
