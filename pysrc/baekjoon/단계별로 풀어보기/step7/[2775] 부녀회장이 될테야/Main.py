t = int(input())

for _ in range(t):
    floor = int(input())
    room = int(input())
    base = [x for x in range(1, room+1)]
    for h in range(floor):
        for i in range(1, room):
            base[i] += base[i-1]
    print(base[-1])