def find(u):
    if u == parent[u]: return u
    parent[u] = find(parent[u])
    return parent[u]

def union(u, v):
    u, v = find(u), find(v)
    if u > v:
        parent[u] = v
    else:
        parent[v] = u


n, m = map(int, input().split())

parent = [i for i in range(n)]
edges = []

for _ in range(m):
    x, y, z = map(int, input().split())
    edges.append((z, x, y))

edges.sort()

save = 0
total = 0
for edge in edges:
    dist, u, v = edge
    total += dist
    if find(u) != find(v):
        union(u, v)
        save += dist

print(total-save)