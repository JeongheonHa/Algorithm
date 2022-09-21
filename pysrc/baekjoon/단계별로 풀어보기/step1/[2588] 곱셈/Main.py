import sys

a, b = [int(sys.stdin.readline().rstrip()) for i in range(2)]
b = str(b)
print(a * int(b[2]))
print(a * int(b[1]))
print(a * int(b[0]))
print(a * int(b))