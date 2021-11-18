def reverse(x):
    x = str(x)
    new = ""
    for i in x:
        new = i + new
    return int(new)


def is_palindrome(x):
    if x == reverse(x):
        return True
    return False


def check(x):
    for _ in range(50):
        x += reverse(x)
        if is_palindrome(x):
            return False
    return True


def main():
    count = 0

    for i in range(10000):
        if check(i):
            count += 1

    print(count)


if __name__ == "__main__":
    main()