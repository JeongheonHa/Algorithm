input = list(map(int, input().split()))
ch = [1, 1, 2, 2, 2, 8]

str = " ".join([str(b - a) for a, b in zip(input, ch)])
print(str)