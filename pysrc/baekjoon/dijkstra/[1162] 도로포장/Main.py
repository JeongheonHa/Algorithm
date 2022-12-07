# k개 이하의 간선의 가중치를 0으로 만들 때 다익스트라를 이용하여 최단 거리를 구하는 문제
# 2차원 dist리스트를 만들어 가중치를 몇 번 0으로 만들었는지에 따라 해당 정점까지의 최단 거리를 저장한다.


import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start, 0))
    dist[start][0] = 0

    while pq:
        cost, here, cnt = heapq.heappop(pq)
        
        if dist[here][cnt] < cost:
            continue
        
        for there, weight in adj[here]:
            nextDist = cost + weight
            
            if nextDist < dist[there][cnt]:
                dist[there][cnt] = nextDist
                heapq.heappush(pq, (nextDist, there, cnt))
            
            if cnt < k and dist[there][cnt+1] > cost:
                dist[there][cnt+1] = cost
                heapq.heappush(pq, (cost, there, cnt+1))
                
                
n, m, k = map(int, input().split())
adj = [[] for _ in range(n+1)]
dist = [[INF]*(k+1) for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))
    
for i in range(1, k+1):
    dist[1][i] = 0
    
dijkstra(1)
print(min(dist[n]))