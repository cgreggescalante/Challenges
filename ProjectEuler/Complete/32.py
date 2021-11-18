# Pandigital Products
from Utilities.LexicographicPermutations import iterate_digit_array


def num_from_array(arr):
    arr = [str(i) for i in arr]
    return int(''.join(arr))


identity = [1, 2, 3, 4, 5, 6, 7, 8, 9]
initial_state = [1, 2, 3, 4, 5, 6, 7, 8, 9]

products = []
iters = 0

while True:
    print(iters)
    iters += 1

    for i in range(1, len(identity) - 1):
        for j in range(i+1, len(identity)):
            a = num_from_array(identity[:i])
            b = num_from_array(identity[i:j])
            c = num_from_array(identity[j:])
            if a * b == c:
                if c not in products:
                    products.append(c)
                    print(c)
    identity = iterate_digit_array(identity)
    if identity == initial_state or iters == 362880:
        print(sum(products))
        break
