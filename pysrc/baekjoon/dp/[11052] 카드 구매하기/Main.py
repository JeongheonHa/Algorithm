# 동전 문제와 비슷한 유형의 문제이다.
# n개의 카드가 최대 1000개이고 1~n까지의 카드를 최대의 금액으로 알맞게 받아 n개를 맞춰야하기 때문에 최대 O(n^2)의 시간 복잡도를 갖는다.


import sys
input = sys.stdin.readline

n = int(input())
p = [0] + list(map(int, input().split()))

d = [-1]*(n+1)
d[0] = 0

for i in range(1, len(p)):
    for j in range(i, n+1):
        d[j] = max(d[j], d[j-i]+p[i])

print(d[n])