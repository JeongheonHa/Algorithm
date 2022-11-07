# dfs를 시행한 범위의 칸을 count하는 문제이다.
# 주의해야할점은 모든 칸을 세는 것이므로 dfs내의 dfs가 반복적으로 실행하기 바로 전 단계에서 cnt를 실행해야한다.
# 비슷하게 모든 칸을 세는 것이 아닌 최대로 갈 수 있는 칸을 세는 경우 dfs의 호출 횟수를 구하는 것과 같기 때문에 dfs(x, y, cnt)형식이 되어야한다.


import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m, k = map(int, input().split())
graph = [[False]*(m+1) for _ in range(n+1)]

for _ in range(k):
    x, y = map(int, input().split())
    graph[x][y] = True
    
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y):
    global cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx > 0 and ny > 0 and nx <= n and ny <= m:
            if graph[nx][ny]:
                graph[nx][ny] = False
                cnt += 1
                dfs(nx, ny)
                
ans = 0
for x in range(1, n+1):
    for y in range(1, m+1):
        if graph[x][y]:
            graph[x][y] = False
            cnt = 1
            dfs(x, y)
            ans = max(cnt, ans)

print(ans)