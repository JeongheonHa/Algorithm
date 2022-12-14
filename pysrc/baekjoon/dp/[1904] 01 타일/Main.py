# n이 100만이기 때문에 O(n)이상의 알고리즘이 필요하다.
# i-1타일과 i-2타일의 경우의 수에서 타일을 추가하는 것이 i 번째의 타일의 모든 경우의 수가 된다. (피보나치 수열)

# 1 : 1
# 2 : 00, 11
# 3 : 100, 001, 111
# 4 + 0000, 0011, 1100, 1001, 1111

import sys
input = sys.stdin.readline


n = int(input())

d = [0]*(1000001)
d[1] = 1
d[2] = 2
for i in range(3, n+1):
    d[i] = (d[i-1] + d[i-2]) % 15746
    
print(d[n])