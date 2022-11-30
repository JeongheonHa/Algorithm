import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
checks = list(map(int, input().split()))

cards.sort()

def binary_search(array, start, end, target):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


for i in range(m):
    if binary_search(cards, 0, n-1, checks[i]) != None:
        print(1, end=' ')
    else:
        print(0, end=' ')