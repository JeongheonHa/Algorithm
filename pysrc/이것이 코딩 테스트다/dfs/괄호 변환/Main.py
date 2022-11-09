# 괄호의 쌍이 맞는지 확인하고 싶을 때는 스택을 사용하도록 하자.


def is_proper(str):
    left = 0
    right = 0
    stack = []
    correct = True
    for i in range(len(str)):
        if str[i] == '(':
            left += 1
            stack.append('(')
        else:
            right += 1
            if len(stack) == 0:
                correct = False
            else:
                stack.pop()
                
        if left == right:
            return i+1, correct


def solution(p):
    if len(p) == 0:
        return p
    
    pos, correct = is_proper(p)
    u = p[:pos]
    v = p[pos:]
    
    if correct:
        return u + solution(v)
    
    ans = '(' + solution(v) + ')'
    for i in range(1, len(u)-1):
        if u[i] == '(':
            ans += ')'
        else:
            ans += '('
        
    return ans
        
        