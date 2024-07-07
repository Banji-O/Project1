# List Comprehension
# provides a way to transform one list into another

num = [1, 2, 3, 4, 5, 6, 7]

even = [i for i in num if i % 2 == 0]
print(even)

sqr_num = [i * i for i in num]
print(sqr_num)

# Set Comprehension
# Provides a way to transform one set into another
# Set is unordered collection of unique items.

xet = {1, 2, 3, 4, 5, 2, 3, 6, 7, 8}
print(xet)

ev = {i for i in xet if i % 2 == 0}
print(ev)

# Dictionary Comprehension

cities = ["Mumbai", "New York", "Paris", "Abuja"]
countries = ["India", "USA", "France", "Nigeria"]

places = {country: city for country, city in zip(countries, cities)}
print(places)