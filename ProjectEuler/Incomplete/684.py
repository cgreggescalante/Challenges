# Inverse Digit Sum

# Correct methods, just too slow


def s(n):
    return int(str(n % 9) + "9" * (n // 9))


def f(i):
    n = 3
    nums = [0, 1, 1]
    append = nums.append
    while n <= i:
        append(nums[n-1] + nums[n-2])
        n += 1
    return nums


n_max = 1
prev_total = 1


def S(k):
    global n_max, prev_total
    total = prev_total
    for n in range(n_max+1, k+1):
        total += s(n) % 1000000007
    n_max = k
    prev_total = total % 1000000007
    return total


def main():
    fibbonacci = f(90)

    total = 0
    for i in range(2, 20):
        total += S(fibbonacci[i]) % 1000000007
        print(total)

    print(total % 1000000007)

main()