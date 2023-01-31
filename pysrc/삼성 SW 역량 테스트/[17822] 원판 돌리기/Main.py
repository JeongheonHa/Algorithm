import sys
from collections import deque
input = sys.stdin.readline


def rotate(x, d, k):
    q = deque(graph[x])
    if d == 0:
        q.rotate(k)
    else:
        q.rotate(-k)
    graph[x] = list(q)

def simul():
    temp = []
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0: continue
            cnt += 1
            if graph[i][j] == graph[i][(j+1)%m]:
                temp.append((i, j))
                temp.append((i, (j+1)%m))

    for j in range(m):
        for i in range(n-1):
            if graph[i][j] == 0: continue
            if graph[i][j] == graph[i+1][j]:
                temp.append((i, j))
                temp.append((i+1, j))

    temp = list(set(temp))

    if len(temp) == 0:
        avg = total / cnt

        for i in range(n):
            for j in range(m):
                if graph[i][j] != 0 and graph[i][j] > avg:
                    graph[i][j] -= 1
                elif graph[i][j] != 0 and graph[i][j] < avg:
                    graph[i][j] += 1
                    
    for x, y in temp:
        graph[x][y] = 0

n, m, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
       
for _ in range(t):
    x, d, k = map(int, input().split())
    total = 0
    for i in range(n):
        total += sum(graph[i])
        if (i+1)%x == 0:
            rotate(i, d, k)
            
    if total == 0: break
    
    simul()
    
ans = 0
for i in range(n):
    for j in range(m):
        ans += graph[i][j]

print(ans)