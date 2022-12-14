n, m = map(int, input().split())

arr = list(map(int, input().split()))

s, e, sumVal, result = 0, 0, 0, 0

while True:
    if sumVal >= m:
        sumVal -= arr[s]
        s += 1
    elif e == n: break
    else: 
        sumVal += arr[e]
        e += 1
    if sumVal == m: result += 1

print(result)