import sys
input = sys.stdin.readline

n = int(input())
h = []
for _ in range(n):
    h.append(int(input()))
    

def histogram(left, right):
    if left == right:
        return h[left]
    mid = (left+right)//2
    
    ret = max(histogram(left, mid), histogram(mid+1, right))
    lo = mid
    hi = mid+1
    height = min(h[lo], h[hi])  # 가운데 나눠진 바로 앞뒤의 높이 측정
    ret = max(ret, 2*height)
    
    while left < lo or hi < right:
        if hi < right and (lo == left or h[lo-1] < h[hi+1]):
            hi += 1
            height = min(height, h[hi])
        else:
            lo -= 1
            height = min(height, h[lo])
        
        ret = max(ret, height*(hi - lo + 1))
    
    return ret

ans = histogram(0, len(h)-1)
print(ans)