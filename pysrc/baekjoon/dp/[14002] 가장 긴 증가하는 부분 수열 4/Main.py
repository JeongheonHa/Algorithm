# 역순으로 돌면서 d[i]가 LIS의 길이와 같아지는 A의 원소를 찾아 저장한다.
# 다시 reverse해서 순차적으로 출력하면 된다.

import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

d = [1]*n

for i in range(n):
    for j in range(i):
        if A[i] > A[j]:
            d[i] = max(d[i], d[j]+1)

print(max(d))

x = max(d)

ans = []
for i in range(n-1, -1, -1):
    if d[i] == x:
        ans.append(A[i])
        x -= 1

ans.reverse()

for num in ans:
    print(num, end = " ")