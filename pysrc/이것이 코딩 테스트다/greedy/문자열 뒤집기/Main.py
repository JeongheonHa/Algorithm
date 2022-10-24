# 문자열의 연속된 0과 1을 cnt
# 다음 원소가 다른 숫자가 나올 때 cnt+1
# 더 적은 숫자를 출력

s = input()
if s[0] == '0':
    zero_cnt = 1
    one_cnt = 0
else:
    zero_cnt = 0
    one_cnt = 1
    
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '0':
            zero_cnt += 1
        else:
            one_cnt += 1
ans = min(zero_cnt, one_cnt)
print(ans)