# 그래프 내의 사이클을 찾아내 사이클의 노드 개수를 구하는 것이 포인트이다.
# 사이클을 구하기 위해서 finished에 해당 노드의 호출 여부를 추가하여 방문 한적이 있고 호출된적이 없는 노드를 찾아야한다.
# 사이클이 생기는 지점을 알았다면 해당 지점으로부터 마지막으로 호출된 정점(here)과 만날 때 까지 cnt 


import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

t = int(input())

for _ in range(t):
    n = int(input())
    choice = [0] + list(map(int, input().split()))
    visited = [0]*(n+1)
    finished = [0]*(n+1)
    cnt = 0

    def dfs(here):
        global cnt
        visited[here] = 1
        next = choice[here]
        if visited[next] and not finished[next]:
            temp = next
            cnt += 1
            while temp != here:
                temp = choice[temp]
                cnt += 1
        elif not visited[next]:
            dfs(next)
        finished[here] = 1
            
    for here in range(1, n+1):
        if not visited[here]:
            dfs(here)
        
    print(n-cnt)