# 원소가 0,1이면 +, 아니면 *

arr = list(map(int, input()))

ans = arr[0]
for i in range(1, len(arr)):
    if arr[i] <= 1 or ans <= 1:
        ans += arr[i]
    else:
        ans *= arr[i]
        
print(ans)