# 벽 1개를 부순 경우 최단 경로로 목표지점까지 갈 수 있는지를 확인하는 문제이다.
# 포인트 : 3차원 공간을 이용하여 1층에는 벽을 부수지않은 경우를 2층에는 벽 1개를 부순 경우로 나눈다.


import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0]*m for _ in range(n)] for _ in range(2)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque([(0, 0, 0)])
    visited[0][0][0] = 1
    while q:
        w, x, y = q.popleft()
        if x == n-1 and y == m-1:
            return visited[w][x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] and w == 0:
                    visited[1][nx][ny] = visited[0][x][y] + 1
                    q.append((1, nx, ny))
                elif not graph[nx][ny] and not visited[w][nx][ny]:
                    visited[w][nx][ny] = visited[w][x][y] + 1
                    q.append((w, nx, ny))
    return -1

print(bfs())