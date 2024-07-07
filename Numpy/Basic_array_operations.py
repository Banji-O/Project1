# Numpy Basic Array

import numpy as np

a = np.array([5, 6, 9])
print(a[0])

a2 = np.array([[1, 2], [3, 4], [5, 6]])

print(a2.ndim)

print(a2.itemsize)

a3 = np.array([[1, 2], [3, 4], [5, 6]], dtype=np.float64)
print(f"a3 itemsize: {a3.itemsize}")
print(a3)

print(f"Array size: {a3.size}")
print(f"Array shape {a3.shape}")

a4 = np.array([[1, 2], [3, 4], [5, 6]], dtype=complex)
print(f"Complex {a4}")

zero = np.zeros((3, 4))
print(f"Zeros holders: \n{zero}")

ones = np.ones((3, 4))
print(f"Ones holders: \n{ones}")

rng = np.arange(1,5)
print(f"The range number between 1 - 5: \n{rng}")

rngstp = np.arange(1,10, 2)
print(f"The range number between 1 - 10 with step: \n{rngstp}")

lnsp = np.linspace(0, 10, 20)  # to generate 20 numbers between 0 and 10
print(f"The linearly spaced number: {lnsp}")

reshp = a2.reshape(2, 3)
print(f"Reshaped 3 by 2 to 2 by 3 \n{reshp}")

flt = a2.ravel()  # This is to flatten the s dimensional array
print(f"flattened array: \n{flt}")

# Mathematical functions
mn = a2.min()
print(f"The minimum number is: {mn}")

mx = a2.max()
print(f"The maximum number is: {mx}")

sm = a2.sum()
print(f"The sum is: {sm}")

smax = a2.sum(axis=0)  # to sum all elements in columns
print(f"The sum of column axis is: {smax}")

smaxr = a2.sum(axis=1)  # to sum all elements in rows
print(f"The sum of row axis is: {smaxr}")

sqrt = np.sqrt(a2)  # To get square root of numbers n array
print(f"The square root is: {sqrt}")

std = np.std(a2)  # To find standard deviation
print(f"The standard deviation is: {std}")

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])

print(f"The sum of x and y is: {x + y}")
print(f"the division of x and y is: {x/y}")

print(f"Matrix product of x and y: {x.dot(y)}")

