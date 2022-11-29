def solution(N, stages):
    answer = []
    rates = []
    length = len(stages)
    
    for stage in range(1, N+1):
        cnt = stages.count(stage)
        
        if length == 0:
            fail = 0
        else:
            fail = cnt / length
        
        length -= cnt
        
        rates.append((stage, fail))
        
    rates.sort(key = lambda x: -x[1])
    
    for rate in rates:
        answer.append(rate[0])
        
    return answer

if __name__ == "__main__":
    N = int(input())
    stages = list(map(int, input().split()))
    print(solution(N, stages))