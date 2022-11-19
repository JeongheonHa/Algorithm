# np-hard 중 하나인 냅색 문제이다.
# 배낭에 담을 수 있는 무게의 최댓값이 정해져있고 일정 가치와 무게가 있는 짐들을 배낭에 넣을 때 가치의 합이 최대가 되도록 짐을 고르는 방법을 찾는 문제이다.
# 매 문제에서 제한 무게에따라 해당 물건을 넣을지 말지를 결정하면되기 때문에 총 O(NK)의 시간 복잡도를 갖는다.


n, k = map(int, input().split())

items = [(0,0)]
for _ in range(1, n+1):
    w, v = map(int, input().split())
    items.append((w, v))
    
knapsack = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(k+1):
        weight = items[i][0]
        value = items[i][1]
        if j < weight:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(value + knapsack[i-1][j-weight], knapsack[i-1][j])

print(knapsack[n][k])