# Equal or Not Equal
import re

t = int(input())


for _ in range(t):
    equality = input()
    equality = re.sub(r"[E]+", "E", equality)
    equality = re.sub(r"[E]+N", "-", equality)
    if equality.endswith("-"):
        equality = re.sub(r"^[N]+", "", equality)
    if equality.startswith("-"):
        equality = re.sub(r"[E]+$", "", equality)
    print(equality)
    if equality == "-":
        print("NO")
        continue

    if equality:
        changes = int(equality[0] != equality[-1] or (equality[0] == "N" and equality[-1] == "N"))
        for i, a in enumerate(equality[:-1]):
            if a != equality[i+1] or a == "N" and equality[i + 1] == "N":
                changes += 1
        print("YES" if (changes % 2 or not changes) else "NO")
    else:
        print("YES")
