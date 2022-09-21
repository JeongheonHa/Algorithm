total = int(input())

if total == sum([num[0] * num[1] for num in [list(map(int, input().split())) for i in range(int(input()))]]):
    print("Yes")
else:
    print("No")