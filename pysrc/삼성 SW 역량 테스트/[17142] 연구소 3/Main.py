import sys
from collections import deque
input = sys.stdin.readline


def bf(cnt, idx):
    if cnt == m:
        bfs(zeroCnt)
        return

    for i in range(idx, len(virus)):
        active[cnt] = virus[i]
        bf(cnt+1, i+1)
        
def bfs(zero):
    global ans
    visited = [[False]*n for _ in range(n)]
    q = deque()
    
    for i in range(m):
        x, y, d = active[i]
        visited[x][y] = True
        q.append((x, y, d))
        
    while q:
        x, y, dist = q.popleft()
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n or visited[nx][ny]: continue
            if graph[nx][ny] == 1: continue
            if graph[nx][ny] == 0:
                zero -= 1
            if zero == 0:
                ans = min(ans, dist+1)
                return
            visited[nx][ny] = True
            q.append((nx, ny, dist+1))
        

n, m = map(int, input().split())
graph = []
virus = []
zeroCnt = 0
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 0:
            zeroCnt += 1
        if graph[i][j] == 2:
            virus.append((i,j,0))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

active = [0]*10
ans = sys.maxsize

if zeroCnt == 0:
    print(0)
else:    
    bf(0,0)
    if ans != sys.maxsize:
        print(ans)
    else:
        print(-1)