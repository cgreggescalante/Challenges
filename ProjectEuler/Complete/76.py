# Counting Summations


def value(x, top):
    val = 0
    for i in options[:top]:
        val += i * x[i]
    return val


def find_increase():
    index = 1

    while index < 99:
        if value(coins, index) >= options[index]:
            return index
        index += 1

    return -1


coins = {}

for a in range(1, 100):
    coins[a] = 0

coins[1] = 100

options = [a for a in range(1, 100)]

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

    if count % 100000 == 0:
        print(count)

print(count)
