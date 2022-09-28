from typing import List


class Solution:
    def twoSum(nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i, num in enumerate(nums):
            num_map[num] = i

        for i, num in enumerate(nums):
            if target - num in num_map and i != num_map[target - num]:
                return [i, num_map[target - num]]