# Perfect Matchings and RNA Secondary Structures

string = "UCCAAUCAUUGCUUCAUAAAAGAACCCGAUGCCGGGGAACAUGGGUGGUCACCAGUAUCGGUUGCGUCAGCUCU"

a = 0
g = 0

for i in string:
    if i == 'A':
        a += 1
    if i == 'G':
        g += 1

t = 1
for i in range(2, a+1):
    t *= i
for i in range(2, g+1):
    t *= i

print(t)