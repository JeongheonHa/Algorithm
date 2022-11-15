import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

sum_val = 0
pSum = [0]

for i in range(len(nums)):
    sum_val += nums[i]
    pSum.append(sum_val)
    
for _ in range(m):
    i, j = map(int, input().split())
    print(pSum[j]-pSum[i-1])