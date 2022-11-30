import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def pow(a, b, c):
    if b == 1:
        return a
    
    if b % 2 != 0:
        return pow(a, b-1, c)*a
    
    half = pow(a, b//2, c)
    return (half * half)%c

ans = pow(a, b, c)
print(ans%c)