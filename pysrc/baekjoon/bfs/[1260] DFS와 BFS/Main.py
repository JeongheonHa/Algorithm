# dfs와 bfs의 개념 문제
# 양방향 그래프이기 때문에 인접 행렬을 사용하는 것이 좋을 것이라고 판단
# 인접 행렬의 경우 idx가 정점에 해당하기 때문에 정점을 돌 때는 for문을 이용해 n까지의 idx를 모두 탐색한다.


import sys
from collections import deque
input = sys.stdin.readline


n, m, v = map(int, input().split())
adj = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    adj[x][y] += 1
    adj[y][x] += 1
    
def dfs(here):
    visited[here] = 1
    print(here, end = " ")
    
    for there in range(1, n+1):
        if adj[here][there] != 0 and not visited[there]:
            dfs(there)
    
    
def bfs(here):
    q = deque([here])
    visited[here] = 1
    while q:
        here = q.popleft()
        print(here, end = " ")
        for there in range(1, n+1):
            if adj[here][there] != 0 and not visited[there]:
                visited[there] = 1
                q.append(there)

visited = [0]*(n+1)        
dfs(v)
print()
visited = [0]*(n+1)
bfs(v)
