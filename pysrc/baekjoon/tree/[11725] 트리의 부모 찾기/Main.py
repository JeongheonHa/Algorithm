import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


n = int(input())
tree = [[] for _ in range(n+1)]
visited = [False]*(n+1)
parents = [0]*(n+1)

for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)
    
def dfs(parent):
    visited[parent] = True
    for child in tree[parent]:
        if not visited[child]:
            dfs(child)
            parents[child] = parent
    
dfs(1)
for child in range(2, n+1):
    print(parents[child])
