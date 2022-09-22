input = list(input())

alpha = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
change_index = {}

for i, a in enumerate(alpha):
    change_index[a] = -1

for n in input:
    if n in change_index:
        change_index[n] = input.index(n)

print(" ".join(map(str, change_index.values())))


# 다른 사람 코드
word = input()
alpha = list(range(97,123))

for i in alpha:
    print(word.find(chr(i)), end = " ")