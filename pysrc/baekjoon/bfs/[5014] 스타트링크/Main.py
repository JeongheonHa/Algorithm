import sys
from collections import deque
input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())

building = [0]*(f+1)
ds = [u, -d]

def bfs(s):
    q = deque([s])
    building[s] = 1
    while q:
        s = q.popleft()
        if s == g:
            return building[s] - 1
        for i in range(2):
            ns = s + ds[i]
            if 0 < ns <= f and not building[ns]:
                building[ns] = building[s] + 1
                q.append(ns)
    return "use the stairs"

print(bfs(s))
        
        