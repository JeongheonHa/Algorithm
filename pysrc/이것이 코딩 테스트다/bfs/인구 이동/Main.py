import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

sec = 0

def bfs(x, y):
    q = deque([(x, y)])
    unit = []
    unit.append((x, y))
    visited[x][y] = 1
    papulation = graph[x][y]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    unit.append((nx, ny))
                    papulation += graph[nx][ny]
    
    for x, y in unit:
        graph[x][y] = papulation//len(unit)
    
    if len(unit) == 1:
        return 0
    else:
        return 1
    
        
while True:
    cnt = 0
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                cnt += bfs(i, j)
    
    if cnt == 0:
        break
    sec += 1
    
print(sec)