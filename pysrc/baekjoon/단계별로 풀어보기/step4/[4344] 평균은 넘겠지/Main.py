n = int(input())

for _ in range(n):
    total = []
    count = 0
    people, *total = map(int, input().split())
    
    avg = sum(total) / people
    
    for score in total:
        if score > avg:
            count += 1
    print(f"{(count/people) * 100:0.3f}%")