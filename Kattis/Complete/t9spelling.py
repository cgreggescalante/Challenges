# T9 Spelling

n = int(input())

for i in range(n):
    message = input()
    output = f"Case #{i + 1}: "
    for c in message:
        o = ""
        if c == " ":
            o = "0"
        else:
            a = ord(c) - 97
            if a < 15:
                digit = a // 3 + 2
                times = a % 3 + 1
            elif a < 19:
                digit = 7
                times = a - 14
            elif a < 22:
                digit = 8
                times = a - 18
            else:
                digit = 9
                times = a - 21
            o = str(digit) * times
        if output.endswith(o[0]):
            output += " "
        output += o
    print(output)
