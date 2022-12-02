import sys
n = int(input())
ans = [[" "]*n for _ in range(n)]

def dfs(x, y, size):
    if size == 1:
        ans[x][y] = '*'
        return 
            
    half = size//3
    dfs(x, y, half)
    dfs(x, y+half, half)
    dfs(x, y+2*half, half)
    dfs(x+half, y, half)
    dfs(x+half, y+2*half, half)
    dfs(x+2*half, y, half)
    dfs(x+2*half, y+half, half)
    dfs(x+2*half, y+2*half, half)

dfs(0, 0, n)

for i in range(n):
    print("".join(ans[i]))