import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

visited = [0]*100001

dn = [-1, 1, 2]

def bfs(n, k):
    q = deque([n])
    visited[n] = 1
    while q:
        n = q.popleft()
        if n == k:
            return visited[n] - 1
        for i in range(3):
            if i == 2:
                nn = n * dn[i]
            else:
                nn = n + dn[i]
            if 0 <= nn <= 100000 and not visited[nn]:
                visited[nn] = visited[n] + 1
                q.append(nn)
    return -1
print(bfs(n, k))