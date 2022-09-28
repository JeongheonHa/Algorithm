import math


class Solution:
    def solution(n, m):
        result = []
        result.append(math.gcd(n, m))
        result.append(n * m / math.gcd(n, m))
        
        return result