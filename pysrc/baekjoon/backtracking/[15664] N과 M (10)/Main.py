# n개의 자연수에 중복된 값이 있는 경우 비 내림차순으로 모든 순열을 구하는 문제이다.

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [0]*n
q = []

def dfs(cnt, idx):
    if cnt == m:
        print(" ".join(q))
        return
    
    overlap = 0
    
    for i in range(idx, n):
        if not visited[i] and overlap != nums[i]:
            visited[i] = 1
            q.append(str(nums[i]))
            overlap = nums[i]
            dfs(cnt+1, i)
            visited[i] = 0
            q.pop()

dfs(0, 0)