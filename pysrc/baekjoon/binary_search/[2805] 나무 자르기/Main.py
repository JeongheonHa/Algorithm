# 파라메트릭 서치 유형

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = 0

def binarySearch(arr, start, end, target):
    global ans
    while start <= end:
        mid = (start+end)//2
        sum_val = 0
        for tree in arr:
            if tree > mid:
                sum_val += (tree-mid)
        
        if sum_val >= target:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1
        
binarySearch(arr, 0, arr[-1], m)
print(ans)