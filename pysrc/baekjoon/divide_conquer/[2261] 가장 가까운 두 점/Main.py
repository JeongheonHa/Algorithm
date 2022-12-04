# closest pair of points 문제이다.
# 2점 : O(1), 3점 : O(3), 4점의 최소 거리를 구할 때는 좀 더 복잡하기 떄문에 3점이 나올 때까지 분할한다.
# left에서의 closest pair를 구하는 총 시간복잡도는 T(n/2)
# right에서의 closest pair를 구하는 총 시간복잡도는 T(n/2)
# strip을 찾을 때 O(n)
# strip을 y로 정렬하는데 O(nlogn)
# strip에서 closest pair를 구할 때 O(n) <- 핵심(최적화)
# 따라서 T(n) = 2*T(n/2) + O(nlogn) + 2*O(n) = O(n(logn)^2)
# 병합정렬 아이디어를 이용하여 정렬을 O(n)에 하여 O(nlogn)에 할 수 있다.
# 스위핑 기법을 사용하여서 O(nlogn)을 얻을 수 있다.


import sys
input = sys.stdin.readline

def getDist(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def bruteForce(left, right):
    minDist = float('Inf')
    
    for i in range(left, right+1):
        for j in range(i+1, right+1):
            if getDist(points[i], points[j]) < minDist:
                minDist = getDist(points[i], points[j])
    return minDist

def closestUtil(left, right):

    if right - left <= 2:
        return bruteForce(left, right)
    
    mid = (left + right)//2
    minDist = min(closestUtil(left, mid), closestUtil(mid+1, right))
    
    strip = []
    for i in range(left, right+1):
        if (points[mid][0] - points[i][0])**2 < minDist:
            strip.append(points[i])
            
    strip.sort(key=lambda x: x[1])
    
    size = len(strip)
    for i in range(size-1):
        for j in range(i+1, size):
            if (strip[j][1] - strip[i][1])**2 < minDist:
                minDist = min(minDist, getDist(strip[i], strip[j]))
            else:
                break

    return minDist

n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
    
points.sort()

ans = closestUtil(0, n-1)
print(ans)
