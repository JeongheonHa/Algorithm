n, m = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0

def binarySearch(arr, start, end, target):
    global ans
    while start <= end:
        total = 0
        mid = (start+end)//2
        
        for x in arr:
            if x > mid:
                total += x-mid
    
        if total < target:
            end = mid-1
        else:
            ans = mid
            start = mid+1

binarySearch(arr, 0, max(arr), m)
print(ans)