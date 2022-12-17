import sys
input = sys.stdin.readline


def dfs(x, y, cnt, sumDfs):
    global maxDfs
    if cnt == 4:
        if maxDfs < sumDfs:
            maxDfs = sumDfs
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, cnt+1, sumDfs + graph[nx][ny])
            visited[nx][ny] = False

            
def bfs(x, y):
    global maxBfs
    for i in range(4):
        sumBfs = graph[x][y]
        
        for j in range(3):
            d = (i+j)%4
            nx = x + dx[d]
            ny = y + dy[d]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                sumBfs = 0
                break
            
            sumBfs += graph[nx][ny]
            
        if sumBfs > maxBfs:
            maxBfs = sumBfs

            
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False]*m for _ in range(n)]

maxDfs, maxBfs = 0, 0
for i in range(n):
    for j in range(m):
        here = graph[i][j]
        visited[i][j] = True
        dfs(i,j,1,here)
        visited[i][j] = False
        bfs(i,j)
        
print(max(maxDfs, maxBfs))
