# Linear Search
trans = [
    {"name": "reema", "device_id": "12AB56", "amount": 56},
    {"name": "aamir", "device_id": "679X1", "amount": 123},
    {"name": "mahesh", "device_id": "E451J", "amount": 87},
    {"name": "andrea", "device_id": "00Z77", "amount": 644}
]


def find_transaction(transactions):
    for index, element in enumerate(transactions):
        if element["device_id"] == "00Z77":
            return index
    return -1


search = find_transaction(trans)

print(search)

# Decorator
import time


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {(end - start) * 1000} mil sec")
        return result

    return wrapper


# Binary Search --- n/2

@time_it
def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
    return -1  # if element not found


if __name__ == "__main__":
    # numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    # number_to_find = 45

    numbers_list = [i for i in range(1000001)]
    number_to_find = 1000000

    index = linear_search(numbers_list, number_to_find)
    print(f"Number found at index {index} using linear search")


@time_it
def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index + 1

        else:
            right_index = mid_index - 1

    return -1


if __name__ == "__main__":
    # numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    # number_to_find = 15

    numbers_list = [i for i in range(1000001)]
    number_to_find = 1000000

    ind = binary_search(numbers_list, number_to_find)
    print(f" The number '{number_to_find}' found at index {ind} using binary search")


# Recursion (in recursion, loops are not used)
def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2

    if mid_index >= len(numbers_list) or mid_index < 0:
        return -1

    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        return mid_index

    if mid_number < number_to_find:
        left_index = mid_index + 1

    else:
        right_index = mid_index - 1

    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)


if __name__ == "__main__":
    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find = 21

    indx = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list))
    print(f" The number '{number_to_find}' found at index {indx} using binary search")



# Simplified Version

# Linear Search Example
trans = [
    {"name": "reema", "device_id": "12AB56", "amount": 56},
    {"name": "aamir", "device_id": "679X1", "amount": 123},
    {"name": "mahesh", "device_id": "E451J", "amount": 87},
    {"name": "andrea", "device_id": "00Z77", "amount": 644}
]

# Function to find a transaction by device_id using linear search
def find_transaction(transactions):
    for index, element in enumerate(transactions):  # Iterate through each transaction
        if element["device_id"] == "00Z77":  # Check if the device_id matches "00Z77"
            return index  # Return the index if found
    return -1  # Return -1 if not found

search = find_transaction(trans)  # Search for the transaction
print(search)  # Print the result of the search

# Decorator to measure execution time of a function
import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()  # Record start time
        result = func(*args, **kwargs)  # Execute the function
        end = time.time()  # Record end time
        print(f"{func.__name__} took {(end - start) * 1000} mil sec")  # Print the execution time
        return result  # Return the result of the function
    return wrapper  # Return the wrapper function

# Linear Search Function with Time Decorator
@time_it
def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):  # Iterate through each number
        if element == number_to_find:  # Check if the current element matches the number to find
            return index  # Return the index if found
    return -1  # Return -1 if not found

if __name__ == "__main__":
    numbers_list = [i for i in range(1000001)]  # Create a list of numbers from 0 to 1,000,000
    number_to_find = 1000000  # Number to find in the list

    index = linear_search(numbers_list, number_to_find)  # Search for the number
    print(f"Number found at index {index} using linear search")  # Print the result

# Binary Search Function with Time Decorator
@time_it
def binary_search(numbers_list, number_to_find):
    left_index = 0  # Initialize the left index
    right_index = len(numbers_list) - 1  # Initialize the right index

    while left_index <= right_index:  # Continue while the left index is less than or equal to the right index
        mid_index = (left_index + right_index) // 2  # Calculate the middle index
        mid_number = numbers_list[mid_index]  # Get the middle number

        if mid_number == number_to_find:  # Check if the middle number is the number to find
            return mid_index  # Return the middle index if found

        if mid_number < number_to_find:  # If the middle number is less than the number to find
            left_index = mid_index + 1  # Move the left index to the right of the middle index
        else:  # If the middle number is greater than the number to find
            right_index = mid_index - 1  # Move the right index to the left of the middle index

    return -1  # Return -1 if not found

if __name__ == "__main__":
    numbers_list = [i for i in range(1000001)]  # Create a list of numbers from 0 to 1,000,000
    number_to_find = 1000000  # Number to find in the list

    ind = binary_search(numbers_list, number_to_find)  # Search for the number using binary search
    print(f"The number '{number_to_find}' found at index {ind} using binary search")  # Print the result

# Recursive Binary Search Function
def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:  # Base case: If right index is less than left index, the number is not found
        return -1

    mid_index = (left_index + right_index) // 2  # Calculate the middle index

    if mid_index >= len(numbers_list) or mid_index < 0:  # Check for out-of-bounds indices
        return -1

    mid_number = numbers_list[mid_index]  # Get the middle number

    if mid_number == number_to_find:  # Check if the middle number is the number to find
        return mid_index  # Return the middle index if found

    if mid_number < number_to_find:  # If the middle number is less than the number to find
        left_index = mid_index + 1  # Move the left index to the right of the middle index
    else:  # If the middle number is greater than the number to find
        right_index = mid_index - 1  # Move the right index to the left of the middle index

    # Recursively call the function with the updated indices
    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)

if __name__ == "__main__":
    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]  # List of numbers
    number_to_find = 21  # Number to find in the list

    indx = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list))  # Search for the number using recursive binary search
    print(f"The number '{number_to_find}' found at index {indx} using binary search")  # Print the result
