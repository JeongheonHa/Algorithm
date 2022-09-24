class Solution:
    def solution(left, right):
        result = 0
        if left != 0:
            for num in range(left, right + 1):
                list = [i for i in range(1, num + 1) if num % i == 0] 
                
                if len(list) % 2 == 0:
                    result += num
                else:
                    result -= num
                    
            return result