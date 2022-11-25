# 0 ~ n까지의 정수 k개를 더해서 합이 n이 되는 경우의 수
# d[i][j]: j까지 정수 i개를 더해서 합이 n이 되는 경우의 수 (1 <= i <= k, 1 <= j <= n)
# k가 1인 경우 d[1][j] = 1
# n이 1인 경우 d[i][1] = j
# 점화식 : d[i][j] = d[i][j-1] + d[i-1][j]
# 시간 복잡도 : O(n^2)

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

d = [[0]*202 for _ in range(202)]

for i in range(1, k+1):
    d[j][1] = i
    
for j in range(1, n+1):
    d[1][j] = 1

for i in range(2, k+1):
    for j in range(2, n+1):
        d[i][j] = (d[i][j-1] + d[i-1][j])%1000000000
        
print(d[k][n])