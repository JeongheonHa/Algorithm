import sys
input = sys.stdin.readline


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

g = int(input())
p = int(input())

parent = [i for i in range(g+1)]
cnt = 0
for _ in range(p):
    root = find(int(input()))
    if root == 0:
        break
    union(root, root-1)
    cnt += 1

print(cnt)