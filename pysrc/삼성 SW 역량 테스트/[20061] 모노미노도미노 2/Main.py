import sys
input = sys.stdin.readline


def checkBlue():
    global ans
    for j in range(2, 6):
        cnt = 0
        for i in range(4):
            if b[i][j]:
                cnt += 1

        if cnt == 4:
            removeBlue(j)
            ans += 1


def checkGreen():
    global ans
    for i in range(2, 6):
        cnt = 0
        for j in range(4):
            if g[i][j]:
                cnt += 1

        if cnt == 4:
            removeGreen(i)
            ans += 1


def removeBlue(idx):
    for j in range(idx, 0, -1):
        for i in range(4):
            b[i][j] = b[i][j-1]
    for i in range(4):
        b[i][0] = 0


def removeGreen(idx):
    for i in range(idx, 0, -1):
        for j in range(4):
            g[i][j] = g[i-1][j]
    for j in range(4):
        g[0][j] = 0


def moveBlue(t, x):
    y = 1
    if t == 1 or t == 2:
        while y+1 < 6 and b[x][y+1] == 0:
            y += 1
        
        b[x][y] = 1
        if t == 2:
            b[x][y-1] = 1


    if t == 3:
        while y+1 < 6 and b[x][y+1] == 0 and b[x+1][y+1] == 0:
            y += 1
            
        b[x][y] = 1
        b[x+1][y] = 1


    checkBlue()

    for j in range(2):
        for i in range(4):
            if b[i][j]:
                removeBlue(5)
                break


def moveGreen(t, y):
    x = 1
    if t == 1 or t == 3:
        while x+1 < 6 and g[x+1][y] == 0:
            x += 1
        g[x][y] = 1
        if t == 3:
            g[x-1][y] = 1


    if t == 2:
        while x+1 < 6 and g[x+1][y] == 0 and g[x+1][y+1] == 0:
            x += 1
        g[x][y] = 1
        g[x][y+1] = 1

    checkGreen()

    for i in range(2):
        for j in range(4):
            if g[i][j]:
                removeGreen(5)
                break


t = int(input())
b = [[0]*6 for _ in range(4)]
g = [[0]*4 for _ in range(6)]

ans = 0
for _ in range(t):
    t, x, y = map(int, input().split())
    moveBlue(t, x)
    moveGreen(t, y)

blueCnt, greenCnt = 0, 0

for i in range(4):
    for j in range(2, 6):
        if b[i][j]:
            blueCnt += 1
            
for i in range(2, 6):
    for j in range(4):
        if g[i][j]:
            greenCnt += 1

print(ans)
print(blueCnt + greenCnt)