n = int(input())

for _ in range(n):
    ox = input()
    count = 0
    score = 0
    
    for i in range(len(ox)):
        if ox[i] == "O":
            count += 1
            score += count
        else:
            count = 0
    print(score)