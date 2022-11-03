# n개의 자연수 중 중복되는 수가 있는 경우의 순열을 구하는 문제이다.
# 중복되는 수를 출력하지 않게 하는 것이 포인트인 문제이다.
# 중복되는 수를 출력하지 않게 이전 값을 기억해서 다음 값과 같으면 건너뛴다.

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [0]*n
q = []

def dfs(cnt):
    if cnt == m:
        print(" ".join(q))
        return
    
    overlap = 0
    
    for i in range(n):
        if not visited[i] and nums[i] != overlap:
            visited[i] = 1
            q.append(str(nums[i]))
            overlap = nums[i]
            dfs(cnt+1)
            visited[i] = 0
            q.pop()

dfs(0)