# 두 개의 팀으로 나눈다.
# 각 팀의 s(i,j)와 s(j,i)의 값을 모두 더한다.
# 각 팀의 값의 차가 최소가 되는 값을 구한다. 

import sys


def dfs(cnt, idx):
    global ans
    if cnt == n//2:
        s_team, l_team = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] == 0 and visited[j] == 0:
                    s_team += arr[i][j]
                elif visited[i] == 1 and visited[j] == 1:
                    l_team += arr[i][j]
        ans = min(ans, abs(s_team - l_team))
        return 
    
    # 팀 구성하기
    for i in range(idx, n): # idx는 dfs로 인스턴스들이 넘어오기 전의 값을 기억해서 그 값보다 작은 수의 범위는 탐색하지 않게하기위해 필요하다.
        if visited[i] == 0:
            visited[i] = 1
            dfs(cnt+1, idx+1)
            visited[i] = 0
        
                
n = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [0]*n
ans = int(1e9)
dfs(0, 0)
print(ans)