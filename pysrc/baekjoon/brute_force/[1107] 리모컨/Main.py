# 처음 볼 땐 완전탐색이라고 생각 못했다.
# 다른 사람의 풀이를 보니 완전 탐색이라는 것일 깨달았다.
# n의 크기가 50만이지만 가장 근접한 채널을 구할 때는 문자열로 바꿔서 구하기 때문에 
# 안쪽 for문은 최대 len(nums)를 넘지 못한다.
# 따라서 시간복잡도는 O(n)이된다. 


import sys
input = sys.stdin.readline


n = int(input())
m = int(input())
brokenButton = list(map(int, input().split()))

minCnt = abs(100-n)
for nums in range(1000001):
    nums = str(nums)
    for i in range(len(nums)):
        if int(nums[i]) in brokenButton:
            break
        
        elif i == len(nums)-1:
            minCnt = min(minCnt, abs(int(nums)-n)+len(nums))

print(minCnt)