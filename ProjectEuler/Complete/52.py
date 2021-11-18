one = 1

while True:
    two = one + one
    three = two + one
    four = three + one
    five = four + one
    six = five + one
    l = len(str(one))
    length = True
    for i in [two, three, four, five, six]:
        if not len(str(i)) == l:
            length = False
            break
    digits = True
    if length:
        # print(one, two, three, four, five, six)
        for i in [two, three, four, five, six]:
            if not sorted(str(i)) == sorted(str(one)):
                digits = False
                break
        if digits:
            print(one, two, three, four, five, six)
            break
    one += 1
