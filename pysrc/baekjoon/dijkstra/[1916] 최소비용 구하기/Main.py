import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
bus = int(input())
graph = [[] for _ in range(n+1)]
costs = [INF]*(n+1)

for _ in range(bus):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

start, end = map(int, input().split())
def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    costs[start] = 0
    
    while pq:
        cost, here = heapq.heappop(pq)
        
        if costs[here] < cost:
            continue
        
        for there, weight in graph[here]:
            nextCost = cost + weight
            
            if nextCost < costs[there]:
                costs[there] = nextCost
                heapq.heappush(pq, (nextCost, there))

dijkstra(start)

print(costs[end])
