import sys
import heapq
input = sys.stdin.readline


def bfs(tx, ty, fuel, m):
    person = 0
    status = 0
    while True:
        if m == 0: break
        q = []
        heapq.heappush(q, (0, tx, ty))
        visited = [[False]*n for _ in range(n)]
        visited[tx][ty] = True
        arrive = False
        time = 0
        while q:
            for _ in range(len(q)):
                time, x, y = heapq.heappop(q)
                
                if people[x][y][1] == 's' and status == 0:
                    fuel -= time
                    tx, ty = x, y
                    person = people[x][y][0]
                    status = 1
                    people[x][y] = (0, 0)
                    if fuel <= 0:
                        return -1
                    arrive = True
                    break
                
                if people[x][y][0] == person and status == 1:
                    fuel = fuel - time + (2*time)
                    tx, ty = x, y
                    person = 0
                    status = 0
                    people[x][y] = (0, 0)
                    m -= 1
                    if fuel < 0:
                        return -1
                    arrive = True
                    break

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if not (0 <= nx < n and 0 <= ny < n) or visited[nx][ny] or graph[nx][ny] == 1: continue
                    heapq.heappush(q, (time+1, nx, ny))
                    visited[nx][ny] = True
                    
            if arrive: break
            
            if fuel - time <= 0:
                return -1
            
        if arrive == False and len(q) == 0:
            return -1
            
    return fuel

n, m, fuel = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
tx , ty = map(int, input().split())
people = [[(0, 0)]*n for _ in range(n)] # (who, start or end), start = 's', end = 'e'
for i in range(1, m+1):
    sx, sy, ex, ey = map(int, input().split())
    people[sx-1][sy-1] = (i, 's')
    people[ex-1][ey-1] = (i, 'e')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = bfs(tx-1, ty-1, fuel, m)

print(ans)