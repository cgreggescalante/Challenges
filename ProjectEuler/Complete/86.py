# Cuboid Route

base = 2000
base2 = base*base
count = 0
a = 1

squares = [a*a for a in range(1, base * 3)]
square_check = {}
counter = 1
for square in squares:
    square_check[square] = counter
    counter += 1

while count < 1000000:
    a2 = a*a
    sums = []
    for s in squares:
        if s > a2:
            try:
                check = square_check[s - a2]
                end = check
                c = check // 2
                if check > a:
                    c -= (check - a - 1)
                if c > 0:
                    count += c
            except KeyError:
                pass
    a += 1

    # print()
    # for b in range(1, a+1):
    #     for c in range(1, b+1):
    #         try:
    #             b2 = (b+c)**2
    #             check = square_check[a2+b2]
    #             print("   ", a, b, c)
    #             count += 1
    #         except KeyError:
    #             pass

print(a - 1, count)
