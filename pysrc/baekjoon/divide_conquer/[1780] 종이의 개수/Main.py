import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
ans = dict()
for i in range(-1, 2):
    ans[i] = 0
    
def div(x, y, n):
    global ans
    num = paper[x][y]
    
    for i in range(x, x+n):
        for j in range(y,  y+n):
            if num != paper[i][j]:
                half = n // 3
                div(x, y, half)
                div(x+half, y, half)
                div(x+2*half, y, half)
                div(x, y+half, half)
                div(x, y+2*half, half)
                div(x+half, y+half, half)
                div(x+half, y+2*half, half)
                div(x+2*half, y+half, half)
                div(x+2*half, y+2*half, half)
                return
            
    ans[num] += 1

div(0, 0, n)

for cnt in ans.values():
    print(cnt)