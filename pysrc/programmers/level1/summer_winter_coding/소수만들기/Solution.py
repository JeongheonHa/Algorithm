from itertools import combinations
from math import sqrt


def is_prime_number(x):
    for i in range(2, int(sqrt(x))+1):
        if x % i == 0:
            return False
    return True

class Solution:
    def solution(nums):
        answer = 0
        for x in combinations(nums, 3):
            if is_prime_number(sum(x)):
                answer += 1

        return answer