# 2차원 그래프에서 (1,1)에서 (r,c)까지 각 칸의 합이 최대가 되도록 하는 path를 구하는 문제이다.
# r이 짝수이고 c가 짝수 일때 반드시 한칸을 제외해야하며 이 점을 고려하여 구현하는 것이 포인트이다.

import sys
input = sys.stdin.readline

r, c = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(r)]

if r % 2 != 0:
    print(('R' * (c - 1) + 'D' + 'L' * (c - 1) + 'D') * (r // 2) + 'R' * (c - 1))
elif c % 2 != 0:
    print(('D' * (r - 1) + 'R' + 'U' * (r - 1) + 'R') * (c // 2) + 'D' * (r - 1))
elif r % 2 == 0 and c % 2 == 0:
    low = 1000
    pos = [-1, -1]

    # 최솟값 칸 찾기
    for i in range(r):
        if i % 2 == 0:
            for j in range(1, c, 2):
                if low > ground[i][j]:
                    low = ground[i][j]
                    pos = [i, j]
        else:
            for j in range(0, c, 2):
                if low > ground[i][j]:
                    low = ground[i][j]
                    pos = [i, j]

    path = ('D' * (r - 1) + 'R' + 'U' * (r - 1) + 'R') * (pos[1] // 2)
    x = 2 * (pos[1] // 2)
    y = 0
    xbound = 2 * (pos[1] // 2) + 1

    while x != xbound or y != r - 1:
        if x < xbound and [y, xbound] != pos:
            x += 1
            path += 'R'
        elif x == xbound and [y, xbound - 1] != pos:
            x -= 1
            path += 'L'
        if y != r - 1:
            y += 1
            path += 'D'

    path += ('R' + 'U' * (r - 1) + 'R' + 'D' * (r - 1)) * ((c - 1 - pos[1]) // 2)

    print(path)
