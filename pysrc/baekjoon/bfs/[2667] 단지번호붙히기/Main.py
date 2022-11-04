# 2차원 배열에서 이어져있는 범위 단위로 나누고 싶을 때 2차원 모든 원소에 대해서 bfs를 하면서 그래프를 수정해나간다.
# 리스트는 가변객체이므로 함수 내에서 변경이이되어도 함수 밖에 영향을 받는다.

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 0
    cnt = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < n and graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = 0
                cnt += 1
    return cnt

total = []
complex_cnt = 0
for x in range(n):
    for y in range(n):
        if graph[x][y] == 1:
            total.append(bfs(x, y))
            complex_cnt += 1
        
total.sort()

print(complex_cnt)
for cnt in total:
    print(cnt)