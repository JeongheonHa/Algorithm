import sys
input = sys.stdin.readline

def matrix_mul(matrix1, matrix2):
    n = len(matrix1)
    result = [[0]*n for _ in range(n)]
    
    for p in range(n):
        for r in range(n):
            for q in range(n):
                result[p][r] += matrix1[p][q] * matrix2[q][r]
                result[p][r] %= 1000
    return result

def pow(A, b):
    if b == 1:
        return A
    
    if b % 2 != 0:
        return matrix_mul(pow(A, b-1), A)
    
    half = pow(A, b//2)
    
    return matrix_mul(half, half)

n, b = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

ans = pow(A, b)

for i in range(n):
    for j in range(n):
        ans[i][j] %= 1000

for i in range(n):
    print(*ans[i])