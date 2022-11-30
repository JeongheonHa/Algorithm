import sys
input = sys.stdin.readline


n, c = map(int, input().split())

houses = []
for _ in range(n):
    houses.append(int(input()))
    
houses.sort()

ans = 0
def binarySearch(arr, start, end):
    global ans
    while start <= end:
        mid = (start+end)//2
        cnt = 1
        val = arr[0]
        for i in range(1, n):
            if arr[i] >= val + mid:
                val = arr[i]
                cnt += 1
        
        if cnt >= c:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1

binarySearch(houses, 1, houses[-1] - houses[0])
print(ans)