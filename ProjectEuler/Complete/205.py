# Dice Game

four_chances = {}
six_chances = {}

for a in range(1, 5):
    for b in range(1, 5):
        for c in range(1, 5):
            for d in range(1, 5):
                for e in range(1, 5):
                    for f in range(1, 5):
                        for g in range(1, 5):
                            for h in range(1, 5):
                                for i in range(1, 5):
                                    t = a + b + c + d + e + f + g + h + i
                                    try:
                                        four_chances[t] += 1
                                    except KeyError:
                                        four_chances[t] = 1

for a in range(1, 7):
    for b in range(1, 7):
        for c in range(1, 7):
            for d in range(1, 7):
                for e in range(1, 7):
                    for f in range(1, 7):
                        t = a + b + c + d + e + f
                        try:
                            six_chances[t] += 1
                        except KeyError:
                            six_chances[t] = 1

p_wins = 0
p_ties = 0
p_losses = 0

for key in four_chances:
    for k in six_chances:
        if key > k:
            p_wins += four_chances[key] * six_chances[k]
        if key == k:
            p_ties += four_chances[key] * six_chances[k]
        if key < k:
            p_losses += four_chances[key] * six_chances[k]

print(four_chances)
print(six_chances)
print(p_wins, p_ties, p_losses)
print(p_wins / (p_wins + p_ties + p_losses))
