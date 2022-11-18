import sys
input = sys.stdin.readline

n, k = map(int, input().split())
d = [[1]*(k+1) for _ in range(n+1)]

for i in range(1, k+1):
    for j in range(i+1, n+1):
        d[j][i] = (d[j-1][i-1] + d[j-1][i]) % 10007

print(d[n][k])