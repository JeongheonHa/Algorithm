def dfs(idx, sumOfNum):
    global n, s, graph
    cnt = 0				
    if idx == n:				
        return 0
    if sumOfNum + graph[idx] == s:			
        cnt += 1	
        			
    cnt += dfs(idx + 1, sumOfNum)			
    cnt += dfs(idx + 1, sumOfNum + graph[idx])	

    return cnt	

n, s = map(int, input().split())
graph = list(map(int, input().split()))

print(dfs(0, 0))

