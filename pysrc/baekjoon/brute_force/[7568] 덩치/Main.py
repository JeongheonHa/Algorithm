# 전형적인 완전 탐색 문제로 반복적으로 사람 한명을 순차적으로 모두와 비교해서 자신의 등수를 정한다.


n = int(input())
group = []
for _ in range(n):
    x, y = map(int, input().split())
    group.append((x, y))
    
for person in group:
    r = 1
    for someone in group:
        if person[0] < someone[0] and person[1] < someone[1]:
            r += 1
    print(r, end = " ")
        