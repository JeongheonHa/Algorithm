import sys
input = sys.stdin.readline


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
graph = []
for u in range(n):
    graph.append(list(map(int, input().split())))
    for v in range(n):
        if graph[u][v] == 1:
            union(u+1, v+1)

path = list(map(int, input().split()))

root = find(path[0])
flag = False
for node in path:
    if root != find(node):
        print("NO")
        flag = True
        break

if flag == False:
    print("YES")