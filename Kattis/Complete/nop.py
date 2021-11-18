# NOP

s = input()
c = 0
i = 0
while i < len(s):
    if s[i] in "QWERTYUIOPASDFGHJKLZXCVBNM":
        if i % 4:
            s = s[:i] + "-" + s[i:]
            c += 1
        else:
            i += 1
    else:
        i += 1

print(c)
