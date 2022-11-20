# 주어진 동전의 조합으로 목표금액을 맞출 수 있는 경우의 수를 구하는 문제이다.
# d[i] : 목표금액을 만드는 경우의 수
# 이전 동전으로 만들 수 있는 목표금액의 경우의 수 + 현재 동전으로 만들 수 있는 경우의 수
# 현재 동전으로 만들 수 있는 경우의 수 = i-동전 만큼의 경우의 수
# i-동전의 경우의 수에서 해당 동전을 더하기만 하면 되기 때문에 경우의 수는 변화하지 않는다.

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))
    
d = [0]*(k+1)
d[0] = 1

for coin in coins:
    for i in range(coin, k+1):
        if i >= coin:
            d[i] += d[i-coin]
            
print(d[k])