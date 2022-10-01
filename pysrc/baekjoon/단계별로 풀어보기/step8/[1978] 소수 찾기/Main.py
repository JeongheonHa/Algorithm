n = int(input())
nums = map(int, input().split(" "))
cnt = 0

for num in nums:
    if num > 1:
        for i in range(2, num+1):
            if num % i == 0 and num != i:
                break
            if num == i:
                cnt += 1
            
print(cnt)