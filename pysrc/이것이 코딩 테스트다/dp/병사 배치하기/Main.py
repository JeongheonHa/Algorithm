import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
d = [1]*n

for i in range(1, n):
    for j in range(i):
        if arr[i] < arr[j]:
            d[i] = max(d[i], d[j] + 1)

print(n - max(d))

ans = []
x = max(d)
for i in range(n-1, -1, -1):
    if d[i] == x:
       ans.append(arr[i])
       x -= 1

ans.reverse()
print(*ans)