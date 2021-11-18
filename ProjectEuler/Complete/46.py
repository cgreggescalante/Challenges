from Utilities.FermatPrimalityTest import is_prime

twice_squares = []

for i in range(1000):
    twice_squares.append(2 * (i ** 2))

n = 1
while True:
    works = False
    for i in twice_squares:
        if n < i:
            break
        if is_prime(n-i):
            works = True
            break
    if not works:
        print(n)
        break
    n += 2
