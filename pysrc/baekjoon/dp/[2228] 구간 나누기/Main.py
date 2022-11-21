import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp1 = [[0]+[-1e9]*m for i in range(n+1)]
dp2 = [[0]+[-1e9]*m for i in range(n+1)]

for i in range(1, n+1):
    num = int(input())
    for j in range(1, m+1):
        dp1[i][j]= max(dp2[i-1][j], dp1[i-1][j])
        dp2[i][j]= max(dp2[i-1][j], dp1[i-1][j-1]) + num
        
print(max(dp1[n][m], dp2[n][m]))
