# (1,1)에서 시작해서 칸 마다 가치를 합하여 (n, m)위치에 최대 가치의 합을 구하는 문제이다.
# 큰 문제 : (n, m)위치의 최대 가치의 합
# 작은 문제 : (i, j)위치의 최대 가치의 합
# (i, j)위치에 최대 가치를 구하기 위해서는 3방향으로 올 수 있는 모든 경우의 합을 구하여 그 중 최댓값을 dp에 저장한다.
# (1, 1)부터 시작하기 때문에 -> 방향으로 가는 경우 밖에 없으므로 dp에 누적합을 저장
# leftToRight : -> 방향으로 가면서 max(위에서 오는 가치, 왼쪽에서 오는 가치) + 현재 위치의 가치를 저장
# rightToLeft : <- 방향으로 가면서 max(위에서 오는 가치, 오른쪽에서 오는 가치) + 현재 위치의 가치를 저장
# d[i][j]에 max(leftToRight[j], rightToLeft[j])를 저장


import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, m):
    d[0][i] += d[0][i-1]

for i in range(1, n):
    leftToRight = d[i][:]
    rightToLeft = d[i][:]
    
    for j in range(m):
        if j == 0:
            leftToRight[j] += d[i-1][j]
        else:
            leftToRight[j] += max(d[i-1][j], leftToRight[j-1])
        
    for j in range(m-1, -1, -1):
        if j == m-1:
            rightToLeft[j] += d[i-1][j]
        else:
            rightToLeft[j] += max(d[i-1][j], rightToLeft[j+1])
    
    for j in range(m):
        d[i][j] = max(leftToRight[j], rightToLeft[j])

print(d[n-1][m-1])