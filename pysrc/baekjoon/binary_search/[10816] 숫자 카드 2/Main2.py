import sys
from collections import Counter


n = int(input())
card = list(map(int, input().split()))
m = int(input())
test = list(map(int, input().split()))

count = Counter(card)

for i in range(len(test)):
    if test[i] in count:
        print(count[test[i]], end=' ')
    else:
        print(0, end=' ')