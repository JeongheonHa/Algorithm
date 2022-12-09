# 자기 자신으로 돌아오는 최단 거리를 구하는 문제

import sys
input = sys.stdin.readline
INF = sys.maxsize

v, e = map(int, input().split())

adj = [[INF]*(v+1) for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    adj[a][b] = c

for k in range(1, v+1):
    for a in range(1, v+1):
        if adj[a][k] == INF:
            continue
        for b in range(1, v+1):
            adj[a][b] = min(adj[a][b], adj[a][k] + adj[k][b])

minDist = INF
for i in range(1, v+1):
    minDist = min(minDist, adj[i][i])

if minDist == INF:
    print(-1)
else:
    print(minDist)