import sys
input = sys.stdin.readline
INF = sys.maxsize


n, m = map(int, input().split())

adj = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u][v] = 1
    adj[v][u] = 1

for i in range(1, n+1):
    adj[i][i] = 0
    
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if adj[a][k] + adj[k][b] < adj[a][b]:
                adj[a][b] = adj[a][k] + adj[k][b]

ans = [0]
for u in range(1, n+1):
    sum_val = 0
    for v in range(1, n+1):
        if adj[u][v] != INF and u != v:
            sum_val += adj[u][v]
    ans.append(sum_val)

answer = INF
vertex = 0
for i in range(1, n+1):
    if ans[i] < answer:
        answer = ans[i]
        vertex = i

print(vertex)