# 무작위 수의 모든 중복 순열을 구하는 문제이다.

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

q = []

def dfs(cnt):
    if cnt == m:
        print(" ".join(q))
        return
    
    for num in nums:
        q.append(str(num))
        dfs(cnt+1)
        q.pop()
        
dfs(0)