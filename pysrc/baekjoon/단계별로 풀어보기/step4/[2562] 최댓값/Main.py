import sys


input = [int(sys.stdin.readline()) for i in range(9)]

max = max(input)

if max in input:
    print(max)
    print(input.index(max)+1)
    
