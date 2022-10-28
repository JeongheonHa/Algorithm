# 모든 강의를 수행해야하기 때문에 시작 시간을 기준으로 오름차순 정렬
# 시작 시간이 끝나는 시간보다 빠른 경우 강의실 하나 추가
# 시작 시간이 끝나는 시간보다 같거나 늦는 경우 해당 강의실에서 강의 진행
# 모든 강의실 중에서 가장 빨리 끝나는 강의를 대상으로 진행해야 하기 때문에 우선순위 큐 사용

import sys
import heapq


n = int(sys.stdin.readline().rstrip())
arr = sorted([tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)])

room = []
heapq.heappush(room, arr[0][1])

for i in range(1, n):
    if arr[i][0] < room[0]:
        heapq.heappush(room, arr[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, arr[i][1])

print(len(room))