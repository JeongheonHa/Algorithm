# n의 크기가 10만이기 때문에 O(nlng n) 이상의 알고리즘으로 풀 수 있다.
# 최대값을 갖는 경우는 각 대각선의 1번째와 2번째 중 최대값을 선택하면된다.

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t) :
    n = int(input())
    dp = [list(map(int,input().split())) for _ in range(2)]

    if n > 1 :
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
    for i in range(2, n) :
        dp[0][i] += max(dp[1][i-1],dp[1][i-2])
        dp[1][i] += max(dp[0][i-1],dp[0][i-2])

    print(max(dp[0][n-1],dp[1][n-1]))