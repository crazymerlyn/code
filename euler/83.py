import heapq

with open('p083_matrix.txt') as f:
    m = [[int(x) for x in line.split(',')] for line in f]
n = len(m)
dist = [[float('inf')] * n for _ in range(n)]
dist[0][0] = m[0][0]
pq = [(m[0][0], 0, 0)]
dirs = [(0,1),(0,-1),(1,0),(-1,0)]
while pq:
    d, r, c = heapq.heappop(pq)
    if d > dist[r][c]:
        continue
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n:
            nd = d + m[nr][nc]
            if nd < dist[nr][nc]:
                dist[nr][nc] = nd
                heapq.heappush(pq, (nd, nr, nc))
print(dist[n-1][n-1])
