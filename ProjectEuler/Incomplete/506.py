# Clock Sequence
# 15,000 years in current implementation
from tqdm import tqdm

current = 0
up = True


def get_next():
    global up, current
    if up and current == 4 or not up and current == 1:
        up = not up

    if up:
        current += 1
    else:
        current -= 1

    return current


sequence = ""

for i in tqdm(range(1, 10**14+1)):
    sequence = ""
    total = 0

    while total < i:
        val = get_next()
        total += val
        if i == 10**14:
            sequence += str(val)

print(int(sequence) % 123454321)