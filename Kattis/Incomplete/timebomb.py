# Time Bomb

tree = {
    "***": {
        "* *": {
            "* *": 0,
            "***": {
                "* *": 8,
                "  *": 9
            }
        },
        "  *": {
            "***": {
                "*  ": 2,
                "  *": 3
            },
            "  *": 7
        },
        "*  ": {
            "***": {
                "  *": 5,
                "* *": 6
            }
        }
    },
    "  *": 1,
    "* *": 4
}

lines = [input() for _ in range(5)]

lines = [[a[i*4:i*4+3] for i in range(len(a) // 4)] for a in lines]

res = ""
fail = False

for j in range(len(lines[0])):
    digit = [lines[i][j] for i in range(5)]

    pos = tree
    i = 0
    while i < 5:
        if digit[i] in pos:
            pos = pos[digit[i]]
            if type(pos) == int:
                break
        else:
            pos = -1
            break
        i += 1

    if pos == -1:
        print("BOOM!!")
        fail = True
        break
    else:
        res += str(pos)

print(res)

if not fail:
    print("BOOM!!" if int(res) % 6 else "BEER!!")
