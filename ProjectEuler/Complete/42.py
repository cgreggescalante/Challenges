words = open('Resources/Words42.txt', 'r').readlines()
count = 0
word_vals = []
tris = []

for i in range(1, 21):
    val = (i * (i + 1)) // 2
    tris.append(val)

print(tris)

for word in words:
    letters = [a for a in word[:-1]]
    val = 0
    for i in letters:
        val += ord(i) - 64

    if val in tris:
        count += 1

print(count)
