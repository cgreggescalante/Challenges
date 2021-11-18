# Help a PhD candidate out!

n = int(input())

for _ in range(n):
    l = input()
    if l == "P=NP":
        print("skipped")
        continue
    a, b = map(int, l.split("+"))
    print(a + b)
