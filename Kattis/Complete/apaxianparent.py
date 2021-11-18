# Honour Thy (Apaxian) Parent

Y, P = input().split()

if Y[-1] in "aeiou":
    Y = Y[:-1]
elif Y.endswith("ex"):
    Y = Y[:-2]

print(Y + "ex" + P)
