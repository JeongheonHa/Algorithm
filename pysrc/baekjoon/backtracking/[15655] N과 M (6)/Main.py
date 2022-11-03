# 무작위 수의 조합을 구하는 문제이다.
# visited의 한 칸마다 nums[i]로 지정하는 것이 포인트인 문제이다.
# 실제 수를 visited의 인덱스로 지정할 수 도 있지만 그렇게 한다면 for 문을 nums의 max값으로 지정해야하기 때문에 연산 수가 더 증가한다.

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [0]*(n)
q = []

def dfs(cnt, idx):
    if cnt == m:
        print(" ".join(q))
        return
    
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = 1
            q.append(str(nums[i]))
            dfs(cnt+1, i+1)
            q.pop()
            visited[i] = 0

dfs(0, 0)
            