from itertools import permutations

# 1. 111 ~ 999 까지의 모든 경우의 수를 미리 구한다.
# 2. num의 각각의 자릿수를 각각의 모든 경우의 수와 s, b 비교
# 3. s, b가 일치하면 남기고 일치하지 않으면 제거한다.
# 4. 제거하는 과정에서 idx가 하나씩 밀리기 때문에 idx를 한칸 전으로 위치시킨다.

n = int(input())
perNum = list(permutations(range(1, 10), 3))

for _ in range(n):
    num, strike, ball = map(int, input().split())
    num = list(str(num))
    cnt = 0
    
    for i in range(len(perNum)):
        s, b = 0, 0
        i -= cnt
        for j in range(3):
            num[j] = int(num[j])
            if num[j] in perNum[i]:
                if j == perNum[i].index(num[j]):
                    s += 1
                else:
                    b += 1
                    
        if strike != s or ball != b:
            perNum.remove(perNum[i])
            cnt += 1

print(len(perNum))