import sys
input = sys.stdin.readline


def binarySearch(arr, start, end):
    if start > end:
        return None
    
    mid = (start+end)//2
    
    if arr[mid] == mid:
        return mid
    elif arr[mid] < mid:
        return binarySearch(arr, mid+1, end)
    else:
        return binarySearch(arr, start, mid-1)
    
n = int(input())
arr = list(map(int, input().split()))

ans = binarySearch(arr, 0, n-1)

if ans == None:
    print(-1)
else:
    print(ans)