import sys
input = sys.stdin.readline
INF = sys.maxsize


n = int(input())
adj = []
for i in range(n):
    adj.append(list(map(int, input().split())))
   
for k in range(n):
    for a in range(n):
        for b in range(n):
            if adj[a][k] and adj[k][b]:
                adj[a][b] = 1

for i in range(n):
    print(*adj[i])