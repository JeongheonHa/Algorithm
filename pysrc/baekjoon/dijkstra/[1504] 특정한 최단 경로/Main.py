# 특정 노드를 거쳐 n까지 가는 최단 경로의 길이를 구하는 문제


import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize


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

n, e = map(int, input().split())
adj = [[] for _ in range(n+1)]

for _ in range(e):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))

v1, v2 = map(int, input().split())

minDist1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
minDist2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)

if minDist1 >= INF and minDist2 >= INF:
    print(-1)
else:
    print(min(minDist1, minDist2))

print(INF)