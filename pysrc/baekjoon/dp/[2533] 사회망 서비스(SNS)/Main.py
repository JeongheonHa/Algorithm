# Tree 자료구조와 DP를 이용한 문제이다.
# 루트 노드를 중심으로 dfs를 통해 모든 노드를 리프 노드까지 탐색 후 주어진 조건에 따라 점화식을 적용하는 것이 포인트이다.
# 큰 문제 : 아이디어 전파에 필요한 최소 얼리어탭터의 인원
# 작은 문제 : 해당 노드에서 리프노드까지 아이디어 전파에 필요한 최소 얼리어댑터의 인원

# 점화식:
# 1. 부모노드가 일반인인 경우 자식노드는 모두 얼리어댑터야한다.
# 2. 부모노드가 얼리어댑터인 경우 자식노드는 얼리어댑터일 수도 있고 일반인일 수 도 있다.

import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline 

def dfs(parent):
  visited[parent] = True
  d[parent][0] = 0
  d[parent][1] = 1

  for child in tree[parent]:
    if not visited[child]:
      dfs(child)
      d[parent][0] += d[child][1]
      d[parent][1] += min(d[child][0], d[child][1])
      
n = int(input())
tree  = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(n-1):
  u, v = map(int, input().split())
  tree[u].append(v)
  tree[v].append(u)

d = [[0,0] for _ in range(n+1)]

dfs(1)

print(min(d[1][0], d[1][1]))