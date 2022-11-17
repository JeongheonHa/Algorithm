# 동전 문제와 유사한 문제이다.
# 미리 제곱수의 리스트를 만들어 n까지의 수에 대입하여 최소 개수를 갱신해나간다.

from math import sqrt
import sys
input = sys.stdin.readline

n = int(input())

d = [100001]*(n+1)

arr = []
for i in range(1, int(sqrt(n))+1):
    arr.append(i*i)
d[0] = 0
d[1] = 1
for i in range(int(sqrt(n))):
    for j in range(arr[i], n+1):
        d[j] = min(d[j], d[j-arr[i]]+1)
    
print(d[n])