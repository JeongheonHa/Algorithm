import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lines = []
for _ in range(k):
    lines.append(int(input()))
lines.sort()

ans = 0
def binarySearch(arr, start, end):
    global ans
    while start <= end:
        mid = (start+end)//2
        
        cnt = 0
        for i in range(k):
            cnt += arr[i]//mid
        
        if cnt >= n:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1

binarySearch(lines, 1, lines[-1])
print(ans)

