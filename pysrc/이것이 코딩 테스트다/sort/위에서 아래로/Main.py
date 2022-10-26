n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
    
arr.sort(reverse = True)

for num in arr:
    print(num, end = " ")