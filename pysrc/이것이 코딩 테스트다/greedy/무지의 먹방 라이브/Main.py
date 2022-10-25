# 전체를 다 돌면서 확인하는 방법은 정확성은 통과했지만 효율성은 통과하지 못했다.
# 다 먹는데 걸리는 시간을 최소힙 우선순위 큐에 넣는다.
# 하나씩 꺼내면서 다 먹는데 걸리는 시간을 합한다.
# 합한 값이 방송이 중단된 시간보다 크다면 합하지 않고 다시 순서를 기준으로 오름차순 정렬하여 다음으로 먹을 음식을 구한다.

import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))
        
    length = len(food_times)    # 남은 음식의 개수
    prev = 0                    # 직전에 다 먹은 음식 시간
    sum_val = 0                 # 먹기 위해 사용한 시간
    
    while sum_val + ((q[0][0] - prev)*length) <= k:
        now = heapq.heappop(q)[0]
        sum_val += (now-prev)*length
        length -= 1
        prev = now
        
    ans = sorted(q, key = lambda x: x[1])
    return ans[(k-sum_val)%length][1]