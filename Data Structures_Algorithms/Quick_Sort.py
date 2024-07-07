#  Quick Sort

def swap(a, b, arr):
    # Swap the elements at indices a and b in array arr
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]


def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]
    low = start + 1
    high = end

    # Continue until low and high pointers cross each other
    while True:
        # Move low pointer to the right while elements[low] <= pivot
        while low <= high and elements[low] <= pivot:
            low += 1

        # Move high pointer to the left while elements[high] > pivot
        while low <= high and elements[high] > pivot:
            high -= 1

        # If low and high pointers cross, break the loop
        if low > high:
            break

        # Swap elements at low and high pointers
        swap(low, high, elements)

    # Swap pivot with element at high pointer
    swap(pivot_index, high, elements)

    return high


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
