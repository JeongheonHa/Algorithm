# n의 크기가 최대 500이기 때문에 O(n^3)내에 문제를 해결해야한다.
# 2차원에서 최대 이동 경로를 구해야하기 떄문에 모든 지점에서 dfs를 이용해 최대 이동 경로를 구해야 한다고 생각했다. 
# 하지만 dfsAll과 dfs로 인해 시간복잡도는 O(n^4)이 된다.
# 따라서 각 지점마다 갈 수 있는 최대 이동 경로를 dp에 기록하면 dfs를 상수시간 내에 구할 수 있다.
# 따라서 시간 복잡도는 O(n^2)이 된다.


import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

def dfs(x, y):
    if d[x][y]:
        return d[x][y]
    d[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > graph[x][y]:
            d[x][y] = max(d[x][y], dfs(nx, ny) + 1)
    return d[x][y]
    
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

d = [[0]*n for _ in range(n)] 
ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i, j))

print(ans)