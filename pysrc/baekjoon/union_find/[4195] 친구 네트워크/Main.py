# 정점이 문자열로 이루어진 경우 각각의 연결된 부분 집합의 크기를 구하는 문제


import sys
input = sys.stdin.readline


def find(u):
    if u == parent[u]: return u
    parent[u] = find(parent[u])
    return parent[u]

def union(a, b):
    a, b = find(a), find(b)
    if a != b:
        if rank[a] > rank[b]:
            a, b = b, a
        if rank[a] == rank[b]:
            rank[b] += 1
        parent[a] = b
        size[b] += size[a]
    print(size[b])
    
for _ in range(int(input())):
    f = int(input())
    
    parent = dict()
    rank = dict()
    size = dict()
    
    for _ in range(f):
        a, b = input().split()
        if a not in parent:
            parent[a] = a
            size[a] = 1
            rank[a] = 0
        if b not in parent:
            parent[b] = b
            size[b] = 1
            rank[b] = 0
        union(a, b)