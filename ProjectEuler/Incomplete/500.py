import multiprocessing
from multiprocessing import Process, Lock


def divisors(x):
    divs = 2
    for i in range(2, x//2 + 1):
        if x // i == x / i:
            divs += 1

    return divs


def check(interval, largest, lock):
    for i in range(interval[0], interval[1], 20):
        divs = divisors(i)
        with lock:
            if divs > largest[0]:
                largest[0] = divs
                largest[1] = i


max_divs = multiprocessing.Array('i', [0, 0])
count = 0
lock = Lock()
prev = [0, 0]
processes = 10
each = 100 * 20

if __name__ == '__main__':
    while True:
        intervals = []
        threads = []

        for i in range(processes):
            start = count + i * each
            end = start + each
            intervals.append([start, end])

        for i in range(4):
            threads.append(Process(target=check, args=(intervals[i], max_divs, lock)))

        for i in threads:
            i.start()
        for i in threads:
            i.join()

        if not prev[0] == max_divs[0]:
            print(max_divs[0], max_divs[1])
            prev[0], prev[1] = max_divs[0], max_divs[1]

        count += processes * each
