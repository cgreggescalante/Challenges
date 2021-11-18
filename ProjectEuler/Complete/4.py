# Largest Palindrome Product


def palindrome(n):
    s = str(n)
    if len(s) == 1:
        return True

    return s[:len(s) // 2] == s[len(s) // 2:][::-1]


top = 0

for a in range(999, 99, -1):
    for b in range(999, 99, -1):
        if a * b < top:
            break
        if palindrome(a * b):
            top = a * b

print(top)
