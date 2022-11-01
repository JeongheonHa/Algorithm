import sys
input = sys.stdin.readline

def check(s):
    for i in range(1, len(s)//2+1):
        if s[-i:] == s[-i*2:-i]:
            return False
    return True

def dfs(s):
    if len(s) == n:
        print(s)
        exit()
        
    for i in range(1, 4):
        if check(s+str(i)):
            dfs(s+str(i))
    return

if __name__ == "__main__":
    n = int(input())
    dfs('1')