def count_by_value(arr, target):
    n = len(arr)
    
    a = first(arr, 0, n-1, target)
    
    if a == None:
        return 0
    
    b = last(arr, 0, n-1, target)
    
    return b-a+1

def first(arr, start, end, target):
    if start > end:
        return None
    
    mid = (start+end)//2
    
    if (mid == 0 or target > arr[mid-1]) and arr[mid] == target:
        return mid
    elif arr[mid] >= target:
        return first(arr, start, mid-1, target)
    else:
        return first(arr, mid+1, end, target)

def last(arr, start, end, target):
    if start > end:
        return None
    
    mid = (start+end)//2
    
    if (mid == n-1 or target < arr[mid+1]) and arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return last(arr, start, mid-1, target)
    else:
        return last(arr, mid+1, end, target)
    

n, target = map(int, input().split())
arr = list(map(int, input().split()))

cnt = count_by_value(arr, target)

if cnt == 0:
    print(-1)
else:
    print(cnt)