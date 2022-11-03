# 무작위 수의 순열을 구하는 문제이다.

n, m = map(int, input().split())

nums = sorted(list(map(int, input().split())))
visited = [0]*(max(nums)+1)
q = []

def dfs (cnt):
    if cnt == m:
        print(" ".join(q))
        return
        
    for num in nums:
        if not visited[num]:
            q.append(str(num))
            visited[num] = 1
            dfs(cnt+1)
            q.pop()
            visited[num] = 0

dfs(0)