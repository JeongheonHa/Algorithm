arr = input()

sum_val = 0
q = []
for n in arr:
    if n.isalpha():
        q.append(n)
    else:
        sum_val += int(n)

q.sort()

if sum_val != 0:
    q.append(str(sum_val))
print("".join(q))