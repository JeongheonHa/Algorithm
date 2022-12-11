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

parent = [i for i in range(n)]

xpos, ypos, zpos = [], [], []
for i in range(n):
    x, y, z = map(int, input().split())
    xpos.append((x, i))
    ypos.append((y, i))
    zpos.append((z, i))
    
xpos.sort(); ypos.sort(); zpos.sort()

edges = []
for i in range(n-1):
    edges.append((xpos[i+1][0] - xpos[i][0], xpos[i][1], xpos[i+1][1]))
    edges.append((ypos[i+1][0] - ypos[i][0], ypos[i][1], ypos[i+1][1]))
    edges.append((zpos[i+1][0] - zpos[i][0], zpos[i][1], zpos[i+1][1]))
    
edges.sort()
total = 0
for i in range(len(edges)):
    w, u, v = edges[i]
    
    if find(u) != find(v):
        union(u, v)
        total += w

print(total)