# n 세로, m 가로

n, m = map(int, input().split())
x, y ,d = map(int, input().split())

game_map = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
visited[x][y] = 1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3
    
turn_time = 0
cnt = 1

while True:
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]
    if visited[nx][ny] == 0 and game_map[nx][ny] == 0:
        visited[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    
    if turn_time == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        
        if game_map[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        
        turn_time = 0

print(cnt)
        
        
    