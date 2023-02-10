import sys
from collections import deque
input = sys.stdin.readline


def init():
    global person_dist, target_dist, visited
    person_dist = target_dist = int(1e9)
    visited = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    
def person_bfs():
    global sx, sy, person_dist

    q = deque([(tx, ty)])
    visited[tx][ty] = 0

    if graph[tx][ty] == -1:
        sx, sy, person_dist = tx, ty, visited[tx][ty]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (1 <= nx < n+1 and 1 <= ny < n+1): continue
            if graph[nx][ny] == 1 or visited[nx][ny] != -1: continue

            visited[nx][ny] = visited[x][y] + 1

            if graph[nx][ny] == -1:
                if person_dist == visited[nx][ny]:
                    if nx == sx:
                        if ny < sy:
                            sx, sy, person_dist = nx, ny, visited[nx][ny]
                    elif nx < sx:
                        sx, sy, person_dist = nx, ny, visited[nx][ny]

                elif visited[nx][ny] < person_dist:
                    sx, sy, person_dist = nx, ny, visited[nx][ny]

            q.append((nx, ny))


def target_bfs():
    global target_dist

    q = deque([(sx, sy)])
    visited[sx][sy] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (1 <= nx < n+1 and 1 <= ny < n+1): continue
            if graph[nx][ny] == 1 or visited[nx][ny] != -1: continue

            visited[nx][ny] = visited[x][y] + 1

            if nx == ex and ny == ey:
                target_dist = visited[nx][ny]

            q.append((nx, ny))


n, m, fuel = map(int, input().split())

target = [[(0, 0) for _ in range(n+1)] for _ in range(n+1)]
sx = sy = ex = ey = 0
person_dist = target_dist = 0
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

graph = [[0]*(n+1)]
for _ in range(n):
    temp = [0] + list(map(int, input().split()))
    graph.append(temp)

tx, ty = map(int, input().split())

for _ in range(m):
    sx, sy, ex, ey = map(int, input().split())
    graph[sx][sy] = -1

    target[sx][sy] = (ex, ey)

while m > 0:

    init()
    person_bfs()

    if fuel <= person_dist:
        break

    fuel -= person_dist

    graph[sx][sy] = 0

    ex, ey = target[sx][sy]

    init()
    target_bfs()

    if fuel < target_dist:
        break

    fuel += target_dist

    m -= 1

    tx, ty = ex, ey

if m > 0:
    fuel = -1

print(fuel)