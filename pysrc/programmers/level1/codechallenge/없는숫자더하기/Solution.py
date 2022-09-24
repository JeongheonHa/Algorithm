class Solution:
    def solution(numbers):
        return sum([num for num in range(10)]) - sum([ num for num in numbers])