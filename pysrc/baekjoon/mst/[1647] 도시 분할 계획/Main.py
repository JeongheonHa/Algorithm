import sys
input = sys.stdin.readline


def find(u):
    if parent[u] == u: return u
    parent[u] = find(parent[u])
    return parent[u]

def union(u, v):
    ru, rv = find(u), find(v)
    if ru == rv: return
    if rank[ru] > rank[rv]:
        ru, rv = rv, ru
    if rank[ru] == rank[rv]:
        rank[rv] += 1
    parent[ru] = rv

n, m = map(int, input().split())

parent = [i for i in range(n+1)]
edges = []
rank = [0]*(n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()
ans = 0
maxCost = 0
for edge in edges:
    w, u, v = edge
    if find(u) != find(v):
        union(u, v)
        ans += w
        if maxCost < w:
            maxCost = w

print(ans-maxCost)