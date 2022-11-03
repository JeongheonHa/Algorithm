# 무작위 수를 비 내림차순으로 모든 순열을 구하는 문제이다.
# 이전 idx를 기억해서 해당 idx부터 탐색을 시작함으로써 이전 값보다 큰 값을 탐색한다.

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

q = []

def dfs(cnt, idx):
    if cnt == m:
        print(" ".join(q))
        return
    
    for i in range(idx, n):
        q.append(str(nums[i]))
        dfs(cnt+1, i)
        q.pop()
        
dfs(0, 0)
