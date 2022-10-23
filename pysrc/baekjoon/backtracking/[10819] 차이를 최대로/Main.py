# n개의 원소의 모든 순열을 dfs로 구한다.
# used에 순열이 꽉 차면 모든 앞뒤 원소 차의 절대값의 합을 구한다.
# 모든 순열의 합 중에서 가장 큰 합을 출력

def dfs(used, visited):
    global ans
    if len(used) == n:
        total = 0
        for i in range(n-1):
            total += abs(used[i] - used[i+1])
        ans = max(total, ans)
        return 
        
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            used.append(arr[i])
            dfs(used, visited)
            visited[i] = 0
            used.pop()
        
n = int(input())
arr = list(map(int, input().split()))
visited = [0]*n
ans = 0
dfs([], visited)
print(ans)