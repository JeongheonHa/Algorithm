n = int(input())
arr = [list(input()) for _ in range(n)]
maxLen = 0

# 같은 종류의 사탕의 최대 길이 찾기
def search(arr):
    maxLen = 1

    for i in range(n):
        cnt = 1
        # 첫 번째 행의 모든 열의 사탕 탐색
        for j in range(1, n):
            if arr[i][j] == arr[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            if cnt > maxLen:
                maxLen = cnt
        cnt = 1
        # 첫 번째 열의 모든 행의 사탕 탐색
        for j in range(1, n):
            if arr[j][i] == arr[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            if cnt > maxLen:
                maxLen = cnt
    return maxLen

     

# 하나씩 교환해보며 최대 길이를 찾기
for i in range(n):
    for j in range(n):
        # 행의 모든 열의 사탕을 하나씩 교환하며 최대길이 갱신
        if j+1 < n:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            
            newMaxLen = search(arr)
            
            if newMaxLen > maxLen:
                maxLen = newMaxLen
                
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
        # 열의 모든 행의 사탕을 하나씩 교환하며 최대길이 갱신
        if i+1 < n:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            
            newMaxLen = search(arr)
            
            if newMaxLen > maxLen:
                maxLen = newMaxLen
            
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]

print(maxLen)