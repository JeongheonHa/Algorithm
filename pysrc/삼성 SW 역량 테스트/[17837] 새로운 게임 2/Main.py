import sys
input = sys.stdin.readline


def simul():
    global turn
    while True:
        turn += 1
        if turn > 1000:
            return
        
        for i in range(k):
            x, y, d = pawns[i]
            nx = x + dx[d]
            ny = y + dy[d]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= n or graph[nx][ny] == 2:
                d ^= 1
                nx = x + dx[d]
                ny = y + dy[d]
                if nx < 0 or ny < 0 or nx >= n or ny >= n or graph[nx][ny] == 2:
                    nx, ny = x, y
            pawns[i] = [nx, ny, d]
            if nx == x and ny == y:
                continue
            
            idx = temp[x][y].index(i)
            for p in temp[x][y][idx+1:]:
                pawns[p][0] = nx
                pawns[p][1] = ny
                
            if graph[nx][ny] == 0:
                temp[nx][ny] += temp[x][y][idx:]
                
            elif graph[nx][ny] == 1:
                temp[nx][ny] += temp[x][y][idx:][::-1]
            temp[x][y] = temp[x][y][:idx]
            
            if len(temp[nx][ny]) >= 4:
                return
              
                      
n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
temp = [[[] for _ in range(n)] for _ in range(n)] # 말들의 이동
pawns = [] # 말들의 현재 위치 (idx가 말)
for i in range(k):
    x, y, d = map(int, input().split())
    pawns.append([x-1, y-1, d-1])
    temp[x-1][y-1].append(i)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

turn = 0
simul()
if turn > 1000:
    print(-1)
else:
    print(turn)