# 특정 조건에서 계단을 오르면서 얻을 수 있는 최대 가치의 합을 구하는 문제이다.
# 타일링 문제와 유사한 문제리고 생각했다.
# 뒤에서부터 가능한 경우의 수를 cnt한 후 점화식을 작성하는 방식을 떠올렸다.
# 주의해야할 점은 i위치에 오르는 경우 중 i-3의 최대합을 구한 값이지만 i-1은 새로운 값이기 때문에 arr[i-1]을 더해 주어야한다.
# 시간 복잡도 : O(n)


import sys
input = sys.stdin.readline

n = int(input())

arr = [0]*301
d = [0]*301

for i in range(n):    # 계단의 갯수는 300이하의 자연수이므로 n은 1, 2도 가능하기 때문에 초기조건때문에 indexerror가 발생할 수 있다.
    arr[i] = int(input())

d[0] = arr[0]
d[1] = max(arr[0] + arr[1], arr[1])
d[2] = max(arr[0] + arr[2], arr[1] + arr[2])

for i in range(3, n):
    d[i] = arr[i] + max(d[i-3] + arr[i-1], d[i-2])

print(d[n-1])