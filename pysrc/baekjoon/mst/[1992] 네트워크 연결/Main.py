import sys
input = sys.stdin.readline


def find(u):
    if u == parent[u]: return u
    parent[u] = find(parent[u])
    return parent[u]

def union(u, v):
    ru, rv = find(u), find(v)
    if ru == rv: return
    if ru > rv:
        parent[ru] = rv
    else:
        parent[rv] = ru
        
n = int(input())
m = int(input())

parent = [i for i in range(n+1)]
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()
ans = 0
for edge in edges:
    w, u, v = edge
    if find(u) != find(v):
        union(u, v)
        ans += w

print(ans)