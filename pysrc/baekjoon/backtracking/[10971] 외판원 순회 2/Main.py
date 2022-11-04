# 전형적인 외판원 문제로 시간복잡도가 n!이기 때문에 n이 11이상이면 완전탐색으로 풀 수 없지만
# n이 11보다 작기 때문에 백트래킹을 이용한 완전탐색으로 풀 수 있다.
# 시작 노드를 이미 방문한 상태로 놓고 하나씩 돌면서 방문 기록을 해놓는데 마지막에 시작노드로 돌아오는 부분을 구현하는데 시간이 많이 걸렸다.

import sys
input = sys.stdin.readline


n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]
visited = [0]*n
ans = sys.maxsize

def dfs(start, next, total, cnt):
    global ans
    if cnt == n:
        if costs[next][start] != 0:
            ans = min(ans, total+costs[next][start])
        return
    
    for i in range(n):
        if not visited[i] and costs[next][i] != 0:
            visited[i] = 1
            dfs(start, i, total+costs[next][i], cnt+1)
            visited[i] = 0
            
for i in range(n):
    visited[i] = 1
    dfs(i, i, 0, 1)
    visited[i] = 0

print(ans)
