# 전형적인 정점까지의 최단 거리를 구하는 문제이다.
# discovered 배열을 이용해 방문 순서를 기록한다.

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
u, v = map(int, input().split())
m = int(input())
adj = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    adj[x][y] += 1
    adj[y][x] += 1
    
discovered = [0]*(n+1)

def bfs(here):
    q = deque([here])
    discovered[here] = 0
    while q:
        here = q.popleft()
        for there in range(1, n+1):
            if adj[here][there] != 0 and not discovered[there]:
                discovered[there] = discovered[here] + 1
                q.append(there)
    

bfs(u)

if not discovered[v]:
    print(-1)
else:
    print(discovered[v])
    
    