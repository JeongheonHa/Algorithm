# 처음에는 2개의 그래프를 만들어서 한 곳의 G를 R로 만들 생각이였지만 dfs함수 내에 조건 문을 2개 만들어야해서 코드가 길어졌다.
# 따라서 모든 배열을 dfs한 후 graph의 내용을 수정하는 쪽으로 방향을 바꿨다.
# pypy3로할 경우 메모리 초과가 나기때문에 python3로 실행한다.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[False]*n for _ in range(n)]


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < n:
            if graph[x][y] == graph[nx][ny] and visited[nx][ny] == False:
                visited[nx][ny] = True
                dfs(nx, ny)
    
cnt1, cnt2 = 0, 0
for x in range(n):
    for y in range(n):
        if visited[x][y] == False:
            visited[x][y] = True
            dfs(x, y)
            cnt1 += 1

visited = [[False]*n for _ in range(n)]

for x in range(n):
    for y in range(n):
        if graph[x][y] == 'G':
            graph[x][y] = 'R'
            
for x in range(n):
    for y in range(n):
        if visited[x][y] == False:
            visited[x][y] = True
            dfs(x, y)
            cnt2 += 1
            
print(cnt1, cnt2)

