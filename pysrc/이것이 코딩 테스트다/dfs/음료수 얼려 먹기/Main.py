# 각각의 원소를 하나씩 지나가면서 dfs을 한다
# 상하좌우로 각각 dfs를 재귀하면서 방문하지 않은 곳을 방문하며 1로 방문표시를 한다
# 더 이상 방문할 곳이 없다면 재귀 탈출


n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

ans = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            ans += 1

print(ans)