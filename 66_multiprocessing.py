# ****************************
# Python multiprocessing
# ****************************
# multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL use for thread
#                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                   multithreading = better for io bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():

    a = Process(target=counter, args=(10000,))
    b = Process(target=counter, args=(10000,))

    a.start()
    b.start()

    a.join()
    b.join()

    print('finished in: ',time.perf_counter(),'seconds')


if __name__=='__main__':
    main()
