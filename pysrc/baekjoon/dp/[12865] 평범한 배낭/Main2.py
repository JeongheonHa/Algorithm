# 평범한 배낭 문제 최적한 버전
# 제한 무게에서 거꾸로 올라가면서 실행하는 것이 포인트이다.
# 메모리와 시간 모두 절약된다.
# 시간 복잡도 : O(nk)

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = []

for _ in range(n):
	w, v = map(int, input().split())
	arr.append((w, v))
   
d = [0]*(k+1)

for item in arr:
    w, v = item
    for i in range(k, w - 1, -1):
        d[i] = max(d[i], d[i - w] + v)
    
print(d[-1])