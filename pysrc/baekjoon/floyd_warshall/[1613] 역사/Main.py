# 해당 노드와 모든 노드와의 전 후 관계를 살펴보는 문제이다.
# adj[u][v]는 u가 v보다 전에 발생한 일이고
# adj[v][u]는 v가 u보다 후에 발생한 일이다.

# 해당 노드의 최대 갯수는 400개이고 시간 제한은 2초이기 때문에 플로이드 와샬 알고리즘을 사용하면 O(V^3)으로 아슬아슬하게 통과하게 될 것이라고 생각했다.
# 하지만 python으로 돌린 결과 시간초과가 발생한다.
# 따라서, 플로이드 와샬 알고리즘에서 이미 a -> k로 가는 경유지에서 INF가 발생하는 부분은 pass하도록 최적화하였다.
# python3로는 7680ms에 통과했고 pypy3로는 3076 -> 1468ms의 성능을 갖는다.


import sys
input = sys.stdin.readline
INF = sys.maxsize


n, k = map(int, input().split())
adj = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(k):
    u, v = map(int, input().split())
    adj[u][v] = 1

for i in range(1, n+1):
    adj[i][i] = 0
    
for k in range(1, n+1):
    for a in range(1, n+1):
        if adj[a][k] == INF or adj[a][k] == 0:  # 최적화
            continue
        for b in range(1, n+1):
            if adj[a][b] > adj[a][k] + adj[k][b]:
                adj[a][b] = adj[a][k] + adj[k][b]

s = int(input())
for _ in range(s):
    x, y = map(int, input().split())
    if adj[x][y] != INF:
        print(-1)
    elif adj[y][x] != INF:
        print(1)
    elif adj[x][y] == INF and adj[y][x] == INF:
        print(0)