import sys
import heapq
input = sys.stdin.readline

n = int(input())
pos, neg = [], []
sum_val = 0
for _ in range(n):
    num = int(input())
    if num > 1:
        heapq.heappush(pos, -num)
    elif num == 1:
        sum_val += num
    else:
        heapq.heappush(neg, num)    

while len(pos) > 1:
    num1 = -heapq.heappop(pos)
    num2 = -heapq.heappop(pos)
    sum_val += num1*num2

if len(pos) == 1:
    num3 = -heapq.heappop(pos)
    sum_val += num3

while len(neg) > 1:
    num1 = heapq.heappop(neg)
    num2 = heapq.heappop(neg)
    sum_val += num1*num2

if len(neg) == 1:
    num3 = heapq.heappop(neg)
    sum_val += num3

print(sum_val)