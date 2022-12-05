n = int(input())
arr = list(map(int, input().split()))

arr.sort()
sum_val = 0
pSum = [0]

for num in arr:
    sum_val += num
    pSum.append(sum_val)

print(sum(pSum))