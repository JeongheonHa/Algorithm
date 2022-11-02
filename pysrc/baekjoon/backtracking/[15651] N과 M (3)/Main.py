# 중복 순열을 구하는 문제이다.
# 순열과 조합에는 visited를 이용해서 방문한 곳을 또 방문하지 못하게 했지만 중복을 허용하기 때문에 방문 정보를 기록하지 않아도 된다.

n, m = map(int, input().split())
q = []

def dfs(cnt):
    if cnt == m:
       print(" ".join(q))
       return
    
    for i in range(1, n+1):
        q.append(str(i))
        dfs(cnt+1)
        q.pop()

dfs(0)