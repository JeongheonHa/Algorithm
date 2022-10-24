# n: 배열의 크기, m: 더한 횟수, k: 중복 횟수

n, m, k = map(int, input().split())
arr = sorted(list(map(int, input().split())), reverse = True)

first = arr[0]
second = arr[1]
# 최대 값의 최대 횟수
cnt = int(m/(k+1))*k + m%(k+1)

ans = cnt*first + (m-cnt)*second

print(ans)
    
    
    
    
