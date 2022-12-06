# 단방향 그래프에서 최단 경로로 갔다가 다시 최단 경로로 돌아오는데 걸리는 시간을 구하는 문제

import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize


n, m, x = map(int, input().split())

adj = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    
def dijkstra(start, end):
    dist = [INF]*(n+1)
    pq = []
    heapq.heappush(pq, (0, start))
    dist[start] = 0
    
    while pq:
        cost, here = heapq.heappop(pq)
        
        if dist[here] < cost:
            continue
        
        for there, weight in adj[here]:
            nextDist = cost + weight
            
            if nextDist < dist[there]:
                dist[there] = nextDist
                heapq.heappush(pq, (nextDist, there))
    
    return dist[end]

path = 0
for start in range(1, n+1):
    if start != x:
        path = max(path, dijkstra(start, x) + dijkstra(x, start))

print(path)