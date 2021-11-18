def val(num):
    total = 0
    for i in str(num):
        total += int(i)
    return total


biggest = 0

for a in range(100):
    for b in range(100):
        num = a ** b
        score = val(num)

        if score > biggest:
            biggest = score
            print(biggest)

print(biggest)
