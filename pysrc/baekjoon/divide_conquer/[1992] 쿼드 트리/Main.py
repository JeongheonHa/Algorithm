# 4사분면 쿼드 트리 압축하기


import sys
input = sys.stdin.readline

n = int(input())
tree = [list(map(int, input().rstrip())) for _ in range(n)]
ans = []

def div(x,y,n):
    global ans
    color = tree[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != tree[i][j]:
                half = n // 2
                ans.append("(")
                div(x, y, half)
                div(x, y+half, half)
                div(x+half, y, half)
                div(x+half, y+half, half)
                ans.append(")")
                return
    ans.append(str(color))

div(0, 0, n)
print("".join(ans))