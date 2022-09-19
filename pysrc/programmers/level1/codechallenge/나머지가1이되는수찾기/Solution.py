class Solution:
    def solution(n):
        a = [ x for x in range(1,n) if n > 2 and n % (x) == 1]
        a.sort()
        return a[0]