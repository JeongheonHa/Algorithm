class Solution:
    def solution(lottos, win_nums):
        rank = [6, 6, 5, 4, 3, 2, 1]    # 맞춘 갯수를 인덱스로 활용해 순위 정의
        zero_count = lottos.count(0)
        count = 0
        
        for num in win_nums:    # 당첨 번호의 숫자를 하나하나 lottos에 비교
            if num in lottos:   # 있으면 +1
                count += 1
        return rank[count + zero_count], rank[count]    # 0의 개수만큼을 더 더한 것이 최대값