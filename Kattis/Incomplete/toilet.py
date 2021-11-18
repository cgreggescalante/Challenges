# Toilet Seat

line = input()

state_1 = line[0]
state_2 = line[0]
state_3 = line[0]

count_1 = 0
count_2 = 0
count_3 = 0

for i in line[1:]:
    if i != state_1:
        count_1 += 1
        state_1 = i
    if state_1 != "U":
        count_1 += 1
        state_1 = "U"

    if i != state_2:
        count_2 += 1
        state_2 = i
    if state_2 != "D":
        count_2 += 1
        state_2 = "D"

    if i != state_3:
        count_3 += 1
        state_3 = i

print(count_1)
print(count_2)
print(count_3)
