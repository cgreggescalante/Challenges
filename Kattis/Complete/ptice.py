# Ptice

a = "ABC"
b = "BABC"
c = "CCAABB"

ac, bc, cc = 0, 0, 0

n = int(input())

correct = input()

for i in range(len(correct)):
    if correct[i] == a[i % 3]:
        ac += 1
    if correct[i] == b[i % 4]:
        bc += 1
    if correct[i] == c[i % 6]:
        cc += 1

m = max([ac, bc, cc])
print(m)
if m == ac:
    print("Adrian")
if m == bc:
    print("Bruno")
if m == cc:
    print("Goran")
