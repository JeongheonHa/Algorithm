# 멀티 탭에 해당 제품에 이미 꽂혀있는 경우 pass
# 멀티 탭에 해당 제품이 꽂혀있지 않은 경우 하나를 뽑고 해당 제품을 꽂는다.
# 뽑는 기준 (1) : 멀티 탭에 꽂혀있는 제품 중에서 다시 나오지 않는 제품을 뽑는다.
# 뽑는 기준 (2) : 멀티 탭에 꽂혀있는 제품 중에서 다음 순서에서 가장 마지막에 등장할 제품을 뽑는다.

import sys


n, k = map(int, sys.stdin.readline().rstrip().split())
items = list(map(int, sys.stdin.readline().rstrip().split()))

tab = []
cnt = 0
for i, item in enumerate(items):
    if item in tab:
        continue
    
    if len(tab) < n:
        tab.append(item)
        continue
    
    plug_out = maxIdx = 0
    
    for tab_item in tab:
        if tab_item in items[i:]:
            idx = items[i:].index(tab_item)
            if idx > maxIdx:
                maxIdx = idx
                plug_out = tab_item
        else:
            plug_out = tab_item
            break
    cnt += 1
    tab.remove(plug_out)
    tab.append(item)

print(cnt)

