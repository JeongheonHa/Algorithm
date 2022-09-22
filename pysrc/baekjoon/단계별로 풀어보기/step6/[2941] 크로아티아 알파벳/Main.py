cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = input()

for str in cro:
    word = word.replace(str, '*')
    
print(len(word))