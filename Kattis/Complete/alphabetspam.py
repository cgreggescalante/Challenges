# Alphabet Spam

ws = 0
lc = 0
uc = 0
s = 0

l = input()

for c in l:
    c = ord(c)
    if c == 95:
        ws += 1
    elif 96 < c < 123:
        lc += 1
    elif 64 < c < 91:
        uc += 1
    else:
        s += 1

l = len(l)

print(ws / l)
print(lc / l)
print(uc / l)
print(s / l)
