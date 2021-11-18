# TODO: Evaluate replacing local implementation of divisors(n)
def divisors(n):
    if n % 2 == 0:
        n = n / 2
    divs = 1
    count = 0
    while n % 2 == 0:
        count += 1
        n = n / 2
    divs = divs * (count + 1)
    p = 3
    while n != 1:
        count = 0
        while n % p == 0:
            count += 1
            n = n / p
        divs = divs * (count + 1)
        p += 2
    return divs


def find_triangular_index():
    n = 1
    one, two = divisors(n), divisors(n + 1)
    while one * two < 500:
        n += 1
        one, two = two, divisors(n + 1)
    return n


index = find_triangular_index()
tri = (index * (index + 1)) // 2

print(tri)
