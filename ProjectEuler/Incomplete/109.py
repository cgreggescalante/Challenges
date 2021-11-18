# Darts

"""
    Scoring
        Board split into 20 slices numbered 1-20
        Outer red/green ring doubles score
        Inner ring triples score
        Center of board is the bull, worth 25 points
        Inner bull is worth 50
"""

valids = [a for a in range(1, 21)]
valids.extend([a for a in range(22, 41, 2)])
valids.extend([a for a in range(21, 41, 6)])
valids.extend([a for a in range(42, 61, 3)])
valids.extend([25, 50])


doubles = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 50]


def counter(score):
    ones = []
    twos = []
    threes = []

    # One dart
    if score in doubles:
        ones.append(["D" + str(score // 2)])

    # Two darts
    for double in doubles:
        d_string = "D" + str(double // 2)
        if double > score - 1:
            break
        remainder = score - double
        if remainder < 21:
            twos.append([d_string, "S" + str(remainder)])
        if remainder % 2 == 0 and remainder < 41:
            twos.append([d_string, "D" + str(remainder // 2)])
        if remainder % 3 == 0 and remainder < 61:
            twos.append([d_string, "T" + str(remainder // 3)])

    # Three darts
    for double in doubles:
        d_string = "D" + str(double // 2)
        if double > score - 2:
            break
        remainder = score - double
        for s in valids:
            if s > remainder - 1:
                break
            val = remainder - s
            s_strings = []
            if s < 21:
                s_strings.append("S" + str(s))
            if s < 41 and s % 2 == 0:
                s_strings.append("D" + str(s // 2))
            if s < 61 and s % 3 == 0:
                s_strings.append("T" + str(s // 3))

            for s_string in s_strings:
                arr = [d_string, s_string]
                if val < 21:
                    threes.append(arr + ["S" + str(val)])
                if val % 2 == 0 and val < 41:
                    threes.append(arr + ["D" + str(val // 2)])
                if val % 3 == 0 and val < 61:
                    threes.append(arr + ["T" + str(val // 3)])

    final_twos = {}
    for i in twos:
        try:
            a = final_twos[i[0]]
            if i[1] not in a:
                final_twos[i[0]].append(i[1:])
        except KeyError:
            final_twos[i[0]] = [i[1:]]

    two_total = 0
    for i in final_twos:
        two_total += len(final_twos[i])

    final_threes = {}
    for i in threes:
        try:
            a = final_threes[i[0]]
            if [i[1], i[2]] not in a and [i[2], i[1]] not in a:
                final_threes[i[0]].append(i[1:])
        except KeyError:
            final_threes[i[0]] = [i[1:]]

    three_total = 0
    for i in final_threes:
        three_total += len(final_threes[i])

    return len(ones) + two_total + three_total


total = 0
for i in range(2, 170):
    total += counter(i)

print(total)

