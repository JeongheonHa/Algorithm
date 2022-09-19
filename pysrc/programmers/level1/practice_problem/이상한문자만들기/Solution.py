class Solution:
    def solution(s):
        answer = ''
        list = s.split(' ')
        
        for str in list:
            for i in range(len(str)):
                if i % 2 == 0:
                    answer += str[i].upper()
                else:
                    answer += str[i].lower()
            answer += ' '
            
        return answer[0:-1]

        # 다른 사람 풀이
        # return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))