n = int(input())
d = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            left_up = 0
        else:
            left_up = d[i-1][j-1]
        if j == i:
            up = 0
        else:
            up = d[i-1][j]
            
        d[i][j] = d[i][j] + max(left_up, up)

print(max(d[n-1]))