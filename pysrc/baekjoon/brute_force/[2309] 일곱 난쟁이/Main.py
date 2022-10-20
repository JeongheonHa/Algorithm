from itertools import combinations

dwarf = [int(input()) for _ in range(9)]
case = list(combinations(dwarf, 7))
for i in case:
    if sum(i) == 100:
        result = list(i)
        break

result.sort()
for i in result:
    print(i)
