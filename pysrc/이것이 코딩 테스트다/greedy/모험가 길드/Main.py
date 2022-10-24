# 오름차순 정렬
# 그룹의 수가 최대가 되려면 같은 숫자끼리 그룹을 맺는다.
# 나머지는 마을에 남겨둔다. 어차피 그룹으로 못만든다.

n = int(input())
arr = sorted(list(map(int, input().split())))
group = 0
cnt = 0
for data in arr:
    cnt += 1
    if cnt == data:
        group += 1
        cnt = 0
print(group)