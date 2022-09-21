import sys

x, y = [int(sys.stdin.readline().rstrip()) for i in range(2)]

if x > 0 and y > 0:
    print(1)
elif x > 0 and y < 0:
    print(4)
elif x < 0 and y > 0:
    print(2)
else:
    print(3)