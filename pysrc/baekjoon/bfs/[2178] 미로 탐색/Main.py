# bfs를 돌면서 갈 수 있는 칸이 나오면 이전 값을 계속 더해 나간다.


import sys
from collections import deque
input = sys.stdin.readline


n, m = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y):
   q = deque()
   q.append((x, y))
   while q:
       x, y = q.popleft()
       for i in range(4):
           nx = x + dx[i]
           ny = y + dy[i]
           if nx >= 0 and ny >= 0 and nx < n and ny < m and maze[nx][ny] == 1:
               maze[nx][ny] += maze[x][y]
               q.append((nx, ny))

bfs(0, 0)
print(maze[n-1][m-1])
   