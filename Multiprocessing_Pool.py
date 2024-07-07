
# Multiprocessing Pool

# This is a process of sharing task among all the processing cores
# in a CPU, this is called parallel processing. Dividing task among cores is called Map
# combining the result in the output is called Reduce

from multiprocessing import Pool

def f(n):
    return n*n


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]
    p = Pool()
    result = p.map(f, array)  # divides task between cores
    print(result)


import time

def f(n):
    sum = 0
    for x in range(1000):
        sum += x*x
    return sum


if __name__ == "__main__":
    t1 = time.time()
    p = Pool()
    result = p.map(f, range(100000))  # divides task between cores
    p.close()
    p.join()

    print(f"Pool took: {time.time() - t1}")

    t2 = time.time()
    result = []
    for x in range(100000):
        result.append(f(x))
    print(f"Serial processing took: {time.time() - t2}")


def f(n):
    return n*n

if __name__ == "__main__":
    p = Pool(processes=3)
    result = p.map(f, [1, 2, 3, 4, 5])
    for n in result:
        print(n)

