# Akcija

N = int(input())

books = sorted([int(input()) for _ in range(N)])[::-1]
cost = 0
i = 0

while i < N - 2:
    cost += books[i]
    cost += books[i+1]
    i += 3

cost += sum(books[i:])

print(cost)
