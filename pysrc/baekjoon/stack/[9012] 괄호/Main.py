import sys
input = sys.stdin.readline

def isValid(s):
    openParens = {'(' : ')'}
    closeParens = {}
    for i, v in openParens.items():
        closeParens[v] = i
        
    stack = []
    for char in s:
        if char in openParens:
            stack.append(char)
            
        elif char in closeParens:
            if len(stack) == 0 or stack[-1] != closeParens[char]:
                return False
            else:
                stack.pop()
                
    return len(stack) == 0

n = int(input())
    
for _ in range(n):

    s = list(input())
    if isValid(s):
        print("YES")
    else:
        print("NO")