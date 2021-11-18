# Roman Numerals


rules = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
}


def numeral(n):
    s = ""

    for k, v in rules.items():
        while n >= k:
            s = s + v
            n -= k

    while n > 0:
        s = s + "I"
        n -= 1

    return s


def value(s):
    n = 0

    for k, v in rules.items():
        while s.startswith(v):
            n += k
            s = s.replace(v, '', 1)

    n += len(s)

    return n


with open("C:\\Users\\Conor\\PycharmProjects\\EulerStuff\\Resources\\romanNumerals89.txt", 'r') as file:
    numerals = [a.strip() for a in file.readlines()]


total = 0

for n in numerals:
    val = value(n)
    actual = numeral(val)
    print(n, val)
    total += len(n) - len(actual)

print(total)
