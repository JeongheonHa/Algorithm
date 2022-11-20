# dp만을 활용한 LIS의 시간복잡도는 O(n^2)이기때문에 시간초과가 난다.
# 따라서 기존의 LIS를 구할때 1~i-1까지의 LIS의 길이를 구할 때 발생하는 n만큼의 시간을 이진 탐색을 이용하여 줄일 수 있다.
# dp[i] : LIS의 원소들 (실제 LIS가 아닐 수 있으며 LIS가 아닌 다른 원소들로 채워질 수 있다. 하지만 길이는 같다.)


import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

d = [A[0]]

for i in range(n):
    if A[i] > d[-1]:
        d.append(A[i])
    else:
        idx = bisect_left(d, A[i])
        d[idx] = A[i]

print(len(d))