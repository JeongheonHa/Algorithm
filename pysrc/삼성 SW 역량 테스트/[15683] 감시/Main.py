import sys
from copy import deepcopy
input = sys.stdin.readline


def findSpot(graph):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                cnt += 1
    return cnt

def fill(graph, rotate, x, y):
    for d in rotate:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= m: break
            if graph[nx][ny] == 6: break
            graph[nx][ny] = '#'

def bf(graph, depth):
    global ans

    if depth == len(cctv):
        cnt = findSpot(graph)
        if ans > cnt:
            ans = cnt
        return
    
    copyGraph = deepcopy(graph)
    cctvType, x, y = cctv[depth]
    
    for rotate in mode[cctvType]:
        fill(copyGraph, rotate, x, y)
        bf(copyGraph, depth+1)
        copyGraph = deepcopy(graph)

n, m = map(int, input().split())

graph = []
cctv = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] != 0 and graph[i][j] != 6:
            cctv.append((graph[i][j], i, j))
            
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]]
]

#     북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ans = int(1e9)
bf(graph, 0)
print(ans)