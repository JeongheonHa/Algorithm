# 뚫린 위치를 인덱스라고 생각한다.
# 뚫린 위치 관점에서 테이프의 길이 범위안에 있으면 기존의 테이프를 쓰는 것과 같다.
# 뚫린 위치가 테이프의 길이 범위안에 없으면 새로운 테이프를 사용한다.
# 테이프의 길이는 뚫린 위치를 기준으로 l만큼이다.

n, l = map(int, input().split())
arr = sorted(list(map(int, input().split())))

cnt = 1
start = arr[0]
for pos in arr:
    if pos not in range(start, start+l):
        cnt += 1
        start = pos

print(cnt)