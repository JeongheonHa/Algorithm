import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    while tomato:
        z, x, y = tomato.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if graph[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = graph[z][x][y] + 1
                    tomato.append((nz, nx, ny))

m, n, h = map(int, input().split())

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

graph = []
tomato = deque()
for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int, input().split())))
        for k in range(m):
            if tmp[j][k] == 1:
                tomato.append((i, j, k))
    graph.append(tmp)
       
bfs()

ans = 0        
for i in range(h):
    for j in range(n):
        if 0 in graph[i][j]:
            print(-1)
            exit(0)
        else:
            ans = max(ans, max(graph[i][j]))
            
print(ans-1)