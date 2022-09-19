class Solution:
    def solution(arr, divisor):
        return sorted([elem for elem in arr if elem % divisor == 0]) or [-1]