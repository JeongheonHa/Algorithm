import sys
input = sys.stdin.readline

n, m = map(int, input().split())

candy = []
for _ in range(n):
    candy.append(list(map(int, input().split())))
    
d = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        d[i][j] = max(d[i-1][j], d[i][j-1], d[i-1][j-1]) + candy[i-1][j-1]

print(d[n][m])