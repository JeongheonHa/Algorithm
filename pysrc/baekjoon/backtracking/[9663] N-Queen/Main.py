# 제한 시간이 10초로 대략 1억번의 연산까지 허용하므로 백트래킹으로 풀 수 있을거라고 생각했다.
# 2차원 배열을 재귀할 때는 매개변수로 행을 넣고 for문을 이용해 모든 열을 탐색함으로써 구현할 수 있다.
# 각각의 pos가 같은 대각선에 위치하는지를 파악하는 것이 이 문제의 포인트이다.
# 오른쪽 대각선 방향에 일치하는 위치에 있는 좌표들은 (x, y)에서 x-y가 모두 같다.
# 왼쪽 대각선 방향에 일치하는 위치에 있는 좌표들은 (x, y)에서 x+y가 모두 같다.
# pypy3를 이용해야 통과 가능 (python3는 시간초과)

import sys
input = sys.stdin.readline


n = int(input())

visited1 = [0]*(n+n+1)
visited2 = [0]*(n+n+1)
visited3 = [0]*(n+n+1)
cnt = 0

def dfs(col):
    global cnt
    if col == n:
        cnt += 1
        return
    
    for row in range(n):
        if visited1[row] or visited2[col+row] or visited3[col-row+n-1]:
            continue
        visited1[row] = 1
        visited2[col+row] = 1
        visited3[col-row+n-1] = 1
        dfs(col+1)
        visited1[row] = 0
        visited2[col+row] = 0
        visited3[col-row+n-1] = 0

dfs(0)
print(cnt)