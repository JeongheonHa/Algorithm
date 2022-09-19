class Solution:
    def solution(nums):
        count = 0
        count = len(set(nums))
        if len(nums) / 2 > count:
            return count
        else:
            return len(nums)/2
        
        # 다른 사람 풀이
        # return min(len(nums)/2, len(set(nums)))