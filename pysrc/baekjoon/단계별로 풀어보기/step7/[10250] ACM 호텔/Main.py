n = int(input())

for _ in range(n):
    H, W, N = map(int, input().split())

    x, y = divmod(N,H)
    room = x+1
    floor = y
    if not y:
        room = x
        floor = H
    print(f"{floor*100+room}")