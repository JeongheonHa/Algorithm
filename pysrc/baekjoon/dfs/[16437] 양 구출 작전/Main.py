# 트리 모양의 방향 그래프로서 인접 리스트 형태로 만든다.
# 인접 리스트의 간선의 방향은 반대 방향으로 만들어서 dfs를 호출하고 되돌아오는 과정에서 cnt를 하도록 한다.
# 각각의 섬에 대한 정보를 island에 저장한다.
# 섬의 개수가 대략 12만개가 주어졌기 때문에 인접 행렬로 만들었다면 O(n^2)의 시간복잡도가 될 것이라고 판단해서 시간복잡도가 O(v+e)인 인접 리스트로 그래프를 만들었다.
# 또한 무방향 그래프가 아닌 유방향 그래프이므로 인접 리스트로 만드는 것이 유리하다고 판단
# n의 값이 큰 만큼 그래프의 메모리, 섬의 정보를 저장하는 메모리, n의 그래프를 재귀하는 과정에서 발생하는 메모리가 상당하기 때문에 pypy3에서는 메모리 초과가 발생한다.
# 따라서 python3로 실행

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n = int(input())

tree = [[] for _ in range(n+1)]
island = [[], [0,0]]

for i in range(2, n+1):
    t, a, p = map(str, input().split())
    a, p = int(a), int(p)
    tree[p].append(i)
    island.append([t, a])
    
    
def dfs(here):
    cnt = 0
    for there in tree[here]:
        cnt += dfs(there)
    if island[here][0] == 'S':
        cnt += island[here][1]
    else:
        cnt -= island[here][1]
        if cnt < 0:
            cnt = 0
    return cnt

print(dfs(1))
