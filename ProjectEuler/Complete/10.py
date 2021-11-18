from Utilities.PrimeTesting import is_prime

total = 5

for i in range(3, 2000001, 2):
    if is_prime(i):
        total += i

print(total)
