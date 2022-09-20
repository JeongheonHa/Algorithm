class Solution:
    def solution(answers):
        result = []
        counts = [0, 0, 0]
        one = [1, 2, 3, 4, 5]
        two = [2, 1, 2, 3, 2, 4, 2, 5]
        three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
        # 각각 맞힌 횟수를 counts리스트에 추가
        for index, answer in enumerate(answers):
            if answer == one[index % len(one)]:
                counts[0] += 1
            if answer == two[index % len(two)]:
                counts[1] += 1
            if answer == three[index % len(three)]:
                counts[2] += 1
        # 최대값을 뽑아서 리스트로 반환
        for index, count in enumerate(counts):
            if count == max(counts):
                result.append(index + 1)
        return result