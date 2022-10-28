# 시작 시간과 끝나는 시간을 튜플의 형태 시간 테이블에 저장
# 끝나는 시간을 기준으로 오름차순 정렬하고 그 다음으로 시작 시간을 기준으로 오름차순 정렬한다.
# 결국 가장 빨리 끝나는 시간을 계속 선택하면 된다.
# 끝난 시간보다 크거나 같은 시작 시간 중에서 끝나는 시간이 가장 짧은 것을 계속 선택.

n = int(input())
time_table = sorted([tuple(map(int, input().split())) for _ in range(n)], key = lambda x: (x[1], x[0]))

cnt = 1
cnt = end = 0
for s, e in time_table:
    if s >= end:
        cnt += 1
        end = e

print(cnt)
