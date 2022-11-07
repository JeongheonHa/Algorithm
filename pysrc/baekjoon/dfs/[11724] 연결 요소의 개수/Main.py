# 인접 리스트를 이용한 무방향 그래프 dfs문제이다.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
visited = [0]*(n+1)

adj = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

def dfs(next):
    for e in adj[next]:
        if not visited[e]:
            visited[e] = 1
            dfs(e)
            
component = 0
for v in range(1,n+1):
    if not visited[v]:
        visited[v] = 1
        dfs(v)
        component += 1

print(component)