# 목표 지점이 없이 갈 수 있는 모든 칸의 최단 경로를 구해야하는 문제이다.
# visited를 이용하는 것이 아닌 그래프 자체에 최단 경로를 표현해야 도달하지 못하는 칸을 구할 수 있다.


import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())

graph = []
tomato = deque()
for x in range(n):
    graph.append(list(map(int, input().split())))
    for y in range(m):
        if graph[x][y] == 1:
            tomato.append((x, y))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while tomato:
        x, y = tomato.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not graph[nx][ny]:
                graph[nx][ny] = graph[x][y] + 1
                tomato.append((nx, ny))

bfs()

ans = 0
for x in range(n):
    if 0 in graph[x]:
        ans = -1
        break
    else:
        ans = max(ans, max(graph[x])-1)

print(ans)
                    