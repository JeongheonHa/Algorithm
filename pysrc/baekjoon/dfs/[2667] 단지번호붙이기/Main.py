import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
ans = []

def dfs(x, y):
    global cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < n:
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                cnt += 1
                dfs(nx ,ny)

complex_cnt = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            graph[i][j] = 0
            cnt = 1
            dfs(i, j)
            ans.append(cnt)
            complex_cnt += 1

ans.sort()

print(complex_cnt)
for house_cnt in ans:
    print(house_cnt)
