# 정점과 간선이 아닌 2차원 배열로 주어졌을 때 최단 경로를 구하는 문제


import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize


m, n = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
dist = [[INF]*m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra(sx, sy):
    pq = []
    heapq.heappush(pq, (0, sx, sy))
    dist[sx][sy] = 0
    while pq:
        cost, x, y = heapq.heappop(pq)

        if dist[x][y] < cost:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            nextDist = cost + graph[nx][ny]
            if nextDist < dist[nx][ny]:
                dist[nx][ny] = nextDist
                heapq.heappush(pq, (nextDist, nx, ny))


dijkstra(0, 0)
print(dist[n-1][m-1])