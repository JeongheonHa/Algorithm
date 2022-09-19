class Solution:
    def solution(strings, n):
        # 리스트의 요소(문자열)의 n번째 단어를 기준으로 오름차순 정렬 후 리스트로 반환
        return sorted(strings, key = lambda x: (x[n], x[0:])) 
    
        # 다른 풀이
        return sorted(strings, key = lambda x: (x[n], x))