M, N = [int(input()) for _ in range(2)]

prime = []
for num in range(M, N+1):
    if num > 1:
        for i in range(2, num+1):
            if num % i == 0 and num != i:
                break
            if num == i:
                prime.append(num)
if prime == []:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))
