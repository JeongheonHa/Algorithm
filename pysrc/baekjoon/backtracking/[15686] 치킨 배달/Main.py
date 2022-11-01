# 백트래킹을 이용해 m개의 치킨 집의 combination을 구하는 것이 포인트이다.
# 각각의 집마다 가장 가까운 치킨집과의 거리를 구한다.
# 모든 조합을 실행하여 총합이 가장 적은 것을 출력한다.


import sys
input = sys.stdin.readline

n, m = map(int, input().split())

house, chicken, chicken_list = [], [], []
ans = int(1e9)

for i in range(n):
    graph = list(map(int, input().split()))
    for j in range(n):
        if graph[j] == 2:
            chicken.append((i,j))
        if graph[j] == 1:
            house.append((i,j))

visited = [0]*len(chicken)

def dfs(depth, idx):
    global ans
    if depth == m:
        total = 0
        for i, j in house:
            val = int(1e9)
            for x, y in chicken_list: 
                tmp = abs(i-x) + abs(j-y) 
                val = min(tmp, val) 
            total += val 
        ans = min(ans, total)
        return

    for i in range(idx, len(chicken)): 
        if visited[i] == 0:
            visited[i] == 1
            chicken_list.append(chicken[i])
            dfs(depth+1, i+1)
            visited[i] == 0
            chicken_list.pop()
        
dfs(0, 0)
print(ans)