# Red, Green, or Blue Tiles
from tqdm import tqdm

known_mappings = {}


def count(total_length, tile_length):
    try:
        a = known_mappings[(total_length, tile_length)]
        return a
    except KeyError:
        pass

    total = 0

    if total_length >= tile_length:
        total += total_length - tile_length + 1

    for start in range(total_length - tile_length + 1):
        next_length = total_length - start - tile_length
        if next_length >= tile_length:
            total += count(total_length - start - tile_length, tile_length)

    known_mappings[(total_length, tile_length)] = total

    return total


result = 0

for length in tqdm(range(2, 5)):
    result += count(50, length)

print(result)