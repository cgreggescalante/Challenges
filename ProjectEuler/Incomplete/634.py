# Numbers of the form a^2 x b^3

target = 9 * (10 ** 18)

a = (x*x for x in range(2, int((target / 8) ** .5) + 1))
b = (x*x*x for x in range(2, int((target / 4) ** (1/3)) + 1))

print(a)
print(b)

count = 0
for i in a:
    print(i)
    for j in b:
        if i * j < target:
            count += 1
        else:
            break

print(count)
