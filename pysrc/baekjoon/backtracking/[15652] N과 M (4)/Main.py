# 중복을 혀용하는 비 내림차순 수열을 구하는 문제이다.
# 다음 값은 이전 값 보다 커야한다.

n, m = map(int, input().split())
q = []

def dfs(cnt, idx):
    if cnt == m:
        print(" ".join(q))
        return
    
    for i in range(idx, n+1):   
        q.append(str(i))
        dfs(cnt+1, i)   # 1부터 시작이 아닌 idx위치에서 시작함으로 이전 값보다 큰 값이 된다. (여기서 +1을 하면 조합이 된다.)
        q.pop()
        
dfs(0, 1)