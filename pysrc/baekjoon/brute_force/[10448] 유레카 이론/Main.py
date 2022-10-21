trangle = [n*(n+1)//2 for n in range(1, 46)]
arr = [0]*1001

# 1000까지의 모든 삼각수를 구한다.
for i in trangle:
    for j in trangle:
        for k in trangle:
            if i+j+k < 1001:
                arr[i+j+k] = 1
                
n = int(input())
for _ in range(n):
    num = int(input())
    print(arr[num])