# Diophante Equation
from math import sqrt
import multiprocessing


class Worker(multiprocessing.Process):
    def __init__(self, jobs, results):
        multiprocessing.Process.__init__(self)
        self.jobs = jobs
        self.results = results

    def run(self):
        while True:
            next_job = self.jobs.get()
            if next_job is None:
                print(f"{self.name}: Exiting")
                self.jobs.task_done()
                break
            self.results.put([next_job, min_x(next_job)])
            self.jobs.task_done()
        return


def min_x(D):
    d2 = sqrt(D)
    if int(d2) == d2:
        return -1
    for y in range(1, 2**64):
        n = y ** 2
        x = sqrt(n * D + 1)
        if int(x) == x:
            return int(x)


if __name__ == '__main__':
    p = multiprocessing.Pool()
    jobs = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()

    for i in range(2, 1001):
        jobs.put(i)

    num_proc = multiprocessing.cpu_count() * 2

    for _ in range(num_proc):
        jobs.put(None)

    procs = [Worker(jobs, results) for _ in range(num_proc)]

    for p in procs:
        p.start()

    jobs.join()

    big_d = 0
    big = 0
    while not results.empty():
        r = results.get()
        if r[1] > big:
            big = r[1]
            big_d = r[0]
        print(f"{r[0]} {r[1]}")
    print()
    print(big_d, big)

