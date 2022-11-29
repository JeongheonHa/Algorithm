import sys
input = sys.stdin.readline

n, c = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

start = 1 # 가능한 최소 거리
end = arr[-1] - arr[0]  # 가능한 최대 거리
ans = 0

while start <= end:
    mid = (start+end)//2    # 가장 인접한 두 공유기 사이의 거리
    val = arr[0]
    cnt = 1
    
    for i in range(1, n):   # 앞에서 부터 설치
        if arr[i] >= val + mid:
            val = arr[i]
            cnt += 1
    
    if cnt >= c:    # c개 이상의 공유기를 설치할 수 있는 경우, 거리 증가
        start = mid + 1
        ans = mid
    else:           # c개 이상의 공유기를 설치할 수 없는 경우, 거리 감소
        end = mid - 1

print(ans)