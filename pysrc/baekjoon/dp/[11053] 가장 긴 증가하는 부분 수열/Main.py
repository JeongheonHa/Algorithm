# LIS를 구하는 문제이다.
# 큰 문제 : 수열 A에서 LIS의 길이
# 작은 문제 : 마지막으로 뽑는 수가 A[i]일 때의 LIS 길이
# A[i]이전의 LIS에서 A[i]를 붙인 부분 수열이 LIS라고 생각할 수 있다.
# 따라서 i보다 작은 위치에서 A[i]보다 작은 수가 마지막으로 오는 부분 수열의 LIS의 길이를 구하고 +1을 해주면된다.
# 시간복잡도 : O(n^2)


import sys
input = sys.stdin.readline


n = int(input())

A = list(map(int, input().split()))

d = [1]*(n+1)

for i in range(n):
    for j in range(i):
        if A[j] < A[i]:
            d[i] = max(d[i], d[j]+1)

print(max(d))