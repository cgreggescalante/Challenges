# Fibonacci numbers

a, b = 0, 1

with open("../Resources/rosalind_fibo.txt", "r") as file:
    n = int(file.readline())

if n == 0:
    print(0)
    quit()

while n > 1:
    c = b
    b += a
    a = c
    n -= 1

print(b)
