import sys, math
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

star = [tuple(map(float, input().split()))for _ in range(n)]
parent = [i for i in range(n+1)]
edges = []

for i in range(n-1):
    for j in range(i+1, n):
        dist = math.sqrt((star[i][0] - star[j][0])**2 + (star[i][1] - star[j][1])**2)
        edges.append((dist, i+1, j+1))

edges.sort()

ans = 0
for edge in edges:
    w, u, v = edge
    if find(u) != find(v):
        union(u, v)
        ans += w
        
print(round(ans, 2))