from Utilities.PrimeTesting import is_prime

num = 600851475143

for i in range(2, num):
    if num % i == 0:
        if is_prime(i):
            print(i)
