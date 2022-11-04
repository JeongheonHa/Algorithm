# dfs: 기둥 3개를 설치하는 모든 경우의 수를 구한다.(조합)
# escape: 기둥 3개를 설치했을 때의 바이러스가 퍼진 결과를 구한다.
# 해당 결과에서의 0의 개수가 최대가 되는 경우를 남겨놓는다.

# 바이러스가 상하좌우로 퍼지는 것을 dfs로 구현하였다.
# 바이러스가 퍼지는 것을 구현하는 방법과 기둥 3개를 선택하는 2차원 조합을 구현하는 것이 포인트이다.
# 처음에 바이러스를 호출하기 전에 바이러스가 있는 부분을 탐색하는 코드를 재귀함수 내에서 정의하려고 했는데 3중 for문이 나와 시간복잡도가 굉장히 커졌다.
# 미리 바이러스가 있는 부분을 리스트에 담아 해결하였다. 
# pypy3를 이용해야 통과

import copy
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
virus = []

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
ans = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            virus.append((i, j))
          
def spreadVirus(x, y, copyGraph):
    if copyGraph[x][y] == 2:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= 0 and ny >= 0 and nx < n and ny < m and copyGraph[nx][ny] == 0:
                copyGraph[nx][ny] = 2
                spreadVirus(nx, ny, copyGraph)
  
def dfs(cnt, idx):
    global ans
    if cnt == 3:
        total = 0
        copyGraph = copy.deepcopy(graph)
        for x, y in virus:
            spreadVirus(x, y, copyGraph)
        for pos in copyGraph:
            total += pos.count(0)
        ans = max(total, ans)
        return
    
    for i in range(idx, n*m):
        x, y = i//m, i%m
        if graph[x][y] == 0:
            graph[x][y] = 1
            dfs(cnt+1, i+1)
            graph[x][y] = 0

dfs(0, 0)
print(ans)