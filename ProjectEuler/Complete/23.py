from tqdm import tqdm

from Utilities.Factoring import divisors


def main():
    n = 28123

    abundants = [i for i in range(1, n) if sum(divisors(i)) > i]

    summers = [0 for _ in range(n + 1)]

    for i in tqdm(range(len(abundants))):
        for j in range(i, len(abundants)):
            s = abundants[i] + abundants[j]
            try:
                summers[s] = 1

            except IndexError:
                break

    print(sum([a for a in range(len(summers)) if summers[a] == 0]))


if __name__ == '__main__':
    main()
