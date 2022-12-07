# 양방향 그래프에서 다익스트라 알고리즘을 통해 스패닝 트리의 간선들(경로)을 구하는 문제

import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

    
def dijkstra(start):
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
                edge[there] = here
                dist[there] = nextDist
                heapq.heappush(pq, (nextDist, there))


n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
dist = [INF]*(n+1)
edge = [0]*(n+1)

for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))
    
dijkstra(1)

print(n-1)  # 스패닝 트리의 간선의 갯수는 n-1
for i in range(2, n+1):
    print(i, edge[i])