# dfs와 백트래킹 사이의 문제라고 생각한다.
# 단지 백트래킹은 조건이 맞지않으면 돌아가지만 이 문제는 끝까지 간 후 돌아온다는 점에서 특별한 조건은 필요없다.
# 하지만 돌아오는길에 방문한 곳을 다시 False처리 해줘야한다는 점은 백트래킹과 같다.
# 최대값을 구하는 지점을 어디에 놓아야하는지 생각하는데 시간이 좀 걸렸다.
# 마지막 노드를 방문하고 상하좌우를 확인하기전에 cnt의 max값을 구하면된다.
# pypy3를 사용하여 겨우 통과하였다.

import sys
input = sys.stdin.readline

r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]

visited = [False]*26

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

ans = 0
def dfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < r and ny < c:
            if visited[ord(graph[nx][ny]) - 65] == False:
                visited[ord(graph[nx][ny]) - 65] = True
                dfs(nx, ny, cnt+1)
                visited[ord(graph[nx][ny]) - 65] = False
                
visited[ord(graph[0][0]) - 65] = True
dfs(0, 0, 1)
print(ans)
