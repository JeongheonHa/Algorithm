import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

cnt = 0
def dfs(x, y, size):
    global cnt
    if x == r and y == c:
        print(cnt)
        exit(0)
    
    if not x <= r < x+size or not y <= c < y+size:
        cnt += size * size
        return
    half = size//2
    dfs(x, y, half)
    dfs(x, y+half, half)
    dfs(x+half, y, half)
    dfs(x+half, y+half, half)

dfs(0, 0, 2**n)
    
    