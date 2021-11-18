temp = 0
one = 0
two = 1
total = 0

while two <= 4000000:
    temp = two
    two += one
    one = temp
    if two % 2 == 0:
        total += two

print(total)
