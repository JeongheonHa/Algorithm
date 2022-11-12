# 두 객체가 동시에 움직이는 경우 목표 지점까지 최단 경로로 이동할 수 있는지를 구하는 문제이다.
# 포인트 : 상하좌우로 움직인 모든 경우의 수를 1번씩 실행하기 위해서는 큐 사이즈 만큼 for문을 돌린다.

# 실수 : 지금까지 사람 1명만 전진 시키고 모든 불 1칸씩 전진 시키고 있었음


import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    while man:
        f_size = len(fire)
        for _ in range(f_size):
            x, y = fire.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w and not f_visited[nx][ny]:
                    if graph[nx][ny] != '#':
                        f_visited[nx][ny] = 1
                        fire.append((nx, ny))
        
        m_size = len(man)
        for _ in range(m_size):
            x, y = man.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w:
                    if not m_visited[nx][ny] and not f_visited[nx][ny] and graph[nx][ny] != '#':
                        m_visited[nx][ny] = m_visited[x][y] + 1
                        man.append((nx, ny)) 
                else:
                    return m_visited[x][y] + 1
    
    return "IMPOSSIBLE"
    
    
t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(t):
    w, h = map(int, input().split())
    
    m_visited = [[0]*w for _ in range(h)]
    f_visited = [[0]*w for _ in range(h)]
    
    graph = []
    man = deque()
    fire = deque()
    for x in range(h):
        graph.append(list(input().rstrip()))
        for y in range(w):
            if graph[x][y] == '@':
                man.append((x, y))
                
            if graph[x][y] == '*':
                fire.append((x, y))
                f_visited[x][y] = 1
                
    print(bfs())
    
    
            