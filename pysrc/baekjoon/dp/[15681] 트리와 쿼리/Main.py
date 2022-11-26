# 기초적인 Tree 자료구조에 DP를 적용한 문제이다.


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def dfs(parent):
    visited[parent] = True
    d[parent] = 1
    
    for child in tree[parent]:
        if not visited[child]:
            dfs(child)
            d[parent] += d[child]
                
n, r, q = map(int, input().split())
tree = [[] for _ in range(n+1)]
visited = [False]*(n+1)
d = [0]*(n+1)

for _ in range(n-1):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)
        
dfs(r)

for _ in range(q):
    U = int(input())
    print(d[U])
    
