# Anagramic Squares
from math import sqrt


def evaluate(square, a, b):
    global max_square
    m_dict = {}
    reps = False
    for i in tuple(zip(a, str(square))):
        if i[0] in m_dict:
            if m_dict[i[0]] != int(i[1]):
                reps = True
                break
        for k, v in m_dict.items():
            if k != i[0] and v == int(i[1]):
                reps = True
                break
        m_dict[i[0]] = int(i[1])

    if not reps:
        if is_square(b, m_dict):
            for w in [a, b]:
                z = mapped_string(w, m_dict)
                if z > max_square:
                    print(z, s)
                    print([a, b], w)
                    max_square = z


def is_permutation(a, b):
    a = [c for c in a]

    for c in b:
        if c in a:
            a.remove(c)
        else:
            return False
    return len(a) == 0


def is_square(a, d):
    if d[a[0]] == 0:
        return False

    n = mapped_string(a, d)

    sn = sqrt(n)
    return sn == int(sn)


def mapped_string(a, d):
    n = 0
    for i in range(len(a)):
        try:
            n += d[a[len(a) - i - 1]] * 10 ** i
        except KeyError:
            print(a, d)
            print(a[len(a) - i - 1])
            quit(69)
    return n


anagrams = []

with open("C:\\Users\\Conor\\PycharmProjects\\EulerStuff\\Resources\\words98.txt") as file:
    words = file.readlines()
    words = [a[:-1] for a in words]

    anagrams = []
    for a in range(len(words)-1):
        for b in range(a+1, len(words)):
            if is_permutation(words[a], words[b]):
                if words[a][::-1] != words[b]:
                    anagrams.append([words[a], words[b]])


max_square = 0


for a in anagrams:
    squares = []
    n = 0
    while True:
        n += 1
        if n ** 2 > 10**len(a[0]) - 1:
            break
        if n ** 2 > 10**(len(a[0]) - 1):
            squares.append(n**2)
    for s in squares:
        evaluate(s, a[0], a[1])
        evaluate(s, a[1], a[0])
