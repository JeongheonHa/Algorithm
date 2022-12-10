# 기본적인 유니온 파인드 자료구조를 이용하는 문제이다.

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
    

n, m = map(int, input().split())
parent = [0]*(n+1)
rank = [0]*(n+1)

for i in range(1, n+1):
    parent[i] = i
    
for _ in range(m):
    option, a, b = map(int, input().split())
    if option == 0:
        union(a, b)
    else:
        ra = find(a)
        rb = find(b)
        
        if ra == rb:
            print("YES")
        else:
            print("NO")