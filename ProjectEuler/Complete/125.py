# Palindromic Sums


def palindrome(n):
    s = str(n)
    return s == s[::-1]


squares = [a*a for a in range(1, 10000)]

possibles = {}

for i in range(len(squares) - 1):
    c = squares[i]
    for j in range(i+1, len(squares)):
        c += squares[j]
        if c >= 1000:
            break
        possibles[c] = 0


total = 0

for p in sorted(possibles.keys()):
    if palindrome(p):
        print(p)
        total += p

print(total)
