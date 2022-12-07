# 이동 경로에 조건이 붙은 경우 다익스트라 알고리즘으로 최단 경로를 구하는 문제


import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(start):
    dist = [INF]*(n+1)
    pq = []
    heapq.heappush(pq, (0, start))
    dist[start] = 0
    
    while pq:
        cost, here = heapq.heappop(pq)
        
        if dist[here] < cost:
            continue
        
        for there, weight in adj[here]:
            if h[here] < h[there]:
                nextDist = cost + weight
                
                if nextDist < dist[there]:
                    dist[there] = nextDist
                    heapq.heappush(pq, (nextDist, there))
    
    return dist

n, m, d, e = map(int, input().split())
h = [0] + list(map(int, input().split()))
adj = [[] for _ in range(n+1)]


for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))

ans = -INF
path1 = dijkstra(1)
path2 = dijkstra(n)
for i in range(2, n):
    ans = max(ans, h[i]*e - (path1[i] + path2[i]) * d)

if ans == -INF:
    print("Impossible")
else:
    print(ans)