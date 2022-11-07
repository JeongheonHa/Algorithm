# 2차원 행렬이 아닌 좌표를 갖는 그래프로 주어졌을 경우 dfs를 하는 문제이다.
# 2차원 좌표로 이루어진 경우 행과 열이 아래에서 위로 왼쪽에서 오른쪽으로 좌표가 증가한다.
# 또한 그래프 내의 간선을 표현하기위한 칸은 (0,0)부터 (1,1)까지 모두 포함하기 때문에 문제의 조건에 맞춰 기준을 정하는 것이 좋다.


import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

m, n, k = map(int, input().split())

graph = [[False]*(n) for _ in range(m)]

for _ in range(k):
    lx, ly, rx, ry = map(int, input().split())
    for x in range(lx, rx):
        for y in range(ly, ry):
            if not graph[y][x]:
                graph[y][x] = True
    

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y):
    global cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < m and ny < n:
            if not graph[nx][ny]:
                graph[nx][ny] = True
                cnt += 1
                dfs(nx, ny)

total = []
component = 0
for x in range(m):
    for y in range(n):
        if not graph[x][y]:
            graph[x][y] = True
            cnt = 1
            dfs(x, y)
            total.append(cnt)
            component += 1
           
total.sort()
 
print(component)

for cnt in total:
    print(cnt, end = ' ')