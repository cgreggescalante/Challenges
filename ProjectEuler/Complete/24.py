from Utilities.LexicographicPermutations import iterate_digit_array

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


for _ in range(1000000-1):
    digits = iterate_digit_array(digits)

print(digits)
