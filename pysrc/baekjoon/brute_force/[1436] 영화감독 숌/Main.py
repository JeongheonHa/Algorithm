# n이 10000이고 제한 시간이 2초이므로 대략 4천만번의 연산이 가능하다고 하자.
# 6669999까지의 n을 생각해보면 10000이상의 카운트 할 수 있다.
# 따라서 이 문제는 n이 10000이 될 때까지 완전 탐색을 돌리면 된다.

n = int(input())
ans = 666

for i in range(666, 6669999):
    if '666' in str(i):
        n -= 1
        if n == 0:
            break
    i += 1

print(i)
    