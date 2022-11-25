# 1, 2, 3의 합으로 나타내는 방법의 수
# d[i] : i의 경우의 수
# 피보나치 수열과 유사한 문제이다.

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    
    d = [0]*12
    d[1] = 1
    d[2] = 2
    d[3] = 4
    for i in range(4, n+1):
        d[i] = d[i-1] + d[i-2] + d[i-3]
    
    print(d[n])