n, k = [int(x) for x in input().split()]

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = [int(x) for x in input().split()]
    graph[a].append(b)
    graph[b].append(a)

parent = [None for _ in range(n+1)]
children = [[] for _ in range(n+1)]
dist = {k: 0}
q = [k]

while q:
    node = q.pop()
    for child in graph[node]:
        if child not in dist:
            parent[child] = node
            children[node].append(child)
            dist[child] = dist[node] + 1
            q.append(child)

state = [0 for _ in range(n+1)]
for node in sorted(range(1, n+1), key=lambda x: -dist[x]):
    for child in children[node]:
        if state[child] == 0:
            state[node] = 1
            break

if state[k] == 0:
    print("First player loses")
else:
    for child in sorted(children[k]):
        if state[child] == 0:
            print("First player wins flying to airport %d" % child)
            break
