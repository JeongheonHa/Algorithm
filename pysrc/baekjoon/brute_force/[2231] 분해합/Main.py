n = int(input())

result = 0

for i in range(1, n+1):
    tmp = i + sum(map(int, str(i)))

    if tmp == n:
        result = i
        break
    elif i == n:
        result = 0
        break

print(result)