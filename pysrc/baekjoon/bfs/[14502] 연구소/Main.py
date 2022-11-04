import sys
from collections import deque
import copy
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
virus = []
     
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for x in range(n):
    for y in range(m):
        if graph[x][y] == 2:
            virus.append((x, y))
                    
def spreadVirus(x, y, copyGraph):
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx <n and ny < m and copyGraph[nx][ny] == 0:
                q.append((nx, ny))
                copyGraph[nx][ny] = 2
             
ans = 0       
def dfs(cnt, idx):
    global ans
    if cnt == 3:
        total = 0
        copyGraph = copy.deepcopy(graph)
        for x, y in virus:
            spreadVirus(x, y, copyGraph)
        for col in copyGraph:
            total += col.count(0)
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