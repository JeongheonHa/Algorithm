import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra(sx, sy):
    pq = []
    heapq.heappush(pq, (graph[sx][sy], sx, sy))
    dist[sx][sy] = graph[sx][sy]
    
    while pq:
        cost, x, y = heapq.heappop(pq)
        
        if dist[x][y] < cost:
            continue
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:

                nextDist = cost + graph[nx][ny]
                
                if nextDist < dist[nx][ny]:
                    dist[nx][ny] = nextDist
                    heapq.heappush(pq, (nextDist, nx, ny))
                

for _ in range(int(input())):
    n = int(input())

    graph = [list(map(int, input().split())) for _ in range(n)]
    dist = [[INF]*n for _ in range(n)]
    
    dijkstra(0,0)
    print(dist[n-1][n-1])