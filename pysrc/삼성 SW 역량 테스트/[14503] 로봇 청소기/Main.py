import sys
input = sys.stdin.readline


def turn(d):
    d = (d-1)%4
    return d

def move(x, y, d):
    cnt = 1
    graph[x][y] = 2
    
    while True:
        flag = False

        for i in range(4):
            d = turn(d)
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    cnt += 1
                    x, y = nx, ny
                    flag = True
                    break
            
        if flag == False:
            x -= dx[d]
            y -= dy[d]
            if graph[x][y] == 1:
                return cnt
                    
                
n, m = map(int, input().split())
sx, sy, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ans = move(sx, sy, d)
print(ans)