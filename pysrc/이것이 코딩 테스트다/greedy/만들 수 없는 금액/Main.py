# 동전을 오름차순 정렬
# 1부터 시작해서 동전의 합으로 해당 값을 만들 수 있는지 확인
# 만들 수 없는 경우가 나오면 해당 값이 최소값이 된다.
# 동전의 다음 값이 해당 값보다 크다면 해당 값은 만들 수 없다.
# 반대로 동전을 순서대로 더한 값과 작거나 같은 값들은 모두 동전의 조합으로 만들 수 있다.

n = int(input())
coins = sorted(list(map(int, input().split())))

ans = 1
for num in coins:
    if ans < num:
        break
    ans += num
print(ans)