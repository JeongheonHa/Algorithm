# 가장 기본적인 플로이드 와샬 알고리즘 문제이다.
# 시간복잡도 : O(V^3)


import sys
input = sys.stdin.readline
INF = sys.maxsize


n = int(input())
m = int(input())

adj = [[INF]*n for _ in range(n)]
    
for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u-1][v-1] = min(w, adj[u-1][v-1])

for i in range(n):
    adj[i][i] = 0
    
for k in range(n):
    for a in range(n):
        for b in range(n):
            adj[a][b] = min(adj[a][b], adj[a][k] + adj[k][b])

for i in range(n):
    for j in range(n):
        if adj[i][j] == INF:
            print(0, end = " ")
        else:
            print(adj[i][j], end = " ")
    print()