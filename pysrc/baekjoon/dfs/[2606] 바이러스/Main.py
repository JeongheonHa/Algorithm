import sys
input = sys.stdin.readline

n = int(input())
e = int(input())

adj = [[] for _ in range(n+1)]

for _ in range(e):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

visited = [False]*(n+1)
cnt = 0
def dfs(u):
    global cnt
    visited[u] = True
    for v in adj[u]:
        if not visited[v]:
            cnt += 1
            dfs(v)

dfs(1)
print(cnt)