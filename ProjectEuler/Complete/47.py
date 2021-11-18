def factor(n):
    facts = []
    for i in range(2, n):
        if n % i == 0:
            facts.append(i)
            news = factor(n // i)
            if not news:
                facts.append(n // i)
            else:
                for i in news:
                    facts.append(i)
            break
    return facts


def distincts(facts):
    dist = []
    for i in facts:
        if not i in dist:
            dist.append(i)
    return len(dist)


i = 1

while True:
    if distincts(factor(i)) == 4:
        if distincts(factor(i + 1)) == 4:
            if distincts(factor(i + 2)) == 4:
                print(i, i + 1, i + 2)
                if distincts(factor(i + 3)) == 4:
                    print(i, i + 1, i + 2, i + 3)
                    break
                else:
                    i += 3
            else:
                i += 2
        else:
            i += 1
    i += 1
