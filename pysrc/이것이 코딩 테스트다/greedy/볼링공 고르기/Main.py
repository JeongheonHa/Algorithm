# 두 사람 중 누가 해당 순서의 볼링공을 가져가도 상관없으므로 조합
# 각각의 무게의 볼링공의 개수를 구한다.
# 서로 다른 무게의 볼링공을 뽑을 경우의 수를 구한다.

n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담는 리스트
arr = [0]*11

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    arr[x] += 1
    
ans = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m+1):
    n -= arr[i]         # 무게가 i인 볼링공의 개수 제외
    ans += arr[i]*n     # B가 선택하는 경우의 수 곱하기

print(ans)
