# Adding together values in list
# tom = [2400, 3400, 3500]
# joe = [200, 500, 700]
#
# def calculate_exp(total):
#     total_sum = 0
#     for i in total:
#         total_sum += i
#     return total_sum
#
# toms_total = calculate_exp(tom)
# joes_total = calculate_exp(joe)
# print('Tom\'s total expenses is: ', toms_total,
#       '\n\nJoe\'s total expenses is: ', joes_total)


# Adding two values

# def sum(a , b):
#     total = a + b
#     return total
#
# x = sum(a = 77, b = 23)
# print(x)

#  GLOBAL AND LOCAL VARIABLE
myself = 'Banji --> outside function'  # Global variable is defined outside of a function

def myname(name):
    print(name, '<-- this is a variable defined within function')

x = myname('Raphael')


def greet():
    print("Hello, world!")

def get_current_time():
    import datetime
    return datetime.datetime.now()

def generate_random_number():
    import random
    return random.randint(1, 100)

def print_menu():
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")

# Calling the functions
greet()
current_time = get_current_time()
print("Current time:", current_time)
random_number = generate_random_number()
print("Generated random number:", random_number)
print("Menu:")
print_menu()
