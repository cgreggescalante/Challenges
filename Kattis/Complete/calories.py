# Calories From Fat

line = input()
prev = ""
cals = [9, 4, 4, 4, 7]


def eval_perc(meal):
    known_total = sum([a for a in meal if type(a) == int])
    perc_total = sum([int(a[:-1]) for a in meal if type(a) == str])

    one_perc = known_total / (100 - perc_total)

    for i in range(5):
        if type(meal[i]) == str:
            meal[i] = int(meal[i][:-1]) * one_perc

    return meal


while True:
    arr = []
    while line != "-":
        line = line.split()
        for i in range(5):
            if "g" in line[i]:
                line[i] = int(line[i][:-1]) * cals[i]
            elif "C" in line[i]:
                line[i] = int(line[i][:-1])
            elif "%" in line[i]:
                if int(line[i][:-1]) == 0:
                    line[i] = 0
        line = eval_perc(line)
        arr.append(line)
        line = input()
    ft = sum([a[0] for a in arr])
    t = sum([sum(a) for a in arr])
    print(f"{round(ft / t * 100)}%")
    line = input()
    if line == "-":
        break

