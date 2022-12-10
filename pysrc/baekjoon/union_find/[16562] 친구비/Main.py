# cost가 최소인 노드를 루트 노드로 만들어 각 집합의 최소 cost를 합하는 문제


import sys
input = sys.stdin.readline


def find(u):
    if u == parent[u]: return u
    parent[u] = find(parent[u])
    return parent[u]

def union(u, v):
    u, v = find(u), find(v)
    if u == v: return
    if cost[u] <= cost[v]:
        parent[v] = u
    else:
        parent[u] = v

n, m, k = map(int, input().split())

cost = [0] + list(map(int, input().split()))
parent = [0]*(n+1)

for i in range(1, n+1):
    parent[i] = i
    
for _ in range(m):
    u, v = map(int, input().split())
    union(u, v)

total = 0
friend = set()
for i in range(1, n+1):
    root = find(i)
    if root not in friend:
        friend.add(root)
        total += cost[root]
    
if total > k:
    print("Oh no")
else:
    print(total)