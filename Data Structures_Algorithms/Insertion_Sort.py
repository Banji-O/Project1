# Insertion Sort
# It is suitable for small size of array or list

import numpy as np

def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j >= 0 and anchor < elements[j]:
            elements[j + 1] = elements[j]
            j = j - 1
        elements[j + 1] = anchor

if __name__ == "__main__":
    element = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
        ]

    for elements in element:
        insertion_sort(elements)
        print(elements)


# Commented Version

# Insertion Sort
# It is suitable for small size of arrays or lists

def insertion_sort(elements):
    # Start from the second element (index 1) because the first element is already "sorted"
    for i in range(1, len(elements)):
        anchor = elements[i]  # The element to be compared
        j = i - 1  # The last element of the sorted portion of the list

        # Move elements of the sorted portion one position to the right
        while j >= 0 and anchor < elements[j]:
            elements[j + 1] = elements[j]
            j = j - 1
        elements[j + 1] = anchor  # Place the anchor in its correct position

if __name__ == "__main__":
    # Test cases for insertion sort
    element = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    # Sort each list using insertion sort and print the sorted list
    for elements in element:
        insertion_sort(elements)  # Sort the list
        print(elements)  # Print the sorted list
