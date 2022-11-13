# 다시 풀어보기

import sys
from collections import deque
import heapq
input = sys.stdin.readline

# x, y 좌표의 물고기 잡아 먹고 상어 이동
def eat_fish(x, y):
    global eaten, shark_size, shark
    eaten += 1
    if shark_size == eaten:
        shark_size += 1
        eaten = 0
    graph[x][y] = 0
    shark = [x, y]

def bfs(sx, sy):
    global shark
    visited = [[False] * n for _ in range(n)]
    fishes = [] # 시간, 행, 열 순으로 저장
    visited[sx][sy] = True
    q = deque([(sx, sy, 0)])

    while q:
        x, y, t = q.popleft()
        
        if fishes and t > fishes[0][0]: # 물고기 목록 중에 조건에 맞는 물고기 선택
            second, r, c = heapq.heappop(fishes)
            eat_fish(r, c)
            return second
        
        if 0 < graph[x][y] < shark_size: # 먹을 수 있는 물고기 목록에 추가
            heapq.heappush(fishes, (t, x, y))
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] <= shark_size and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, t + 1))
    if fishes:
        second, r, c = fishes[0]
        eat_fish(r, c)
        return second
    else: 
        return None

n = int(input())

graph = []
shark = list()
for x in range(n):
    graph.append(list(map(int, input().split())))
    for y in range(n):
        if graph[x][y] == 9:
            graph[x][y] = 0
            shark = [x, y]; break
            
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

shark_size = 2
eaten = 0

answer = 0
while True:
    time = bfs(*shark)
    if time is None:
        print(answer)
        break
    else: answer += time