i = 0
while True: 
    l, p, v = map(int, input().split())
    
    if l == 0 and p == 0 and v == 0:
        break
    i += 1
    days = (v//p)*l
    if v%p <= l:
        days += v%p
    else:
        days += l
    print(f"Case {i}: {days}")

