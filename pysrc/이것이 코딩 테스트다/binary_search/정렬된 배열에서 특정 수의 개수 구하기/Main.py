import sys
import bisect
input = sys.stdin.readline


n, target = map(int, input().split())
arr = list(map(int, input().split()))

leftIdx = bisect.bisect_left(arr, target)
rightIdx = bisect.bisect_right(arr, target)

if leftIdx == rightIdx:
    print(-1)
else:
    print(rightIdx - leftIdx)
