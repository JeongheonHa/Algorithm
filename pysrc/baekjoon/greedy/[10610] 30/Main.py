n = input()
n = sorted(n, reverse=True)
sum_val = 0

if '0' not in n:
    print(-1)
else:
    for i in n:
        sum_val += int(i)
    if sum_val % 3 != 0:
        print(-1)
    else:
        print(''.join(n))