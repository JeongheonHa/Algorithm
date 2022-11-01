# 사다리에 놓을 수 있는 m의 모든 경우의 수를 dfs에 넣고 재귀할 경우 불필요한 연산을 하게된다.
# 따라서, case에 미리 불필요한 부분을 제거한 경우의 수를 넣어 case를 dfs에 넣고 재귀한다.
# dfs로는 사다리를 놓을 수 있는 모든 경우의 수를 구한다. (사다리는 연속으로 놓을 수 없다.)
# cnt가 3을 넘거나 check가 True면 탈출
# check는 i에서 시작해서 i로 끝나는지를 확인한다.


import sys
input = sys.stdin.readline


n, m, h = map(int, input().split())
visited = [[False] * (n+1) for _ in range(h+1)]
case = []
for _ in range(m):
    a, b = map(int, input().split())
    visited[a][b] = True

def check():
    for i in range(1, n+1):
        pos = i
        for j in range(1, h+1):
            if visited[j][pos-1]:
                pos -= 1
            elif visited[j][pos]:
                pos += 1
        if pos != i:
            return False
    return True

def dfs(cnt, idx):
    global ans
    if cnt > 3:
        return
    if check():
        ans = min(ans, cnt)
        return

    for c in range(idx, len(case)):
        x, y = case[c]
        if not visited[x][y-1] and not visited[x][y+1]:
            visited[x][y] = True
            dfs(cnt+1, c+1)
            visited[x][y] = False

for i in range(1,h+1):
    for j in range(1, n):
        if not visited[i][j-1] and not visited[i][j] and not visited[i][j+1]:
            case.append((i, j))

ans = 4
dfs(0, 0)

print(ans if ans < 4 else -1)