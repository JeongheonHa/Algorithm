import sys

n = int(sys.stdin.readline().rstrip())
num = n
count = 0

while 1:
    a = num // 10 # n 왼쪽
    b = num % 10 # n 오른쪽
    c = a + b # 왼쪽 + 오른쪽
    num = (b * 10) + (c % 10)
    count += 1
    
    if n == num:
        print(count)
        break