from Utilities.FermatPrimalityTest import is_prime

prev = 1
primes = 0
count = 1
layer = 0

while True:
    layer += 1
    for _ in range(4):
        prev += layer * 2
        if is_prime(prev):
            primes += 1
    if primes / ((layer + 1) * 4) < .1:
        print(layer * 2 + 1)
        break
