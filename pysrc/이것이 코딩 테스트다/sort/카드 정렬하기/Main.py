import sys
input = sys.stdin.readline
import heapq

n = int(input())

q = []
for _ in range(n):
    heapq.heappush(q, int(input()))
    
ans = 0
while len(q) != 1:
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    sum_val = a + b
    ans += sum_val
    heapq.heappush(q, sum_val)

print(ans)