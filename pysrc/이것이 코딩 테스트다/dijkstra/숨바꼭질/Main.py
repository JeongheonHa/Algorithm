import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize


n, m = map(int, input().split())

adj = [[] for _ in range(n+1)]
dist = [INF]*(n+1)

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append((v,1))
    adj[v].append((u,1))

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

dijkstra(1)

maxNode = 0
maxDist = 0

result = []

for i in range(1, n+1):
    if maxDist < dist[i]:
        maxNode = i
        maxDist = dist[i]
        result = [maxNode]
    elif maxDist == dist[i]:
        result.append(i)

print(maxNode, maxDist, len(result))