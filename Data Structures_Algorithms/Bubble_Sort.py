# Bubble SOrt


def bubble_sort(elements):
    size = len(elements)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True
        if not swapped:
            break



if __name__ == "__main__":
    elements = [5, 9, 2, 1, 67, 34, 88, 34]
    elements = [1, 2, 3, 4, 2]
    elements = ["mona", "dhaval", "aamir", "tina", "chang"]

    bubble_sort(elements)
    print(elements)


def bubble_sort(elements, key):
    n = len(elements)
    print(f"The length is: {n}")
    for i in range(n):
        for j in range(n-i-1):
            #print(f"The value of j \n{j}")
            if elements[j][key] > elements[j+1][key]:
                elements[j], elements[j+1] = elements[j+1], elements[j]

# List of transactions
transactions = [
    {"name": "mona", "amount": 1000, "device": "iphone-10"},
    {"name": "dhaval", "amount": 400, "device": "google-pixel"},
    {"name": "kathy", "amount": 200, "device": "vivo"},
    {"name": "aamir", "amount": 800, "device": "iphone-8"}
]

# Sort the transactions by amount using bubble sort
bubble_sort(transactions, key='amount')

# Print the sorted transactions
print("Sorted transactions by amount:")
for transaction in transactions:
    print(transaction)

# Commented Version

# Bubble Sort Function for Simple List
def bubble_sort(elements):
    size = len(elements)  # Get the length of the list

    # Loop through each element in the list
    for i in range(size - 1):
        swapped = False  # Initialize a flag to check if a swap occurred
        # Loop to compare each element with the next one
        for j in range(size - 1 - i):
            if elements[j] > elements[j + 1]:  # Compare the current element with the next element
                # Swap the elements if they are in the wrong order
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
                swapped = True  # Set the flag to True if a swap occurred
        if not swapped:  # If no swaps occurred, the list is already sorted
            break


if __name__ == "__main__":
    # Test cases for bubble sort
    elements = [5, 9, 2, 1, 67, 34, 88, 34]
    bubble_sort(elements)  # Sort the list
    print("Sorted list:", elements)  # Print the sorted list

    elements = [1, 2, 3, 4, 2]
    bubble_sort(elements)  # Sort the list
    print("Sorted list:", elements)  # Print the sorted list

    elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    bubble_sort(elements)  # Sort the list
    print("Sorted list:", elements)  # Print the sorted list


# Bubble Sort Function for List of Dictionaries
def bubble_sort(elements, key):
    n = len(elements)  # Get the length of the list
    print(f"The length is: {n}")

    # Loop through each element in the list
    for i in range(n):
        # Loop to compare each element with the next one
        for j in range(n - i - 1):
            # Compare the value of the key in the current dictionary with the next one
            if elements[j][key] > elements[j + 1][key]:
                # Swap the dictionaries if they are in the wrong order
                elements[j], elements[j + 1] = elements[j + 1], elements[j]


# List of transactions (dictionaries)
transactions = [
    {"name": "mona", "amount": 1000, "device": "iphone-10"},
    {"name": "dhaval", "amount": 400, "device": "google-pixel"},
    {"name": "kathy", "amount": 200, "device": "vivo"},
    {"name": "aamir", "amount": 800, "device": "iphone-8"}
]

# Sort the transactions by the 'amount' key using bubble sort
bubble_sort(transactions, key='amount')

# Print the sorted transactions
print("Sorted transactions by amount:")
for transaction in transactions:
    print(transaction)
