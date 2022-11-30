import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n = int(input())
myCards = sorted(list(map(int, input().split())))
m = int(input())
checks = list(map(int, input().split()))
ans = []

def countByRange(arr, val):
    leftIdx = bisect_left(arr, val)
    rightIdx = bisect_right(arr, val)
    return rightIdx-leftIdx

for check in checks:
    ans.append(countByRange(myCards, check))

print(*ans)