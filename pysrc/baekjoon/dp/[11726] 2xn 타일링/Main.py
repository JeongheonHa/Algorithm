# n까지의 모든 타일의 경우의 수는 n에 1x2타일을 놓는 경우 1개와 n과 n-1에 타일을 놓는 경우의 수 1개가 존재한다.
# 이 겻은 반대로 n에 1x2를 놓는 타일을 제외한 n-1까지 타일을 놓는 모든 경우의 수 + n-2까지 타일을 놓는 모든 경우의 수이다.

import sys
input = sys.stdin.readline

n = int(input())

d = [-1]*(1001)

d[1] = 1
d[2] = 2

for i in range(3, n+1):
    d[i] = (d[i-1] + d[i-2])%10007

print(d[n])
