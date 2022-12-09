import sys
input = sys.stdin.readline

n, m = map(int, input().split())

adj = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u][v] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if adj[a][k] and adj[k][b]:
                adj[a][b] = 1

cnt = 0
for u in range(1, n+1):
    link = 0
    for v in range(1, n+1):
        link += adj[u][v] + adj[v][u]
    
    if link == n-1:
        cnt += 1

print(cnt)