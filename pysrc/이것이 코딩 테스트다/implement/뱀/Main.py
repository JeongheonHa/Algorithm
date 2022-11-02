# 뱀이 이동하면서 사과를 먹을 경우 크기를 늘리고 사과를 먹지 않을 경우 크기를 줄이는 방법을 deque를 이용해 구현하였다.
# 정해진 시간 후에 방향을 바꾸는 부분은 우선순위 큐를 이용하여 가장 빠른 시간 부터 꺼내서 별도의 turn 함수를 이용해 방향을 바꾸도록 구현하였다.

import heapq
from collections import deque


n = int(input())
k = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]
move = []

for _ in range(k):
    x, y = map(int, input().split())
    graph[x][y] = 1
    
m = int(input())

for _ in range(m):
    x, c = input().split()
    heapq.heappush(move, (int(x), c))
    
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(d, c):
    if c == 'L':
        d = (d-1)%4
    else:
        d = (d+1)%4
    return d
        
def simulate():
    x, y = 1, 1
    graph[x][y] = 2
    d = 0
    time = 0
    q = deque()
    q.append((x, y))
    
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        if nx >= 1 and nx <= n and ny >= 1 and ny <= n and graph[nx][ny] != 2:
            if graph[nx][ny] == 0:  # 사과가 없는 경우
                graph[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.popleft()
                graph[px][py] = 0
            if graph[nx][ny] == 1:  # 사과가 있는 경우
                graph[nx][ny] = 2
                q.append((nx, ny))
        else:
            time += 1
            break
        x, y = nx, ny   # 이동
        time += 1
        if len(move) != 0 and time == move[0][0]:
            d = turn(d, heapq.heappop(move)[1])
    return time
print(simulate())