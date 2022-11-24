# dfs와 DP를 이용해서 (1,1)부터 (m,n)까지의 갈 수 있는 경로의 갯수를 구하는 문제이다.
# 주의해야할 점은 루프를 방지하기위해 d[x][y]를 다시 0으로 초기화 해줘야한다.


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1
    
    if d[x][y] != -1:
        return d[x][y]
    
    d[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if graph[nx][ny] < graph[x][y]:
                d[x][y] += dfs(nx, ny)

    return d[x][y]

m, n = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

d = [[-1]*n for _ in range(m)]

print(dfs(0,0))