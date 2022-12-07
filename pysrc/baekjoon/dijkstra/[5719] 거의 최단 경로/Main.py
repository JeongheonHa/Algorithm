# 최단 경로의 간선들을 제외한 그래프에서 최단 경로를 찾는 문제이다.
# 최단 경로의 길이와 같은 모든 경로의 간선들을 지워야하는 것이 포인트이다.
# bfs를 이용해 역으로 최단 경로를 추적해나가면서 해당 간선들을 path에 저장한 후 graph에서 해당 간선들을 제거하면된다.


from collections import deque
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

        for there in graph[here]:
            nextDist = cost + graph[here][there]
            if nextDist < dist[there]:
                dist[there] = nextDist
                heapq.heappush(pq, (nextDist, there))


def bfs(end):
    q = deque([end])

    while q:
        here = q.popleft()
        if here == s:
            continue
        for there, weight in revGraph[here]:
            if dist[there] + graph[there][here] == dist[here]:
                if (there, here) not in path:
                    path.append((there, here))
                    q.append(there)


if __name__ == "__main__":
    while True:
        n, m = map(int, input().split())
        
        if n == 0 and m == 0:
            break
        
        s, d = map(int, input().split())
        graph = [dict() for _ in range(n)]
        revGraph = [[] for _ in range(n)]
        
        for _ in range(m):
            u, v, p = map(int, input().split()) 
            graph[u][v] = p
            revGraph[v].append((u, p))
            
        dist = [INF]*n
        dijkstra(s)

        path = []
        bfs(d)

        for u, v in path:
            del graph[u][v]
            
        dist = [INF]*n
        dijkstra(s)
        if dist[d] == INF:
            print(-1)
        else:
            print(dist[d])

