# Numpy nditer

import numpy as np

a = np.arange(12).reshape(3, 4)

print(a)

for row in a:
    for cell in row:
      print(cell)  # this will flatten the 2 dimentional array

for c in a.ravel():   # this will flatten the 2 dimentional array
    print(c)


for x in np.nditer(a, order='C'):
    print(x)  # It will flatten in C order (row by row)

for x in np.nditer(a, order='F'):
    print(x)  # It will flatten in Fortran order (column by column)

for y in np.nditer(a, order='F', flags=['external_loop']):
    print(y)  # iterates column by column

for w in np.nditer(a,op_flags=['readwrite']):
    w[...]=w*w  # it would square the array
    print(w)

#  iterating over 2 arrays simultaneously

c = np.arange(12).reshape(3, 4)

b = np.arange(3, 15, 4).reshape(3,1)

for ar, ra in np.nditer([c, b]):
    print(ar, ra)
