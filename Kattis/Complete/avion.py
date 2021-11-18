# Avion

found = False

for i in range(5):
    if "FBI" in input():
        print(i+1, end=" ")
        found = True

if not found:
    print("HE GOT AWAY!")
