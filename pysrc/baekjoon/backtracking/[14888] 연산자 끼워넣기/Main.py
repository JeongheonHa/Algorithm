import sys
input = sys.stdin.readline


def dfs(num, idx, add, sub, mul, div):
    global maxAns, minAns
    if idx == n:
        maxAns = max(num, maxAns)
        minAns = min(num, minAns)
        return
    
    if add > 0:
        dfs(num+nums[idx], idx+1, add-1, sub, mul, div)
    if sub > 0:
        dfs(num-nums[idx], idx+1, add, sub-1, mul, div)
    if mul > 0:
        dfs(num*nums[idx], idx+1, add, sub, mul-1, div)
    if div > 0:
        dfs(int(num/nums[idx]), idx+1, add, sub, mul, div-1)

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    a, b, c, d = map(int, input().split())
    maxAns = -1e9
    minAns = 1e9
    dfs(nums[0], 1, a, b, c, d)
    print(maxAns)
    print(minAns)