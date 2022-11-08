# i정점이 지날 수 있는 모든 j를 그래프로 표현하는 문제이다.
# n의 조건이 100이하이기 때문에 O(n^3)으로 풀어도 해결이 가능하다.
# 인접행렬의 모든 간선을 탐색해야하기 때문에 dfs의 시간복잡도는 O(n^2)이고 dfs를 n번 돌려야하기 때문에 총 시간복잡도는 O(n^3)이다.
# 사실 이 문제는 플로이드 워셜 알고리즘으로 보다 간단히 풀 수 있다.
# 플로이드 워셜 알고리즘은 모든 노드 쌍에 대한 최단 거리를 구하는 알고리즘이다.


import sys
input = sys.stdin.readline

n = int(input())
adj = [list(map(int, input().split())) for _ in range(n)]
visited = [0]*n
graph = []

def dfs(here):
    for there in range(n):
        if adj[here][there] == 1 and not visited[there]:
            visited[there] = 1
            dfs(there)
            
for here in range(n):
    dfs(here)
    for v in visited:
        print(v, end = " ")
    print()
    visited = [0]*n