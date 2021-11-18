# Cryptographer's Conundrum

target = "PER"

initial = input()
c = 0

for i in range(len(initial)):
    if initial[i] != target[i % 3]:
        c += 1

print(c)
