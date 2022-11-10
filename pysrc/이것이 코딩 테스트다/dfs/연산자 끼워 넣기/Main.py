# dfs + 백트래킹 문제이다.
# 각 숫자를 정점으로 놓고 연산자를 간선으로 놓고 dfs를 한다.
# 모든 정점을 탐색 했을 때의 최대값과 최솟값을 갱신한다.


import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

max_num = -1e9
min_num = 1e9

def dfs(num, idx, plus, minus, mul, div):
    global max_num, min_num
    if idx == n:
        max_num = max(max_num, num)
        min_num = min(min_num, num)
        return
    
    if plus > 0:
        dfs(num+nums[idx], idx+1, plus-1, minus, mul, div)
    if minus > 0:
        dfs(num-nums[idx], idx+1, plus, minus-1, mul, div)
    if mul > 0:
        dfs(num*nums[idx], idx+1, plus, minus, mul-1, div)
    if div > 0:
        dfs(int(num/nums[idx]), idx+1, plus, minus, mul, div-1)

dfs(nums[0], 1, plus, minus, mul, div)

print(max_num)
print(min_num)

        