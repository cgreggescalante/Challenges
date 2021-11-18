# Coin Sums


def value(x, top):
    val = 0
    for i in options[:top]:
        val += i * x[i]
    return val


def find_increase():
    index = 1

    while index < 7:
        if value(coins, index) >= options[index]:
            return index
        index += 1

    return -1


coins = {
    1: 0,
    2: 0,
    5: 0,
    10: 0,
    20: 0,
    50: 0,
    100: 0
}

target = 200
coins[1] = target
options = [1, 2, 5, 10, 20, 50, 100]

count = 1

while True:
    increase = find_increase()

    if increase == -1:
        break

    coins[options[increase]] += 1

    deficit = value(coins, increase) - options[increase]

    for i in range(1, increase):
        coins[options[i]] = 0

    coins[options[0]] = deficit

    count += 1

print(count)
