# A List Game

X = int(input())

facts = 0

while X % 2 == 0:
    facts += 1
    X //= 2

i = 3
while i < X**.5 + 1:
    while X % i == 0:
        facts += 1
        X //= i
    i += 2

if X > 1:
    facts += 1

print(facts)
