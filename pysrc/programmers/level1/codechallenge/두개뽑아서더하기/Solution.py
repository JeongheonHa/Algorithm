class Solution:
    def solution(numbers):
        # 배열의 서로 다른 인덱스를 뽑는다
        # 두 수를 더해서 리스트에 담아 정렬 후 반환
        result = []
        for i in range(len(numbers)):
            for j in range(1, len(numbers)):
                if i != j:
                    result.append(numbers[i] + numbers[j])
        return sorted(list(set(result)))
    
    # 다른 사람 풀이
    def solution(numbers):
        answer = []
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                answer.append(numbers[i] + numbers[j])
        return sorted(list(set(answer)))