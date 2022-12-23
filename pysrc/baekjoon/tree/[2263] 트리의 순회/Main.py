import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


def getPreorder(inS, inE, postS, postE):
    if inS > inE or postS > postE:
        return
    
    root = postorder[postE]
    
    left = pos[root] - inS

    print(root, end = " ")
    getPreorder(inS, pos[root]-1, postS, postS+left-1)
    getPreorder(pos[root]+1, inE, postS+left, postE-1)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

pos = [0]*(n+1)
for i in range(n):
    pos[inorder[i]] = i
    
getPreorder(0, n-1, 0, n-1)