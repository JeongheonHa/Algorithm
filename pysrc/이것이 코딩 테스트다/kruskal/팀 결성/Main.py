def find(u):
    if u == parent[u]: return u
    parent[u] = find(parent[u])
    return parent[u]

def union(u, v):
    u, v = find(u), find(v)
    if u == v: return
    if u > v:
        parent[u] = v
    else:
        parent[v] = u

n, m = map(int, input().split())

parent = [i for i in range(n+1)]

for _ in range(m):
    option, a, b = map(int, input().split())
    
    if option == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")