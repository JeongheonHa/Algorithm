n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
sub_sum = 0

def dfs(idx):
    global cnt, sub_sum

    if idx == n:
        return

    if sub_sum + arr[idx] == s:
        cnt += 1
         
    # 이번 원소를 포함시키지 않고 시도
    dfs(idx+1)
    
    # 이번 원소를 포함시키고 시도
    sub_sum += arr[idx]
    dfs(idx+1)

    sub_sum -= arr[idx]
    

dfs(0)
print(cnt)
