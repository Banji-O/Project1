# Multithreading

# This could be likened to tasks performed at the same time.

import time

def calc_square(numbers):
     print("calculate square numbers")
     for n in numbers:
         time.sleep(0.2)
         print(f"square: {n*n}")


def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print(f"cube: {n*n*n}")


arr = [2, 3, 8, 9]
t = time.time()
calc_square(arr)
calc_cube(arr)

print(f"done in: {time.time() - t} seconds")
print(f"Hah--- I am done with all my work now!")

import threading


def calc_square(numbers):
    print("calculate square numbers")
    for n in numbers:
        time.sleep(0.2)
        print(f"square: {n * n}")


def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print(f"cube: {n * n * n}")


arr = [2, 3, 8, 9]
t = time.time()
t1 = threading.Thread(target=calc_square, args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print(f"done in: {time.time() - t} seconds")
print(f"Hah--- I am done with all my work now! after threading")