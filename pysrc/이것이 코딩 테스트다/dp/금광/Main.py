import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    arr = list(map(int, input().split()))

    d = []
    idx = 0
    for i in range(n):
        d.append(arr[idx:idx+m])
        idx += m
        
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = d[i-1][j-1]
            # 왼쪽 아래에서 오는 경우
            if i == n-1:
                left_down = 0
            else:
                left_down = d[i+1][j-1]
            # 왼쪽에서 오는 경우
            left = d[i][j-1]
            d[i][j] = d[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n):
        result = max(result, d[i][m-1])
        
    print(result)