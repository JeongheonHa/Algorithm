n = int(input())
ans = [[" "]*(2*n) for _ in range(n)]


def dfs(x, y, size):
    if size == 3:
        ans[x][y] = "*"
        ans[x+1][y-1] = ans[x+1][y+1] = "*"
        for i in range(-2, 3):
            ans[x+2][y+i] = "*"
        return

    half = size//2
    dfs(x, y, half)
    dfs(x+half, y-half, half)
    dfs(x+half, y+half, half)
    
dfs(0, n-1, n)

for i in range(n):
    print("".join(ans[i]))