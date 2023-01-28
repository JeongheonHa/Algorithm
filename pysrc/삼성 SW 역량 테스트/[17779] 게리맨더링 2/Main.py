import sys
input = sys.stdin.readline


def solve(x, y, d1, d2):
    global ans
    visited = [[0]*(n+1) for _ in range(n+1)]
    people = [0]*6
    
    visited[x][y] = 5
    for i in range(1, d1+1):
        visited[x+i][y-i] = 5
        visited[x+d2+i][y+d2-i] = 5
    for i in range(1, d2+1):
        visited[x+i][y+i] = 5
        visited[x+d1+i][y-d1+i] = 5

    # 1
    for i in range(1, x+d1):
        for j in range(1, y+1):
            if visited[i][j] == 5:
                break
            else:
                people[1] += graph[i][j]

    # 2
    for i in range(1, x+d2+1):
        for j in range(n, y, -1):
            if visited[i][j] == 5:
                break
            else:
                people[2] += graph[i][j]

    # 3
    for i in range(x+d1, n+1):
        for j in range(1, y-d1+d2):
            if visited[i][j] == 5:
                break
            else:
                people[3] += graph[i][j]
    # 4
    for i in range(x+d2+1, n+1):
        for j in range(n, y-d1+d2-1, -1):
            if visited[i][j] == 5:
                break
            else:
                people[4] += graph[i][j]

    people[5] = total - sum(people)
    ans = min(ans, max(people)-min(people[1:6]))


n = int(input())
graph = [[0 for _ in range(n+1)]]
total = 0

for i in range(n):
    data = [0] + list(map(int, input().split()))
    total += sum(data)
    graph.append(data)

ans = int(1e9)

for x in range(1, n+1):
    for y in range(1, n+1):
        for d1 in range(1, n+1):
            for d2 in range(1, n+1):
                if x+d1+d2 > n:
                    continue
                if y-d1 < 1:
                    continue
                if y+d2 > n:
                    continue
                solve(x, y, d1, d2)

print(ans)