# 첫번째는 1밖에 올 수 없으니 1개
# 두번째는 10 밖에 올 수 없으니 1개
# 세번째는 101, 100 2개
# 네번째는 1010, 1001, 1000 3개

# 다음과 같이 경우의 수의 개수는 피보나치 수열의 구조를 갖는다.

import sys
input = sys.stdin.readline

n = int(input())

d = [-1]*(91)
d[1] = 1
d[2] = 1    # n이 1부터 가능하기 때문에 2칸짜리 dp테이블을 만들 경우 indexerror 발생
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])
