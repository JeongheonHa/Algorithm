num = int(input())
count = 0

for i in range(1, num + 1):
    List = list(map(int, str(i)))
    if i < 100:
        count += 1
    elif List[0] - List[1] == List[1] - List[2]:
        count += 1

print(count)