# FizzBuzz

X, Y, N = map(int, input().split())

for i in range(1, N + 1):
    if i % X == 0:
        print("Fizz", end="")
    if i % Y == 0:
        print("Buzz", end="")
    if i % X and i % Y:
        print(i, end="")
    print()
