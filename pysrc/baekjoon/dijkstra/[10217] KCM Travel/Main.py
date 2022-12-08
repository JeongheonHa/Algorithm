# M원 이하의 비용(돈)으로 1 -> n까지 가는 최단 거리를 구하는 문제
# 다익스트라 + DP를 활용
# DP테이블에 각 정점까지 제한 비용까지의 1 ~ m까지 cost를 투자해서 갈 수 있는 최단 거리를 기록
# 즉, 7원을 투자해서 갈 수 있는 최단 거리가 7일 때 9원을 투자해도 갈 수 있는 최단 거리가 7원의 비용의 path일 수 있다.


import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start, 0))
    time[start][0] = 0
    
    while pq:
        hour, here, cost = heapq.heappop(pq)
        
        if time[here][cost] < hour:
            continue
        
        for there, weight, thereCost in adj[here]:
            nextDist = hour + weight
            nextCost = cost + thereCost
            
            if nextCost <= m and nextDist < time[there][nextCost]:
                for i in range(nextCost, m+1):
                    if time[there][i] > nextDist:
                        time[there][i] = nextDist
                    else:
                        break
                    
                heapq.heappush(pq, (nextDist, there, nextCost))
        
for _ in range(int(input())):
    n, m, k = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    time = [[INF]*(m+1) for _ in range(n+1)]
    
    for _ in range(k):
        u, v, c, d = map(int, input().split())
        adj[u].append((v, d, c))
    
    dijkstra(1)
    
    ans = time[n][m]
    
    if ans == INF:
        print("Poor KCM")
    else:
        print(ans)
    