count = 0


def iterate(num):
    num = str(num)
    new = 0
    for i in num:
        new += int(i) ** 2
    return new

for i in range(10000000):
    if i % 100000 == 0:
        print(i)
        print(count)
    num = i
    while True:
        if num == 89:
            count += 1
            break
        if num == 1 or num == 0:
            break
        num = iterate(num)

print(count)
