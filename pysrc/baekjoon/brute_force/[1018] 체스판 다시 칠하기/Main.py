# 1. 끝에서 7칸이 남을 때 까지 x, y 포인터 이동
# 2. 포인터마다 행열로 8칸안에 교체해야하는 칸의 개수 count
# 3. 왼쪽 위가 white일 때와 black일 때 구분해서 count 개수들을 저장
# 4. 마지막 포인터까지 모두 순회한 후 그 중에서 최소 count를 출력

n, m = map(int, input().split())
chess = [input().strip() for _ in range(n)]

cnt = []

for a in range(n-7):
    for b in range(m-7):
        w_cnt, b_cnt = 0, 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j)%2 == 0:
                    if chess[i][j] != 'W':
                        w_cnt += 1
                    if chess[i][j] != 'B':
                        b_cnt += 1
                else:   
                    if chess[i][j] != 'B':
                        w_cnt += 1
                    if chess[i][j] != 'W':
                        b_cnt += 1
        cnt.append(min(w_cnt, b_cnt))

print(min(cnt))
