total = 1

for i in range(61175):
    total *= 340282366920938463463374607431768211456
    total = int(str(total)[-10:])

for i in range(57):
    total *= 2
    total = int(str(total)[-10:])

print('Last 10 :', str(total*28433 + 1)[-10:])