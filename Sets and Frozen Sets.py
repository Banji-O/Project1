# Sets and Frozen Sets
# Frozen a set means content will not be changed
# Set is an unordered collection of unique elements.

basket = {"orange", "apple", "mango", "apple", "orange"}
print(basket)

num = set()
num.add(1)
print(num)

num.add(2)

print(num)
print(type(num))

# Frozen Set

numbers = [1, 2, 3, 4, 2, 3, 4]
unique = set(numbers)
print(unique)

fs = frozenset(numbers)
print(fs)

# fs.add(5) will generate AttributeError

x = {"a", "b", "c"}
"a" in x

"g" in x

y = {"a", "g", "h"}
# UNION OPERATION
print("X union Y - ", x|y)

# INTERSECTION OPERATION
print("X intersect Y", x&y)

# DIFFERRENCE OPERATION
print(x-y)
print(y-x)

#Subset Operation
print("X subset Y", x < y)