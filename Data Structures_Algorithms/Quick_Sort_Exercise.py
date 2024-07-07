# Lumoto  Partitioning Quick Sort

def swap(a, b, arr):
    # Swap the elements at indices a and b in array arr
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]

def partition(elements, start, end):
    pivot = elements[end]  # Choosing the pivot as the last element
    i = start - 1          # Index of the smaller element

    # Traverse through the array from start to end-1
    for j in range(start, end):
        if elements[j] <= pivot:
            i += 1
            swap(i, j, elements)  # Swap if element is smaller than or equal to pivot

    # Place the pivot in the correct position
    swap(i + 1, end, elements)
    return i + 1  # Return the partition index

def quick_sort(elements, start, end):
    if start < end:
        # Partition the array and get the pivot index
        pi = partition(elements, start, end)
        # Recursively sort the left partition
        quick_sort(elements, start, pi - 1)
        # Recursively sort the right partition
        quick_sort(elements, pi + 1, end)

if __name__ == "__main__":
    tests = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],

        [],
        [6]
    ]

    for elements in tests:
        quick_sort(elements, 0, len(elements) - 1)
        print(f"sorted array: {elements}")
