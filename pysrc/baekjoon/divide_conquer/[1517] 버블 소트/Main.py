import sys
input = sys.stdin.readline


def mergeSort(arr):
    def div(left, right):
        if left >= right:
            return
        mid = (left+right)//2
        div(left, mid)
        div(mid+1, right)
        merge(left, mid, right)
        
    def merge(left, mid, right):
        global swap_cnt
        temp = []
        l, r = left, mid+1
        
        while l <= mid and r <= right:
            if arr[l] <= arr[r]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[r])
                r += 1
                swap_cnt += (mid-l+1)
        
        while l <= mid:
            temp.append(arr[l])
            l += 1
        while r <= right:
            temp.append(arr[r])
            r += 1
        
        for i in range(left, right+1):
            arr[i] = temp[i-left]
    return div(0, len(arr)-1)

n = int(input())
arr = list(map(int, input().split()))
swap_cnt = 0
mergeSort(arr)

print(swap_cnt)
    