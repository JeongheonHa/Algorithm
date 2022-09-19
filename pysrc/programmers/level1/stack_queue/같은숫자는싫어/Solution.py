class Solution:
    def solution(arr):
        return [arr[i] for i in range(len(arr)) if [arr[i]] != arr[i+1:i+2]]