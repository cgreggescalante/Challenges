# The Next Palindrome

t = int(input())

for _ in range(t):
    K = int(input()) + 1

    while True:
        if str(K) == str(K)[::-1]:
            print(K)
            break
        K += 1
