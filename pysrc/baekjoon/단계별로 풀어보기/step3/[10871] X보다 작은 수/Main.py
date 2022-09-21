n, x = map(int, input().split())
A = list(map(int, input().split()))
result = []
for a in A:
    if a < x:
        result.append(str(a))
print(" ".join(result))