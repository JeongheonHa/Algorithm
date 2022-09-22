input = [int(input()) for i in range(10)]

set = {num % 42 for num in input}

print(len(set))