import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

graph = []
viruses = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            viruses.append((graph[i][j], i, j, 0))

viruses.sort()

s, x, y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(s):
    q = deque(viruses)
    while q:
        virus, x, y, sec = q.popleft()
        if sec == s:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < n:
                if not graph[nx][ny]:
                    graph[nx][ny] = virus
                    q.append((virus, nx, ny, sec+1))

bfs(s)
print(graph[x-1][y-1])