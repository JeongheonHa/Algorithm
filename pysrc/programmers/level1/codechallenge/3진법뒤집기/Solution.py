class Solution:
    def solution(n):
        result = ""
        # 3진법 상에서 앞 뒤로 뒤집기
        while n:
            n, r = divmod(n, 3)
            result += str(r)
        # 10진법으로 변환 후 리턴
        return int(result, 3)
        