# bfs로 풀 경우 이미 갔던 지점을 다시 방문해야하기 때문에 q에 들어가는 데이터가 굉장히 커지기 떄문에 메모리 초과와 시간 초과가 날 것이라고 생각했다.
# dp 테이블을 이용해서 (i, j)까지 갈 수 있는 경로의 갯수를 dp테이블에 cnt하면서 (n, m)까지 내려온다.
# dp[i][j] : (i, j)위치까지의 경로의 갯수


import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
d = [[0]*n for _ in range(n)]
d[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            break
        r = i + graph[i][j]
        c = j + graph[i][j]
        
        if r < n:
            d[r][j] += d[i][j]
        if c < n:
            d[i][c] += d[i][j]

print(d[n-1][n-1])