# 다이나믹 프로그래밍의 정말 유명한 유형의 알고리즘 문제인 LCS(최장 공통 부문자열)의 길이를 구하는 문제이다.
# 정리 1. 마지막 문자가 같은 경우 이전 문자들의 LCS길이에서 +1 한 것과 같다.
# 정리 2. 마지막 문자가 같지 않은 경우 x문자열의 i-1의 LCS길이와 y문자열의 j-1의 LCS길이 중 가장 긴 LCS길이가 해당 i, j의 LCS길이가 된다.

import sys
input = sys.stdin.readline

x = input().rstrip()
y = input().rstrip()
n = len(x)
m = len(y)

d = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if x[i-1] == y[j-1]:
            d[i][j] = d[i-1][j-1] + 1
        else:
            d[i][j] = max(d[i][j-1], d[i-1][j])

print(d[n][m])