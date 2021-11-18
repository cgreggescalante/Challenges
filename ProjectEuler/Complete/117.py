# Red, Green, and Blue Tiles

known_mappings = {}


def count(total_length):
    try:
        a = known_mappings[total_length]
        return a
    except KeyError:
        pass
    total = 0

    for tile_length in [2, 3, 4]:
        for start in range(total_length - tile_length + 1):
            total += 1
            next_length = total_length - start - tile_length
            if next_length > 1:
                total += count(next_length)

    known_mappings[total_length] = total
    print(total_length, total)
    return total


for c in range(2, 51):
    count(c)
