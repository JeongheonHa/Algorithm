import sys
input = sys.stdin.readline


def spread():
    for i in range(n):
        for j in range(n):
            if smell[i][j][1]:
                smell[i][j][1] -= 1
            else:
                smell[i][j] = [0, 0]
                
            if graph[i][j]:
                smell[i][j] = [graph[i][j], k]
            
def simul():
    temp = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if graph[x][y]:
                sd = dir[graph[x][y]] - 1
                flag = False
                for i in pri[graph[x][y]][sd]:
                    nx = x + dx[i-1]
                    ny = y + dy[i-1]
                    if not (0 <= nx < n and  0 <= ny < n): continue
                    if smell[nx][ny][1] == 0:
                        dir[graph[x][y]] = i
                        if temp[nx][ny]:
                            temp[nx][ny] = min(temp[nx][ny], graph[x][y])
                        else:
                            temp[nx][ny] = graph[x][y]
                        flag = True
                        break
                
                if flag == False:    
                    for i in pri[graph[x][y]][sd]:
                        nx = x + dx[i-1]
                        ny = y + dy[i-1]
                        if not (0 <= nx < n and 0 <= ny < n): continue
                        if smell[nx][ny][0] == graph[x][y]:
                            dir[graph[x][y]] = i
                            temp[nx][ny] = graph[x][y]
                            break
        
    return temp
                
                
n, m, k = map(int, input().split())

# [shark, time]
smell = [[[0, 0]]*n for _ in range(n)]
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j]:
            smell[i][j] = [graph[i][j], k]

dir = [0] + list(map(int, input().split())) # +1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# pri[shark][nowDir][priDir], 0, +1
pri = [[] for _ in range(m+1)]
for i in range(1, m+1):
    for _ in range(4):
        temp = list(map(int, input().split()))
        pri[i].append(temp)

ans = 0
while True:
    graph = simul()
    spread()
    ans += 1
    
    flag = False
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 1:
                flag = True
    
    if flag == False:
        print(ans)
        break
    
    if ans >= 1000:
        print(-1)
        break