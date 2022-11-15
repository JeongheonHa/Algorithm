# 가로가 20만 세로가 50만으로 제한 시간이 1초이기 때문에 O(n)이상의 알고리즘을 사용해야한다.
# 2차원 그래프를 이용하여 석순과 종유석이 있는 위치에 1을 넣어주면 쉽게 풀 수 있지만 결국 for문을 2번 돌려야하기 때문에 O(n^2)이 되고 만다.
# 따라서 하나의 배열을 이용해 모든 석순과 종유석을 표현하기 위해서는 누적 합 방식을 이용하면 될 것이라고 판단했다.
# up은 석순을 표현하고 down은 종유석을 표현
# up은 역순으로 누적 합을 구하고 down은 수순으로 누적 합을 구하여 같은 구간에 곂쳐있는 장애물을 표현
# 각 구간 별로 up과 down을 더해 충돌 횟수가 최소가 되는 값을 구한다.
# 해당 최솟값과 같은 값이 있으면 +1

n, h = map(int, input().split())

up = [0]*(h+1)
down = [0]*(h+1)
ans = n+1
for i in range(n):
    height = int(input())
    if i % 2 == 0:
        up[height] += 1
    else:
        down[height] += 1

for i in range(h-1, 0, -1):
    up[i] += up[i+1]
    down[i] += down[i+1]

for i in range(1, h+1):
    cnt = up[h-i+1] + down[i]
    if ans > cnt:
        ans = cnt
        scope = 1
    elif ans == cnt:
        scope += 1

print(ans, scope)