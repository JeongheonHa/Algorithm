import sys
input = sys.stdin.readline

n = int(input())

d = [1]*10

for _ in range(2, n+1):
    for j in range(1, 10):
        d[j] = d[j-1] + d[j]
        
print(sum(d)%10007)