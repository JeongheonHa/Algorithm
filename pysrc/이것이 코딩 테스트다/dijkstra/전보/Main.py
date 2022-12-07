import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m, start = map(int, input().split())

adj = [[] for _ in range(n+1)]
dist = [INF]*(n+1)

for _ in range(m):
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

cnt = 0
maxDist = 0
for d in dist:
    if d != INF:
        cnt += 1
        maxDist = max(maxDist, d)

print(cnt-1, maxDist)