# Poker Hands


def card_to_value(c):
    value_map = {
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }

    if c[0] in value_map:
        return value_map[c[0]]
    return int(c[0])


def hand_to_value(hand):
    return sum([card_to_value(i) for i in hand])


def high_card(hand):
    values = [card_to_value(i) for i in hand]

    return max(values)


def one_pair(hand):
    for i in range(len(hand)):
        for j in range(i+1, len(hand)):
            if hand[i][0] == hand[j][0]:
                return [hand[i], hand[j]]
    return 0


def two_pair(hand):
    pair1 = one_pair(hand[:])
    if pair1 == 0:
        return 0
    hand.remove(pair1[0])
    hand.remove(pair1[1])

    pair2 = one_pair(hand)
    if pair2 == 0:
        return 0
    return [pair1, pair2]


def three_of_kind(hand):
    for i in range(len(hand)):
        for j in range(i+1, len(hand)):
            for k in range(j+1, len(hand)):
                if hand[i][0] == hand[j][0] == hand[k][0]:
                    return [hand[i], hand[j], hand[k]]
    return 0


def straight(hand):
    values = [card_to_value(i) for i in hand]

    current = min(values)
    values.remove(current)

    while len(values) > 0:
        if current + 1 in values:
            current = current + 1
            values.remove(current)
        else:
            return 0
    return hand_to_value(hand)


def flush(hand):
    suit = hand[0][1]

    for card in hand:
        if not card[1] == suit:
            return 0
    return hand_to_value(hand[:])


def full_house(hand):
    three = three_of_kind(hand[:])
    if three == 0:
        return 0
    hand.remove(three[0])
    hand.remove(three[1])
    hand.remove(three[2])

    if len(hand) < 2:
        print(hand)

    if hand[0][0] == hand[1][0]:
        return hand_to_value(hand)
    return 0


def four_of_kind(hand):
    pairs = two_pair(hand[:])
    if pairs == 0:
        return 0
    if pairs[0][0][0] == pairs[1][0][0]:
        return hand_to_value([pairs[0][0], pairs[0][1], pairs[1][0], pairs[1][1]])
    return 0


def straight_flush(hand):
    if straight(hand) > 0 and flush(hand) > 0:
        return hand_to_value(hand)
    return 0


def royal_flush(hand):
    if straight_flush(hand) > 0:
        values = [card_to_value(i) for i in hand]
        if min(values) == 10:
            return 1
    return 0


def tiebreaker(p1, p2):
    p1_values = [card_to_value(i) for i in p1]
    p2_values = [card_to_value(i) for i in p2]

    while len(p1_values) > 0:
        a = max(p1_values)
        b = max(p2_values)
        if a > b:
            return 1
        elif a < b:
            return 0
        p1_values.remove(a)
        p2_values.remove(b)
    return "Tiebreaker Failed"


def evaluate(p1, p2):
    a = royal_flush(p1[:])
    b = royal_flush(p2[:])

    if a > b:
        return 1
    if a < b:
        return 0

    a = straight_flush(p1[:])
    b = straight_flush(p2[:])

    if a != 0:
        if b == 0:
            return 1
        if a > b:
            return 1
        if b > a:
            return 0
        return tiebreaker(p1[:], p2[:])
    if b != 0:
        return 0

    a = four_of_kind(p1[:])
    b = four_of_kind(p2[:])

    if a > 0 or b > 0:
        if a > b:
            return 1
        if b > a:
            return 0
        return tiebreaker(p1[:], p2[:])

    a = full_house(p1[:])
    b = full_house(p2[:])

    if a > 0 or b > 0:
        if a > b:
            return 1
        if b > a:
            return 0
        return tiebreaker(p1[:], p2[:])

    a = flush(p1[:])
    b = flush(p2[:])

    if a > 0 or b > 0:
        if a > b:
            return 1
        if b > a:
            return 0
        return tiebreaker(p1[:], p2[:])

    a = straight(p1[:])
    b = straight(p2[:])

    if a > 0 or b > 0:
        if a > b:
            return 1
        if b > a:
            return 0
        return tiebreaker(p1[:], p2[:])

    a = three_of_kind(p1[:])
    b = three_of_kind(p2[:])

    if len(str(a)) > 1:
        if len(str(b)) == 1:
            return 1
        a = hand_to_value(a[:])
        b = hand_to_value(b[:])
        if a > b:
            return 1
        if b > a:
            return 0
        return tiebreaker(p1[:], p2[:])
    if len(str(b)) > 1:
        return 0

    a = two_pair(p1[:])
    b = two_pair(p2[:])

    if len(str(a)) > 1:
        if len(str(b)) == 1:
            return 1
        a = hand_to_value(a[:])
        b = hand_to_value(b[:])
        if a > b:
            return 1
        if b > a:
            return 0
        return tiebreaker(p1[:], p2[:])
    if len(str(b)) > 1:
        return 0

    a = one_pair(p1[:])
    b = one_pair(p2[:])

    if len(str(a)) > 1:
        if len(str(b)) == 1:
            return 1
        a = hand_to_value(a[:])
        b = hand_to_value(b[:])
        if a > b:
            return 1
        if b > a:
            return 0
        return tiebreaker(p1[:], p2[:])
    if len(str(b)) > 1:
        return 0

    a = high_card(p1[:])
    b = high_card(p2[:])

    if a == b:
        return tiebreaker(p1[:], p2[:])
    if a > b:
        return 1
    if b > a:
        return 0
    return tiebreaker(p1[:], p2[:])


with open("/Resources/poker54.txt", 'r') as file:
    rounds = file.readlines()
    count = 0

    for i in rounds:
        cards = i.split()
        count += evaluate(cards[:5], cards[5:])

    print(count)