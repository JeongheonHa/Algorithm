import sys

n = sys.stdin.readline().rstrip()

for i in range(int(n)):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a + b)