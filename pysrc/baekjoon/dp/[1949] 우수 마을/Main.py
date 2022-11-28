import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
village = [0] + list(map(int, input().split()))

tree = [[] for _ in range(n+1)]
visited = [False]*(n+1)
dp = [[0,village[i]] for i in range(n+1)]
    
for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)
    
def dfs(parent):
    visited[parent] = True
    for child in tree[parent]:
        if not visited[child]:
            dfs(child)
            dp[parent][0] += max(dp[child][0], dp[child][1])
            dp[parent][1] += dp[child][0]

dfs(1)
print(max(dp[1][0], dp[1][1]))