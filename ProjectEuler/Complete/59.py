cipher = open('Resources/Cipher59.txt', 'r').read()

cipher = [int(a) for a in cipher.split()]

words = open('10000words.txt', 'r').readlines()
words = [a[:-1] for a in words]

alpha = ['a', 'b', 'c', 'd',
         'e', 'f', 'g', 'h',
         'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q',
         'r', 's', 't', 'u',
         'v', 'w', 'x', 'y',
         'z']


def to_check(message):
    comp = 'to'
    for i in range(len(message) - 1):
        one = message[i] == comp[0]
        two = message[i + 1] == comp[1]
        if one and two:
            return True
    return False


def and_check(message):
    comp = 'and'
    for i in range(len(message)-2):
        one = message[i] == comp[0]
        two = message[i + 1] == comp[1]
        three = message[i + 2] == comp[2]
        if one and two and three:
            if to_check(message):
                return True
            return False


def of_check(message):
    comp = 'of'
    for i in range(len(message)-1):
        one = message[i] == comp[0]
        two = message[i + 1] == comp[1]
        if one and two:
            if and_check(message):
                return True
            return False


def the_check(message):
    comp = 'the'
    for i in range(len(message)-2):
        one = message[i] == comp[0]
        two = message[i + 1] == comp[1]
        three = message[i + 2] == comp[2]
        if one and two and three:
            if of_check(message):
                return True
            return False


def decode(k, message):
    decoded = []
    for i in range(len(message)):
        new = message[i] ^ ord(k[i % 3])
        decoded.append(chr(new))
    return decoded


def final(message):
    total = 0
    for i in message:
        total += ord(i)
    return total


for x in alpha:
    for y in alpha:
        for z in alpha:
            key = x + y + z
            print(key)
            new = decode(key, cipher)
            if the_check(new):
                to_print = ''
                for i in new:
                    to_print += i
                print(to_print)
                if input():
                    print(final(new))
                    quit()

