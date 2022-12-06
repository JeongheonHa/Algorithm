# 가장 기본적인 다익스트라 최단 경로 알고리즘이다.
# 시간 복잡도 : O(ElogV)


import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


V, E = map(int, input().split())
start = int(input())

adj = [[] for _ in range(V+1)]
dist = [INF]*(V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))

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
                dist[there] = nextDist
                heapq.heappush(pq, (nextDist, there))

dijkstra(start)
                                                                                                                                   
for vertex in range(1, V+1):
    if dist[vertex] == INF:
        print("INF")
    else:
        print(dist[vertex])