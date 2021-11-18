# Provinces and Gold

G, S, C = map(int, input().split())

p = G * 3 + S * 2 + C

if p >= 8:
    print("Province or ", end="")
elif p >= 5:
    print("Duchy or ", end="")
elif p >= 2:
    print("Estate or ", end="")

if p >= 6:
    print("Gold")
elif p >= 3:
    print("Silver")
else:
    print("Copper")
