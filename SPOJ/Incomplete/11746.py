# Sum the Series
# ID: 11746
# Key: SUMUP

for _ in range(int(input())):
    print(round(sum([i / ((i**2 - i + 1) * (i**2 + i + 1)) for i in range(1, int(input())+1)]), 5))
