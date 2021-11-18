total = 0

for i in range(2, 11):
    print(i**i)
    total += (i ** i)
    if len(str(total)) > 20:
        total = int(str(total)[-20:])
print(total)