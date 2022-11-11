# 전형적인 최단 경로 탐색과 해당 지점까지 걸리는 시간을 구하는 문제이다.
# 단지 2차원이 아닌 3차원이기 때문에 dz를 추가해서 visited와 discovered를 이용해 구하면 된다.


import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs(z, x, y):
    q = deque([(z, x, y)])
    visited[z][x][y] = 1
    while q:
        z, x, y = q.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C and not visited[nz][nx][ny]:
                if graph[nz][nx][ny] == '.' or graph[nz][nx][ny] == 'E':
                    visited[nz][nx][ny] = 1
                    time[nz][nx][ny] = time[z][x][y] + 1
                    q.append((nz, nx, ny))
while True:
    L, R, C = map(int, input().split())
    
    if L == 0:
        break
    graph = [[]*R for _ in range(L)]
    time = [[[0]*C for _ in range(R)] for _ in range(L)]
    visited = [[[0]*C for _ in range(R)] for _ in range(L)]
    l = L-1
    while l >= 0:
        for r in range(R):
            graph[l].append(list(input().rstrip()))
            for c in range(C):
                if graph[l][r][c] == 'S':
                    sz, sx, sy = l, r, c
                elif graph[l][r][c] == 'E':
                    ez, ex, ey = l, r, c
        input()
        l -= 1
    bfs(sz, sx, sy)
    
    if time[ez][ex][ey]:
        print(f"Escaped in {time[ez][ex][ey]} minute(s).")
    else:
        print("Trapped!")     
            