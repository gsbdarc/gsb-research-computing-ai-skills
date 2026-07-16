import multiprocessing
import time
import math


def crunch_numbers():
    # Hold data in memory while doing CPU work
    data = list(range(12_500_000))  # ~100 MB per process
    end_time = time.time() + 30    # run for 30 seconds
    while time.time() < end_time:
        for i in range(10000):
            math.sqrt(i)


if __name__ == "__main__":
    num_cores = 4
    processes = []

    for _ in range(num_cores):
        p = multiprocessing.Process(target=crunch_numbers)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
