# 이 문제를 pypy3로 풀려고하면 visited를 계속 생산하기 때문에 메모리를 많이 잡아먹는다.
# 따라서 python3로 풀어야하며 dfs를 이용하려면 재귀 제한을 풀어야 풀 수 있다.

# 어렵진 않았으나 재귀 제한을 푸는 과정과 메모리 초과가 나는 상황에서 다른 방법이 있는지 생각하느라 시간이 많이 걸렸다.
# visited 대신 copy를 이용해 그래프를 복사해서 사용하는 방법도 생각해보았지만 메모리가 더 들거라고 판단
# 리스트 컴프리헨션을 이용해 데이터를 입력 받고 height값을 map을 이용해 받으면 시간이 줄어들거라고 판단

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
    
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y, h):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < n:
            if graph[nx][ny] > h and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, h)
        
ans = 0
for h in range(max(map(max, graph))):
    cnt = 0
    visited = [[False]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if graph[x][y] > h and not visited[x][y]:
                visited[x][y] = True
                cnt += 1
                dfs(x, y, h)
    ans = max(cnt, ans)

print(ans)