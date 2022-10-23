def dfs(used, visited):
    global ans
    total = 0
    if len(used) == 3:
        total += sum(used)
        if total <= m:
            ans = max(ans, total)
        return 
    
    for i in range(n):
        if visited[i] == 0:
            used.append(arr[i])
            visited[i] = 1
            dfs(used, visited)
            used.pop()
            visited[i] = 0

n, m = map(int, input().split())
arr = list(map(int, input().split()))
visited = [0]*n
ans = 0
dfs([], visited)
print(ans)