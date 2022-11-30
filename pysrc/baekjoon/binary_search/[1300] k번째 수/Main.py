# 2차원 배열을 1차원 배열로 오름차순 정렬시켰을 때 인덱스 k번째의 값을 구하는 문제 (단 모든 원소는 i*j이다)
# 아이디어 : k번째 값 앞에 k-1개 만큼 있다면 해당 위치의 값이 k번째의 값이 된다.
# 따라서 k번째 값이 몇 개 있는지 cnt


import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

ans = 0
def binarySearch(start, end):
    global ans
    while start <= end:
        mid = (start+end)//2
    
        cnt = 0
        for i in range(1, n+1):
            cnt += min(mid//i, n)
        
        if cnt >= k:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1

binarySearch(1, k)
print(ans)