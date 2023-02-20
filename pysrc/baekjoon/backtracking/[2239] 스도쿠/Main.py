import sys
input = sys.stdin.readline


def check(sx, sy, num):
    if graph[sx].count(num) != 0: return False
    for i in range(9):
        if graph[i][sy] == num: return False
        
    x = sx // 3
    y = sy // 3
    
    for i in range(x*3, x*3+3):
        for j in range(y*3, y*3+3):
            if i != sx and i != sy and graph[i][j] == num:
                return False
    
    return True
            
def dfs(cnt):
    global zero
    if cnt == zero:
        for i in range(9):
            print("".join(map(str, graph[i])))
        exit(-1)

    for num in range(1, 10):
        x = blank[cnt][0]
        y = blank[cnt][1]

        if check(x, y, num):
            graph[x][y] = num
            dfs(cnt+1)
            graph[x][y] = 0

graph = []
blank = []
zero = 0
for i in range(9):
    graph.append(list(map(int, input().rstrip())))
    zero += graph[i].count(0)
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i, j))
            
dfs(0)