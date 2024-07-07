# Decorators
# Decorator allows wrapping of function in another function

import time

def calc_square(numbers):
    start = time.time()
    result = []
    for number in numbers:
        result.append(number*number)
    end = time.time()
    print(f"calc_square {(end - start) * 1000} milli-seconds")
    return result

def calc_cube(numbers):
    start = time.time()
    result = []
    for number in numbers:
        result.append(number*number*number)
    end = time.time()
    print(f"calc_cube {(end - start) * 1000} milli-seconds")
    return result

array = range(1, 100000)
out_square = calc_square(array)
out_cube = calc_cube(array)


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {(end - start) * 1000} mil sec")
        return result
    return wrapper
@time_it
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result

@time_it
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result

array = range(1, 100000)
out_square = calc_square(array)
out_cube = calc_cube(array)


