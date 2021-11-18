# Cubic Permutations


def is_permutation(a, b):
    sa = [c for c in str(a)]
    sb = [c for c in str(b)]

    for s in sa:
        if s in sb:
            sb.remove(s)
        else:
            return False
    return len(sb) == 0


p = 1
max_v = 0

while True:
    print(p)
    nums = []
    num_counter = {}
    n = int((10 ** p) ** (1/3.0) + .9)
    while n**3 < 10 ** (p + 1):
        nums.append(n**3)
        num_counter[n**3] = 1
        n += 1

    if len(nums) > 5:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if is_permutation(nums[i], nums[j]):
                    num_counter[nums[i]] += 1
                    num_counter[nums[j]] += 1

    for k, v in num_counter.items():
        if v > max_v:
            print(v, k)
            max_v = v

    if max_v == 5:
        break

    p += 1

