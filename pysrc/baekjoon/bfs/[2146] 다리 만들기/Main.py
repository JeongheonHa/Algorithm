# 섬과 섬사이에 최소한의 경로로 다리를 설치하는 문제이다.
# visited : 섬의 방문 여부를 기록한다.
# finished : 섬과 섬을 구분하기 위해 해당 섬의 방문이 끝났는지 여부를 기록하며 섬이 바뀔 때마다 초기화 해준다.
# dist : 섬과 섬 사이의 최단 거리를 측정한다.
# island : 현재의 섬을 좌표를 저장한다. (다리를 설치하기 위해 island의 모든 좌표를 대상으로 bfs를 이용해 최단 경로를 찾는다.)

# 이 문제의 핵심은 visited, finished, dist 3가지가 필요하다는 것을 인지하는 것이 포인트이다.

import sys
from collections import deque
input = sys.stdin.readline

# 섬 나누기
def bfs(x, y):
    q = deque([(x, y)])
    island.append((x, y))
    visited[x][y] = True
    finished[x][y] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    finished[nx][ny] = True
                    q.append((nx, ny))
                    island.append((nx, ny))

# 다리 설치
def install_bridge():
    bridge = deque(island)
    
    while bridge:
        x, y = bridge.popleft()
        if not finished[x][y] and graph[x][y] == 1:
            return dist[x][y] - 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if dist[nx][ny] == 0 and not finished[nx][ny]:
                    dist[nx][ny] = dist[x][y] + 1
                    bridge.append((nx, ny))
                    

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[False]*n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = sys.maxsize
for x in range(n):
    for y in range(n):
        if graph[x][y] == 1 and not visited[x][y]:
            island = []
            finished = [[False]*n for _ in range(n)]
            bfs(x, y)
            dist = [[0]*n for _ in range(n)]
            cnt = install_bridge()
            ans = min(cnt, ans)
print(ans)

                