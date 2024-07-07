# Numpy Tutorial

import numpy as np

import time
import sys

ls = range(1000)
print(sys.getsizeof(5) * len(ls))

array = np.arange(1000)
print(array.size * array.itemsize)


size = 1000000
ls1 = range(size)
ls2 = range(size)

array1 = np.arange(size)
array2 = np.arange(size)

start = time.time()
result = [(x+y) for x, y in zip(ls1, ls2)]
print(f"python list took: {(time.time() - start)* 1000}")

# numpy Array
start1 = time.time()
result2 = array1 + array2
print(f"numpy took: {(time.time() - start1) * 1000}")

a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])

print(a1 + a2)

print(f"arange: {np.arange(10)}")