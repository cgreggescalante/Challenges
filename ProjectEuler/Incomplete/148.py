# Exploring Pascal's Triangle

known = {"0:0": 1}


def iterators(target):
    rows = 10 ** target
    row = [1]
    yield 1
    for r in range(1, rows - 1):
        new_row = [1]
        yield 1
        for i in range(1, r - 1):
            new_row.append((row[i] + row[i + 1]) % 7)
            yield new_row[-1]
        yield 1
        # if r % 2 == 0:
        #     new_row.append(new_row[-1])
        row = new_row

# def combinations(n, r):
#     if r > n:
#         raise Exception("r must be less than n")
#     if r == n or n <= 1 or r < 1:
#         return 1
#
#     s = f"{n}:{r}"
#     if s in known:
#         return known[s]
#     else:
#         try:
#             v = combinations(n - 1, r) + combinations(n - 1, r - 1)
#         except RecursionError:
#             print(n, r)
#         known[s] = v
#         return v
#


target = 2
#
# for row in tqdm(range(10**target)):
#     for col in range((row + 1) // 2):
#         if combinations(row, col) % 7:
#             t += 2
#     if row % 2 == 0:
#         if combinations(row, row // 2) % 7:
#             t += 1
#
# print(t)

t = 0
for i in iterators(target):
    # print(i % 7)
    if i % 7 == 0:
        t += 1

print(t)
