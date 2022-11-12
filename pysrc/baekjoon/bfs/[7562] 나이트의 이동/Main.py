# 나이트가 목표 지점까지 이동하는데 걸리는 최단 시간을 구하는 문제이다.

# 주의 : 나이트가 이동할 때 한번도 이동하지 않은 칸으로 이동해야한다.
# 그렇지 않으면 이전에 갔던 경로로 되돌아오는 경로가 최단 경로가 될 것이다.


import sys
from collections import deque
input = sys.stdin.readline


t = int(input())

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [-1, 1, -1, 1, 2, -2, 2, -2]
          
def bfs(ex, ey):
    while q:
        x, y = q.popleft()
        
        if x == ex and y == ey:
            return graph[x][y]

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not graph[nx][ny]:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
                
for _ in range(t):
    n = int(input())
    graph = [[0]*n for _ in range(n)]
    
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    
    q = deque([(sx, sy)])
    
    print(bfs(ex, ey))
