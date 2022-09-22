n = int(input())

for _ in range(n):
    r, s = input().split()
    
    for alpha in s:
        print(alpha*int(r), end = "")
    print()