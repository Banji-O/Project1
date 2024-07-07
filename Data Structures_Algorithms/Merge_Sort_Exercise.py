# Merge Sort Exercise

def merge_sort(arr, key, descending=False):
    # Base case: if the array has 0 or 1 element, it is already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle index to split the array into two halves
    mid = len(arr) // 2

    # Recursively sort the left half
    left = merge_sort(arr[:mid], key, descending)

    # Recursively sort the right half
    right = merge_sort(arr[mid:], key, descending)

    # Merge the two sorted halves
    return merge_two_sorted_lists(left, right, key, descending)


def merge_two_sorted_lists(a, b, key, descending):
    # Initialize an empty list to store the merged sorted elements
    sorted_arr = []

    # Initialize pointers for both lists
    i = j = 0

    # Compare elements from both lists based on the key and order
    while i < len(a) and j < len(b):
        if descending:
            if a[i][key] >= b[j][key]:
                sorted_arr.append(a[i])
                i += 1
            else:
                sorted_arr.append(b[j])
                j += 1
        else:
            if a[i][key] <= b[j][key]:
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
    # List of athletes
    elements = [
        {"name": "vedanth", "age": 17, "time_hours": 1},
        {"name": "rajab", "age": 12, "time_hours": 3},
        {"name": "vignesh", "age": 21, "time_hours": 2.5},
        {"name": "chinmay", "age": 24, "time_hours": 1.5}
    ]

    # Sort elements by 'time_hours' in descending order
    sorted_elements = merge_sort(elements, key='time_hours', descending=True)
    print(sorted_elements)

    # Example of sorting by 'age' in ascending order
    sorted_elements_by_age = merge_sort(elements, key='age', descending=False)
    print(sorted_elements_by_age)
