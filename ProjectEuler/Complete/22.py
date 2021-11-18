with open('../Resources/Names22.txt', 'r') as file:
    names = [a.strip("\"").lower() for a in file.read().split(',')]

names.sort()
total = 0

for i in range(len(names)):
    score = 0
    for c in names[i]:
        score += ord(c) - 96
    total += score * (i + 1)

print(total)
