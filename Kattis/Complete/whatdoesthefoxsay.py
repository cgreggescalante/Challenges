# What does the fox say?

T = int(input())

for _ in range(T):
    noises = input().split()

    s = input()

    while s != "what does the fox say?":
        s = s.split()[-1]
        while s in noises:
            noises.remove(s)
        s = input()

    print(' '.join(noises))
