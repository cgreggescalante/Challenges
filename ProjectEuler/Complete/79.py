attempts = open('Resources/Keylog79.txt', 'r').readlines()

for i in range(len(attempts)):
    attempts[i] = attempts[i][:-1]

print(attempts)

chars = {}
# number : [appearances]
for a in attempts:
    for i in range(3):
        if not a[i] in chars:
            chars[a[i]] = [i]
        else:
            chars[a[i]].append(i)

averages = {}
for key, value in chars.items():
    print(key, value)
    total = 0
    for i in value:
        total += i
    averages[key] = total / len(value)

for key, value in averages.items():
    print(key, value)