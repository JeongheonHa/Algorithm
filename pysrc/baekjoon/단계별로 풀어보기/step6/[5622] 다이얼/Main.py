alpha = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

num = list(input())
time = 0

for i in num:
    for j in alpha:
        if i in j:
            time += alpha.index(j) + 3
print(time)