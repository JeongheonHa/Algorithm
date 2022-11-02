# combination을 백트래킹으로 구현하는 문제이다.
# dfs(cnt+1, i+1)에서 idx가 아니라 i (실수하지말자)
# 수가 불규칙할 경우 visited를 사용해야하기 때문에 참고하는 의미에서 visited를 사용

n, m = map(int, input().split())
visited = [0]*(n+1)
q = []
def dfs(cnt, idx):
    if cnt == m:
        print(" ".join(q))
        return
    
    for i in range(idx, n+1):
        if visited[i] == 0:
            visited[i] = 1
            q.append(str(i))
            dfs(cnt+1, i+1)
            visited[i] = 0
            q.pop()

dfs(0, 1)