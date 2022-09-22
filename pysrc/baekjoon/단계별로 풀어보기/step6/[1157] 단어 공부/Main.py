from collections import Counter

input = input().upper()

count = Counter(input)
common = count.most_common()

if len(input) > 1 and common[0][1] == common[1][1]:
    print("?")
else:
    print(common[0][0])