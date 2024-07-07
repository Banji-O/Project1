# Numpy Slicing, Stacking, Indexing

import numpy as np
n = [6, 7, 8]
print(n[0:2])

print(n[-1])

arr = np.array([6, 7, 8])
print(arr[-1])

ar = np.array([[6, 7, 8], [1, 2, 3], [9, 3, 2]])


print(ar[1, 2])
print(ar[0:2, 2])
print(ar[-1])
print(ar[-1, 0:2])
print(ar[:, 1:3])
print(ar)

for row in ar:
    print(ar)

for cell in ar.flat:  # ravel() can also be used
    print(cell)

# Stacking
a = np.arange(6).reshape(3, 2)
b = np.arange(6, 12).reshape(3, 2)

st = np.vstack((a, b))
print(st)

print(np.hstack((a, b)))

#  Split
array = np.arange(30).reshape(2, 15)
print(array)

splt = np.hsplit(array, 3)
print(splt)

print(f" 1st split: {splt[0]} \n\n 2nd split:{splt[1]} "
      f"\n\n 3rd split:{splt[2]}")

vsplt = np.vsplit(array, 2)
print(vsplt)

print(f"vertical split: {vsplt[0]}, \n vertical split2: {vsplt[1]}")

# Boolean Array

a1 = np.arange(12).reshape(3, 4)
a2 = a1 > 4
print(a1)
print(a2)

print(a1[a2])  # extracting elements in a1 that are greater than 4

a1[a2] = -1
print(a1[a2])

