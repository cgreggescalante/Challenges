# Left Beehind

sweet, sour = map(int, input().split())

while sweet and sour:
    if sweet + sour == 13:
        print("Never speak again.")
    elif sour > sweet:
        print("Left beehind.")
    elif sweet == sour:
        print("Undecided.")
    elif sweet > sour:
        print("To the convention.")
    sweet, sour = map(int, input().split())
