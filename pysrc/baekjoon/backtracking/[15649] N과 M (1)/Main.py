# permutation을 백트래킹을 이용해 구현하는 문제이다.


n, m = map(int, input().split())
visited = [0]*(n+1)
q = []
def dfs(cnt):
    if cnt == m:
        print(" ".join(q))
        return
    
    for i in range(1, n+1):
        if visited[i] == 0:
            visited[i] = 1
            q.append(str(i))
            dfs(cnt+1)
            visited[i] = 0
            q.pop()

dfs(0)