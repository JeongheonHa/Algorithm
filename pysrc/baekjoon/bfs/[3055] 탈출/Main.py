# 고슴도치의 이동과 물의 이동이 동시에 일어나기 때문에 for문을 이용해 시간을 기준으로 큐에 추가한 모든 요소를 동시에 한번씩 이동한다.
# 고슴도치의 이동과 물의 이동의 순서를 잘 파악해야한다.
# tip : 고슴도치와 물이 같은 칸으로 이동하는 상황을 생각해보자.


import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())

graph = []
hed = deque()
water = deque()

h_visited = [[0]*C for _ in range(R)]
w_visited = [[0]*C for _ in range(R)]

for x in range(R):
    graph.append(list(input().rstrip()))
    for y in range(C):
        if graph[x][y] == 'S':
            hed.append((x, y))
        if graph[x][y] == '*':
            water.append((x, y))
            w_visited[x][y] = 1
            
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while hed:
        w_size = len(water)
        for _ in range(w_size):
            x, y = water.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < R and 0 <= ny < C and not w_visited[nx][ny]:
                    if graph[nx][ny] != 'X' and graph[nx][ny] != 'D':
                        w_visited[nx][ny] = 1
                        water.append((nx, ny))
        
        h_size = len(hed)
        for _ in range(h_size):
            x, y = hed.popleft()
            if graph[x][y] == 'D':
                return h_visited[x][y]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < R and 0 <= ny < C and not h_visited[nx][ny]:
                    if not w_visited[nx][ny] and graph[nx][ny] != 'X':
                        h_visited[nx][ny] = h_visited[x][y] + 1
                        hed.append((nx, ny))
    return "KAKTUS"

print(bfs())