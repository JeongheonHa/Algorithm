import sys
input = sys.stdin.readline


n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)] 

ans = dict()
for i in range(2):
    ans[i] = 0

def dfs(x, y, n):
    color = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]:
                half = n//2
                dfs(x, y, half)
                dfs(x, y+half, half)
                dfs(x+half, y, half)
                dfs(x+half, y+half, half)
                return
    ans[color] += 1

dfs(0, 0, n)
print(ans[0])
print(ans[1])