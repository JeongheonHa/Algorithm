# 행렬간의 곱셈에 필요한 최소 연산 횟수를 구하는 문제이다.
# 행렬간의 곱셈의 연산은 괄호를 놓는 위치에 지배를 받는다.
# 따라서, d[i][j]에 i부터 j까지의 행렬의 곱셈 연산이 최소가 되는 연산을 기록한다.
# 이말은 즉, 연산 값이 최소가 되는 괄호의 위치를 저장하여 다음 값을 구할 때 해당 괄호가 적용된 값을 다시 사용하겠다는 말이다.
# 이것을 부분 문제로 표현하면 다음과 같다.
# d[i][j] = min(d[i][k] + d[k+1][j] + p[i]*p[k+1]*p[j+1]) for k in range(i, j-1) (if j >= i)


import sys
input = sys.stdin.readline
n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]

dp = [[0]*n for _ in range(n)]

for cnt in range(n-1):
    for i in range(n-1-cnt):
        j = i+cnt+1
        dp[i][j] = 2**31
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + matrix[i][0]* matrix[k][1]* matrix[j][1])

print(dp[0][-1])