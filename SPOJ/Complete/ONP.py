# Transform the Expression

t = int(input())


def parse(s):
    if len(s) == 1:
        return s
    if len(s) == 3:
        return s[0] + s[2] + s[1]

    s = s[1:-1]

    layer = 0
    i = 0
    while True:
        if s[i] == "(":
            layer += 1
        elif s[i] == ")":
            layer -= 1
        elif s[i] in "+-*/^" and not layer:
            a = s[:i]
            o = s[i]
            b = s[i+1:]
            return parse(a) + parse(b) + o
        i += 1


for _ in range(t):
    expression = input()
    print(parse(expression))
