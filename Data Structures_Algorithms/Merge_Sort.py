# Merge Sort

# It is used to merge different sorted arrays (lists) to become one

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_two_sorted_lists(left, right)


def merge_two_sorted_lists(a, b):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i = j = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1
    while i < len_a:
        sorted_list.append(a[i])
        i += 1

    while j < len_b:
        sorted_list.append(b[j])
        j += 1
    return sorted_list


if __name__ == "__main__":
    a = [5, 8, 12, 56]
    b = [7, 9, 45, 51]

    arr = [10, 3, 15, 7, 8, 23, 98, 29]

    print(f"{merge_two_sorted_lists(a, b)}")
    print(f"merge sort: {merge_sort(arr)}")


#  Optimize the code for efficiency


def merge_sort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left, right, arr)


def merge_two_sorted_lists(a, b, arr):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1
    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1

    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1


if __name__ == "__main__":
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9, 8, 7, 2],
        [1, 2, 3, 4, 5]
    ]

    for arr in test_cases:
        merge_sort(arr)
        print(arr)

# The Second Optimization

def merge_sort(arr):
    # Base case: if the array has 0 or 1 element, it is already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle index to split the array into two halves
    mid = len(arr) // 2

    # Recursively sort the left half
    left = merge_sort(arr[:mid])

    # Recursively sort the right half
    right = merge_sort(arr[mid:])

    # Merge the two sorted halves
    return merge_two_sorted_lists(left, right)


def merge_two_sorted_lists(a, b):
    # Initialize an empty list to store the merged sorted elements
    sorted_arr = []

    # Initialize pointers for both lists
    i = j = 0

    # Compare elements from both lists and append the smaller one to sorted_arr
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            sorted_arr.append(a[i])
            i += 1
        else:
            sorted_arr.append(b[j])
            j += 1

    # Append any remaining elements from list 'a' to sorted_arr
    sorted_arr.extend(a[i:])

    # Append any remaining elements from list 'b' to sorted_arr
    sorted_arr.extend(b[j:])

    # Return the merged and sorted array
    return sorted_arr


if __name__ == "__main__":
    # Define test cases
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9, 8, 7, 2],
        [1, 2, 3, 4, 5]
    ]

    # Apply merge_sort to each test case and print the sorted array
    for arr in test_cases:
        sorted_arr = merge_sort(arr)
        print(sorted_arr)

    # Define two separate sorted lists
    a = [5, 8, 12, 56]
    b = [7, 9, 45, 51]

    # Merge and sort the two separate lists
    merged_sorted_arr = merge_two_sorted_lists(a, b)

    # Print the merged and sorted array
    print(merged_sorted_arr)






