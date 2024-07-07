# Multiprocessing queue
# Processes can exchange data through file, shared memory, or message pipe
# Multiprocessing Queue is a shared memory
# There is another Queue module in python
# Queue module lives in in-process memory - used to share data between threads



import multiprocessing

def calc_square(numbers, q):
    for n in numbers:
        q.put(n*n)


if __name__ == "__main__":
    numbers = [2, 3, 5]
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=calc_square, args=(numbers, q))

    p.start()
    p.join()

    while q.empty() is False:
        print(q.get())





