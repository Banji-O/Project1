# Shell Sort

# It is an optimization over insertion sort. Insertion sort undergoes many comparisons and swaps when sorting arry

# Shell makes use of a method called gap. It divides array into number of gap stipulated

# Star with gap n/2 and keep reducng gap by n/2. Last iteration should gap 1

def shell_sort(arr):
    size = len(arr)
    gap = size // 2

    while gap > 0:
        for i in range(gap, size):
            anchor = arr[i]
            j = i
            while j >= gap and arr[j - gap] > anchor:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = anchor
        gap = gap // 2


if __name__ == "__main__":
    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1, 5, 8, 9],
        [234, 3, 1, 56, 34, 12, 9, 12, 1300],
        [5],
        [21, 38, 29, 17, 4, 25, 11, 32, 9]
    ]

    for elements in tests:
        shell_sort(elements)
        print(elements)

"""
Exercise:
Sort the elements below by using Shell Sort. modify the shell sort with
duplicate removal, swap if first element is bigger than second, and do nothing if element is smaller, but if values are same, 
delete one of the two elements before starting the next pass for the
reduced gap.
data = [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]
the output should look like this: [0, 1, 2, 3, 5, 7, 8, 9]
"""

def shell_sort_with_duplicates_removal(arr):
    # Get the length of the array
    n = len(arr)
    # Initialize the gap, starting with half the length of the array
    gap = n // 2

    # Continue the loop until the gap is reduced to 0
    while gap > 0:
        # Perform insertion sort for the elements with the current gap
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Shift earlier gap-sorted elements up until the correct location for arr[i] is found
            while j >= gap and arr[j - gap] >= temp:
                if arr[j - gap] == temp:
                    temp = None  # Mark for removal
                    break
                arr[j] = arr[j - gap]
                j -= gap
            if temp is not None:
                arr[j] = temp
        # Reduce the gap size and repeat the process
        gap //= 2

    # Final pass to remove any remaining duplicates after sorting
    i = 0
    while i < len(arr) - 1:
        # If the current element is the same as the next element, remove the next element
        if arr[i] == arr[i + 1]:
            del arr[i + 1]
        else:
            i += 1

    return arr

if __name__ == "__main__":
    # Define the data to be sorted
    data = [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]
    # Call the sorting function and store the result
    sorted_unique_data = shell_sort_with_duplicates_removal(data)
    # Print the sorted list without duplicates
    print(sorted_unique_data)
