# Ordering Strings of Varying Length Lexicographically

alpha = [a for a in "J D K C G Z A R F B".split()]
order = {}
for a in range(len(alpha)):
    order[alpha[a]] = a
n = 3

options = []

for i in alpha:
    options.append(i)

prev_options = options[:]
for i in range(n - 1):
    new_options = []
    for a in prev_options:
        for b in alpha:
            new_options.append(a + b)
    options.extend(new_options)
    prev_options = new_options


def greater(a, b):
    i = 0
    while i < len(a) and i < len(b):
        if order[a[i]] > order[b[i]]:
            return True
        i += 1


for i in range(len(options)):
    for j in range(len(options) - 1):
        if greater(options[j], options[j + 1]):
            options[j], options[j + 1] = options[j + 1], options[j]

for o in options:
    print(o)