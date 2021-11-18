# Homework

l = input().split(";")

n = 0

for i in l:
    if "-" in i:
        i = i.split("-")
        n += int(i[1]) - int(i[0]) + 1
    else:
        n += 1

print(n)
