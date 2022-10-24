n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
num = []
for i in range(n):
    num.append(min(arr[i]))
print(max(num))