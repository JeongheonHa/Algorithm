# 딕셔너리가 더 빠르다.

import sys
input = sys.stdin.readline

n = int(sys.stdin.readline())
cards = list(map(int, input().split()))
n = int(sys.stdin.readline())
checks = list(map(int, input().split()))

ans = dict()
for card in cards:
    ans[card] = 0

for check in checks:
    if check not in ans:
        print(0, end=' ')
    else:
        print(1, end=' ')