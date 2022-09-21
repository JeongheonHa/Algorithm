import sys


h, m = list(map(int, sys.stdin.readline().rstrip().split()))

total_m = h * 60 + m - 45

h, m = divmod(total_m, 60)

print(" ".join([str(h % 24) , str(m % 60)]))