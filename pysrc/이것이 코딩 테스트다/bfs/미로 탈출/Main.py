from collections import deque


n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    
    while len(q) != 0:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >=n or ny < 0 or ny >= m:        
                continue
            
            if maze[nx][ny] == 0:
                continue
            
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                q.append((nx, ny))
                
    return maze[n-1][m-1]

print(bfs(0, 0))