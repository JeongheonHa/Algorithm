n, k = map(int, input().split())
coins = sorted([int(input()) for _ in range(n)], reverse = True)
remainder = k
cnt = 0
for coin in coins:
    if remainder >= coin:
        cnt += remainder//coin
        remainder %= coin
        
print(cnt)