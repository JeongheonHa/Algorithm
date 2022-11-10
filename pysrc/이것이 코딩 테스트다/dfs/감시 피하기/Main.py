import sys
input = sys.stdin.readline

n = int(input())
graph = []
teachers = []
for i in range(n):
    graph.append(list(input().split()))
    for j in range(n):
        if graph[i][j] == 'T':
            teachers.append((i, j))
            
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

success = False

def check(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        while nx >= 0 and ny >= 0 and nx < n and ny < n and graph[nx][ny] != 'O':
            if graph[nx][ny] == 'S':
                return True
            
            nx += dx[i]
            ny += dy[i]
            
    return False

def dfs(cnt, idx):
    global success
    if cnt == 3:
        teacher = 0
        for x, y in teachers:
            if not check(x, y):
                teacher += 1
        if teacher == len(teachers):
            success = True
        return
    
    for i in range(idx, n*n):
        x, y = i//n, i%n
        if graph[x][y] == 'X':
            graph[x][y] = 'O'
            dfs(cnt+1, i+1)
            graph[x][y] = 'X'

dfs(0, 0)

if success:
    print("YES")
else:
    print("NO")