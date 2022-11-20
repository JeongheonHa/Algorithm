import sys
input = sys.stdin.readline

x = input().rstrip()
y = input().rstrip()
n = len(x)
m = len(y)

d = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if x[i-1] == y[j-1]:
            d[i][j] = d[i-1][j-1] + 1
        else:
            d[i][j] = max(d[i][j-1], d[i-1][j])
            
print(d[n][m])

ans = []
i = len(x)
j = len(y)
while i >= 1 and j >= 1:
    if d[i][j] == d[i-1][j]: 
        i -= 1
    elif d[i][j] == d[i][j-1]: 
        j -= 1
    else:
        ans.append(x[i-1])
        i -= 1
        j -= 1

ans.reverse()

print("".join(ans))