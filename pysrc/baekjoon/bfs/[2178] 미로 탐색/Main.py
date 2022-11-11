# bfs를 돌면서 갈 수 있는 칸이 나오면 이전 값을 계속 더해 나간다.

# 코드를 좀 더 형식화해서 재풀이 하였다. (2022.11.11)

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < m:
                if graph[nx][ny] != 0 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1
                
                    
bfs(0, 0)
print(graph[n-1][m-1])
   