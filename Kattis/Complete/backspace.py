# Backspace

line = input()
out = []

for c in line:
    if c == "<":
        out.pop()
    else:
        out.append(c)

print(''.join(out))
