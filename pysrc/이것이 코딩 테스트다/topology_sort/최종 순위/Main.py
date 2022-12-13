from collections import deque


for _ in range(int(input())):
    n = int(input())
    graph = [[False]*(n+1) for i in range(n+1)]
    indegree = [0]*(n+1)
    data = list(map(int, input().split()))
    
    for i in range(n-1):
        for j in range(i+1, n):
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1
            
    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1
    
    result = []
    q = deque()
    
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    
    certain = True  # 위상 정렬 결과가 오직 하나인지 여부
    cycle = False   # 사이클 존재 여부
    
    for _ in range(n):
        if len(q) == 0:     # 큐가 비었다면 사이클 발생했다는 의미
            cycle = True
            break
        if len(q) >= 2:     # 큐의 원소가 2개 이상이면 가능한 정렬 결과가 여러개
            certain = False
            break
        
        here = q.popleft()
        result.append(here)
        for there in range(1, n+1):
            if graph[here][there]:
                indegree[there] -= 1
                if indegree[there] == 0:
                    q.append(there)
                    
    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for i in result:
            print(i, end = ' ')
        print()