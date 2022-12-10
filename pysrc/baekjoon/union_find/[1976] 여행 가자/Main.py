# 해당 노드들이 서로 같은 집합인지를 묻는 문제

import sys
input = sys.stdin.readline


def find(u):
    if u == parent[u]: return u
    parent[u] = find(parent[u])
    return parent[u]

def union(a, b):
    a, b = find(a), find(b)
    if a == b: return
    if rank[a] > rank[b]:
        a, b = b, a
    if rank[a] == rank[b]:
        rank[b] += 1
    parent[a] = b
    
n = int(input())
m = int(input())


parent = [0]*(n+1)
rank = [0]*(n+1)

for i in range(1, n+1):
    parent[i] = i
    
for i in range(1, n+1):
    link = list(map(int, input().split()))
    for j in range(1, len(link)+1):
        if link[j-1] == 1:
            union(i, j)
            
path = list(map(int, input().split()))
ans = set([find(i) for i in path])
if len(ans) != 1:
    print("NO")
else:
    print("YES")