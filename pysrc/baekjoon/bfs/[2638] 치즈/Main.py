# 얼음이 치즈를 완전히 녹이는데 걸리는 시간을 구하는 문제이다.
# 큐에 상하좌우로 퍼지는 얼음을 넣어 다음 위치의 칸에 치즈가 있을 경우 +1을 한다.
# 탐색을 끝낸 시점에 각 칸의 값이 3 이상이라면 2개의 면 이상이 얼음과 접촉한 것이기 때문에 해당 칸을 얼음으로 만든다.
# 1 사이클이 끝나면 시간을 +1 한다.
# 모든 치즈가 다 녹을 때까지 반복한다.

# 얼음과 접촉하는 2개 이상의 면을 표현하는 것이 포인트이다.


import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    q = deque([(0, 0)])
    visited[0][0] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                else:
                    graph[nx][ny] += 1

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

hour = 0

while True:
    visited = [[False]*m for _ in range(n)]
    bfs()
    flag = False
    for x in range(n):
        for y in range(m):
            if graph[x][y] > 2:
                graph[x][y] = 0
                flag = True
            elif graph[x][y] == 2:
                graph[x][y] = 1
                
    if flag == False:
        break 
            
    hour += 1        

print(hour)
                        