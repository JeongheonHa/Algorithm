# 우선순위에 맞게 물고기를 먹은 후 최단 경로를 찾는 문제이다.
# 물고기를 먹고 난 후 먹을 수 있는 다음 물고기 까지의 최단 경로를 구하여 지금까지 지나온 경로를 갱신한다.
# 현재 위치에서 다시 bfs를 호출하여 먹을 수 있는 다음 물고기 까지의 최단 경로를 구한다.
# 먹을 수 없는 물고기가 없을 때 까지 반복하여 최단 경로를 구한다.

# 포인트 : 물고기를 1마리 먹을 때마다 bfs를 호출하여 최단 경로를 갱신한다.

import sys
from collections import deque
import heapq
input = sys.stdin.readline

def bfs(sx, sy):
    global shark_size
    visited = [[-1]*n for _ in range(n)]
    fishes = []
    visited[sx][sy] = 0
    q = deque([(sx, sy)])

    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] <= shark_size and visited[nx][ny] == - 1:  # 지나갈 수 있는 경우
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                    if 0 < graph[nx][ny] < shark_size:    # 먹을 수 있는 경우
                        heapq.heappush(fishes, (visited[nx][ny], nx, ny))   # 먹을 수 있는 물고기 리스트를 우선순위에 맞게 저장
    if len(fishes) == 0:
        return None
    return heapq.heappop(fishes)

n = int(input())

graph = []
for x in range(n):
    graph.append(list(map(int, input().split())))
    for y in range(n):
        if graph[x][y] == 9:
            graph[x][y] = 0
            sx, sy = x, y
            break
            
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

shark_size = 2
eaten = 0

ans = 0

while True:
    fish = bfs(sx, sy)
    
    if fish == None:
        print(ans)
        exit()
   
    time, sx, sy = fish
    
    eaten += 1
    if shark_size == eaten:
        shark_size += 1
        eaten = 0
    
    graph[sx][sy] = 0
    ans += time