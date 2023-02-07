import sys
input = sys.stdin.readline
from copy import deepcopy


def dfs(x, y, score, graph):
    global ans
    score += graph[x][y][0]
    ans = max(ans, score)
    graph[x][y][0] = 0
    
    for num in range(1, 17):
        fx, fy = -1, -1
        for i in range(4):
            for j in range(4):
                if graph[i][j][0] == num:
                    fx, fy = i, j
                    break
        
        if fx == -1 and fy == -1: continue
        
        fd = graph[fx][fy][1]
        for i in range(8):
            nd = (fd+i)%8
            nx = fx + dx[nd]
            ny = fy + dy[nd]
            if not (0 <= nx < 4 and 0 <= ny < 4) or (nx == x and ny == y): continue
            graph[fx][fy][1] = nd
            graph[fx][fy], graph[nx][ny] = graph[nx][ny], graph[fx][fy]
            break
    
    sd = graph[x][y][1]
    for i in range(1, 5):
        nx = x + dx[sd]*i
        ny = y + dy[sd]*i
        if not (0 <= nx < 4 and 0 <= ny < 4) or graph[nx][ny][0] == 0: continue
        dfs(nx, ny, score, deepcopy(graph))
        
graph = [[] for _ in range(4)]
for i in range(4):
    temp = list(map(int, input().split()))
    for j in range(4):
        graph[i].append([temp[j*2], temp[j*2+1]-1])

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

ans = 0
dfs(0, 0, 0, graph)

print(ans)