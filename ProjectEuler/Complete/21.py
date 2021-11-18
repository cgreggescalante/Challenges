# Amicable Numbers
from Utilities.Factoring import divisors


def main():
    amicable = []

    for i in range(10000):
        if i not in amicable:
            s = sum(divisors(i))
            sum_sum = sum(divisors(s))
            if i == sum_sum and not i == s:
                amicable.append(i)
                amicable.append(s)

    print(sum(amicable))


if __name__ == "__main__":
    main()
