input = int(input())

index, max, gap = 0, 0, 0

while input > max:
    index += 1
    max = int((index**2+index)/2)
    gap = max - input
    
if index % 2 == 0:
    print(f"{index-gap}/{1+gap}")
else:
    print(f"{1+gap}/{index-gap}")