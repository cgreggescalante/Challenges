# Digit sum numbers

def is_digit_sum(n):
    arr = list(map(int, str(n)))

    return max(arr) == sum(arr) - max(arr)


target = 7
total = 0

for n in range(10 ** target):
    if is_digit_sum(n):
        total += n

print(total)
