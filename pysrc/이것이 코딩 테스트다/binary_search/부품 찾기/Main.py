n = int(input())
items = sorted(list(map(int, input().split())))
m = int(input())
buy = list(map(int, input().split()))

def binarySearch(arr, start, end, target):
    if start > end:
        return "no"
    
    mid = (start+end)//2
    
    if arr[mid] == target:
        return "yes"
    elif target > arr[mid]:
        return binarySearch(arr, mid+1, end, target)
    elif target < arr[mid]:
        return binarySearch(arr, start, mid-1, target)
    
for item in buy:
    print(binarySearch(items, 0, len(items)-1, item), end = " ")