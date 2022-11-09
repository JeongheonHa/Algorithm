# 정점의 방문 순서를 기록하는 discovered의 기능을 distance가 함으로써 정점이 지나간 거리를 기록하는 것이 포인트이다.

import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
adj = [[] for _ in range(n+1)]

distance = [0]*(n+1)

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)

q = deque([x])

def bfs(x):
    distance[x] = 0
    while q:
        here = q.popleft()
        for there in adj[here]:
            if not distance[there]:
                distance[there] = distance[here] + 1
                q.append(there)
     
bfs(x)

flag = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        flag = True

if flag == False:
    print(-1)