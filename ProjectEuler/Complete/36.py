# Double-Based Palindromes


def palindrome(n):
    n = str(n)
    return n == n[::-1]


total = 0

for i in range(1000000):
    if palindrome(i):
        if palindrome(bin(i)[2:]):
            total += i

print(total)
