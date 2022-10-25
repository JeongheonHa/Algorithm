# 입력 받은 칸에서 나이트가 이동할 수 있는 모든 경우의 수를 구한다.

pos = input()
col = int(pos[1])
row = ord(pos[0]) - ord('a') + 1
cnt = 0

steps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

for step in steps:
    new_row = row + step[0]
    new_col = col + step[1]

    if new_row > 0 and new_row <= 8 and new_col > 0 and new_col <=8:
        cnt += 1
    
print(cnt)