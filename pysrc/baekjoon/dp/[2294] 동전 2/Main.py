import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

d = [100001]*(k+1)
d[0] = 0

for i in range(len(coins)):
    for j in range(coins[i], k+1):
        d[j] = min(d[j], d[j-coins[i]]+1)

if d[k] != 100001:
    print(d[k])
else:
    print(-1)