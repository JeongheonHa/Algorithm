n = int(input())

input = list(map(int, input().split()))

print(" ".join([str(min(input)), str(max(input))]))