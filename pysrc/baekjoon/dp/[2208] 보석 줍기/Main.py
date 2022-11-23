# 구간합 + DP를 이용한 문제이다.
# 큰 문제 : 보석 m개 이상의 1개 구간의 최대합을 구하라
# 부분 문제 : max(0부터 i까지 최소 m개의 보석의 누적합 - min(0부터 i+m-1까지 누적합))


import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(int(input()))
    
val = 0
pSum = [0]
for i in range(n):
    val += arr[i]
    pSum.append(val)
    
ans, tmp = 0, 0
for i in range(m - 1, n):
    tmp = min(tmp, pSum[i - (m - 1)])
    ans = max(ans, pSum[i + 1] - tmp)
    
print(ans)