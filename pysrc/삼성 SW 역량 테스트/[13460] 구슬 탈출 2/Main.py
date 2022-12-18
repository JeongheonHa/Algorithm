import sys
from collections import deque
input = sys.stdin.readline


def bfs(rsx, rsy, bsx, bsy, rotate):
    for n in range(4):
        cnt = 0
        rq = deque()
        bq = deque()
        rq.append((rsx, rsy))
        bq.append((bsx, bsy))
        
        for i in range(4):
            move = False
            i = (n + i)% 4
            if rotate == -1:
                i = 4-i
                if i == -1:
                    i = 3

            while q:
                rx, ry = rq.popleft()
                bx, by = bq.popleft()
                
                if graph[bx][by] == '0':
                    return 0
                if graph[rx][ry] == '0':
                    return cnt
                nrx = rx + dx[i]
                nry = ry + dy[i]
                nbx = bx + dx[i]
                nby = by + dy[i]
                
                if 0 <= nrx < n and 0 <= nry < m and 0 <= nbx < n and 0 <= nby < m:
                    if graph[nrx][nry] != '#' and graph[nbx][nby] != '#' and nrx != nbx and nry != nby:
                        move = True
                        q.append((nrx, nry, nbx, nby))
            
            if move == True:
                cnt += 1
            
    
    
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 'R':
            rx, ry = i, j
        if graph[i][j] == 'B':
            bx, by = i, j

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

ans = min(bfs(rx, ry, bx, by, 1), bfs(rx, ry, bx, by, -1))

print(ans)