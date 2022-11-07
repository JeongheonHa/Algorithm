import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    def dfs(y, x):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < m and ny < n:
                if graph[ny][nx] == 1:
                    graph[ny][nx] = 0
                    dfs(ny, nx)

    component = 0
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 1:
                dfs(y, x)
                component += 1

    print(component)