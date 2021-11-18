# Reversed Binary Numbers

N = int(input())

print(int(bin(N)[2:][::-1], 2))
